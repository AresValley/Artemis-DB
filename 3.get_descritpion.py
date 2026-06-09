import re
import requests
import json
import time
from tqdm import tqdm
import wikitextparser as wtp

from utils.constants import ProjectPath
from models.signal import Signal


def _wikitext2markdown(wikitext):
    try:
        base_url = "https://www.sigidwiki.com/wiki/"

        # 1. Rimuove i menu/navigazione iniziale in HTML (span/div)
        wikitext = re.sub(
            r"^\s*<(span|div)[^>]*>[\s\S]*?<\/\1>", "", wikitext, flags=re.IGNORECASE
        )

        # 2. Parsing del Wikitext con la nuova libreria
        parsed = wtp.parse(wikitext)

        # 3. Rimuove TUTTI i template ({{Cell}}, {{Signal ...}}) in modo nativo
        for template in parsed.templates:
            del template[:]

        # 4. ISOLAMENTO DELL'INTRODUZIONE
        # parsed.sections[0] contiene sempre il testo prima del primo titolo (==)
        if parsed.sections:
            testo = parsed.sections[0].contents
        else:
            testo = parsed.string

        # 5. CONVERSIONE E PULIZIA LINK
        # 5a. Convertiamo i link con testo esplicito https://www.testo.com/ -> [testo](URL)
        testo = re.sub(r"\[(https?://[^\s\]]+)\s+([^\]]+)\]", r" [\2](\1)", testo)

        # 5b. Convertiamo i link "nudi" (es. https://...) in [LINK](https://...)
        # Evita i link già convertiti controllando che non ci sia '(' o '[' subito prima
        testo = re.sub(
            r"(?<![\(\[])(https?://[^\s,;\)\"\]]+)", r" [LINK](\1)", testo
        )

        # 5c. Convertiamo i link interni generici del Wiki
        testo = re.sub(
            r"\[\[(?!File:|Image:)([^|\]]+)\|([^\]]+)\]\]",
            rf" [\2]({base_url}\1)",
            testo,
        )
        testo = re.sub(
            r"\[\[(?!File:|Image:)([^\]]+)\]\]", rf" [\1]({base_url}\1)", testo
        )

        # 6. FORMATTAZIONE INLINE (Grassetto e Corsivo)
        testo = re.sub(r"'''(.*?)'''", r"**\1**", testo)
        testo = re.sub(r"''(.*?)''", r"*\1*", testo)

        # 7. FIX LISTE PUNTATE: Forza lo spazio dopo l'asterisco
        testo = re.sub(r"^\*(?!\*)(?:\s*)", "* ", testo, flags=re.MULTILINE)

        # 8. PULIZIA FINALE TAG HTML E SPAZI
        testo = testo.replace("<br>", "\n")
        testo = re.sub(r"<[^>]*>", "", testo)

        # Normalizza gli spazi bianchi ed elimina righe vuote eccessive
        testo = re.sub(r" {2,}", " ", testo)
        testo = re.sub(r"\n{3,}", "\n\n", testo)

        return testo.strip
    except Exception:
        # In caso di errore durante qualsiasi step, ritorna una riga vuota
        return ""


# Funzione per dividere la lista in chunk
def get_chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# Funzione modificata per gestire un chunk di segnali
def get_descriptions_for_chunk(signals_chunk: list[Signal]):
    titles_param = "|".join([sig.title for sig in signals_chunk])

    query_param = {
        "action": "query",
        "prop": "revisions",
        "titles": titles_param,
        "rvprop": "content",
        "format": "json",
    }

    res_testo = requests.get(ProjectPath.SIGID_API, params=query_param)
    data_testo = res_testo.json()
    
    pages = data_testo.get("query", {}).get("pages", {})

    result = []
    
    for page_id, page_data in pages.items():
        signal = Signal(page_id, page_data['title'])

        wikitext_grezzo = page_data["revisions"][0].get("*", "")

        try:
            wikitext_pulito = _wikitext2markdown(wikitext_grezzo)
            signal.description = wikitext_pulito
        except Exception:
            continue
        result.append(signal)
    return result




if __name__ == "__main__":
    # 1. Caricamento dell'indice
    with open(ProjectPath.INDEX_JSON, 'r', encoding='utf-8') as f:
        index = json.load(f)

    # 2. Inizializzazione della lista dei segnali
    signals = []
    signals_with_description = []

    for pageid, title in index.items():
        sig = Signal(pageid, title)
        sig.load_json()
        signals.append(sig)

    dimensione_chunk = 30
    
    # Suddividiamo i segnali in chunk
    chunks_list = list(get_chunks(signals, dimensione_chunk))

    # 3. Loop principale sui chunk con tqdm
    tqdm.write(f"Elaborazione di un chunk di {dimensione_chunk} segnali...")
    for chunk in tqdm(chunks_list):
    
        signals_chunk = None
        tentativi = 0
        attesa_base = 5  # secondi base per il backoff

        while signals_chunk is None:
            try:
                signals_chunk = get_descriptions_for_chunk(chunk)

            except Exception as e:
                tentativi += 1
                tempo_di_attesa = attesa_base * tentativi
                
                tqdm.write(f"⚠️ Errore! Tentativo {tentativi} fallito. Errore: {e}")
                tqdm.write(f"... Attendo {tempo_di_attesa} secondi prima di riprovare...")
                time.sleep(tempo_di_attesa)
                
                if tentativi > 5:
                    tqdm.write("❌ Troppi fallimenti consecutivi per questo chunk. Salto il chunk.")
                    break

        if signals_chunk is None:
            continue

        signals_with_description.extend(signals_chunk)
        
        # Grace period between chunks
        time.sleep(2)

    # Saving all jsons
    for signal in signals_with_description:
        signal.save_json()