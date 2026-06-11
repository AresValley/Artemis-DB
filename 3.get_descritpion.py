import re
import requests
import json
import time

import wikitextparser as wtp
from tqdm import tqdm

from utils.constants import ProjectPath
from models.signal import Signal


def _wikitext2markdown(wikitext):
    """
    Rielaborazione contenuto mediawiki in markdown
    La descrizione esatta delle varie sezioni è commentata punto per punto
    """
    base_url = "https://www.sigidwiki.com/wiki/"

    # 1. Rimuove i menu/navigazione iniziale in HTML (span/div)
    wikitext = re.sub(
        r"^\s*<(span|div)[^>]*>[\s\S]*?<\/\1>", "", wikitext, flags=re.IGNORECASE
    )

    # 2. Parsing del Wikitext
    parsed = wtp.parse(wikitext)

    # 3. Rimuove TUTTI i template ({{Cell}}, {{Signal ...}})
    for template in parsed.templates:
        del template[:]

    # 4. ISOLAMENTO DELL'INTRODUZIONE
    # parsed.sections[0] contiene sempre il testo prima del primo titolo (==)
    if parsed.sections:
        testo = parsed.sections[0].contents
    else:
        testo = parsed.string

    # 5. CONVERSIONE E PULIZIA LINK
    # 5a. Convertiamo i link con testo esplicito URL -> [testo](URL)
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

    # 6. FORMATTAZIONE (Grassetto e Corsivo)
    testo = re.sub(r"'''(.*?)'''", r"**\1**", testo)
    testo = re.sub(r"''(.*?)''", r"*\1*", testo)

    # 7. FIX LISTE PUNTATE
    testo = re.sub(r"^\*(?!\*)(?:\s*)", "* ", testo, flags=re.MULTILINE)

    # 8. PULIZIA FINALE TAG HTML E SPAZI
    testo = testo.replace("<br>", "\n")
    testo = re.sub(r"<[^>]*>", "", testo)

    # 9. Normalizza gli spazi bianchi ed elimina righe vuote eccessive
    testo = re.sub(r" {2,}", " ", testo)
    testo = re.sub(r"\n{3,}", "\n\n", testo)

    return testo.strip()


def get_chunks(lst, n):
    """
    Divisione lista in subliste di n elementi in maniera iterativa
    """
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def get_descriptions_for_chunk(session, signals_chunk: list[Signal]):
    """
    Funzione che recupera la descrizione (non la short description) e la converte in markdown
    Per ora viene solo elaborato il contenuto della prima sezione della pagina e viene escluso il resto
    """
    param = "|".join([sig.title for sig in signals_chunk])

    query_param = {
        "action": "query",
        "prop": "revisions",
        "titles": param,
        "rvprop": "content",
        "format": "json",
    }

    response = session.get(ProjectPath.SIGID_API, params=query_param)
    data = response.json()

    pages = data.get("query", {}).get("pages", {})

    result = []

    for page_id, page_data in pages.items():
        signal = Signal(page_id, page_data['title'])
        signal.load()

        wikitext_raw = page_data["revisions"][0].get("*", "")

        try:
            wikitext_clean = _wikitext2markdown(wikitext_raw)
            signal.description = wikitext_clean
        except Exception:
            signal.description = ''
        result.append(signal)
    return result


if __name__ == "__main__":
    with open(ProjectPath.INDEX_JSON, 'r', encoding='utf-8') as f:
        index = json.load(f)

    signals = []
    signals_with_description = []

    for pageid, title in index.items():
        sig = Signal(pageid, title)
        sig.load()
        signals.append(sig)

    session = requests.session()
    chunk_size = 30

    chunks_list = list(get_chunks(signals, chunk_size))

    tqdm.write(f"🟦 Processing a chunk of {chunk_size} signals...")
    for chunk in tqdm(chunks_list):

        signals_chunk = None
        attempts = 0
        base_wait = 5

        while signals_chunk is None:
            try:
                signals_chunk = get_descriptions_for_chunk(session, chunk)

            except Exception as e:
                attempts += 1
                wait_time = base_wait * attempts

                tqdm.write(f"🟨 Error! Attempt {attempts} failed. Error: {e}")
                tqdm.write(f"🟦 Waiting {wait_time} seconds before retrying...")
                time.sleep(wait_time)

                if attempts > 5:
                    raise ValueError("🟥 Too many consecutive failures for this chunk. Halt.")

        if signals_chunk is None:
            continue

        signals_with_description.extend(signals_chunk)
        # Grace period
        time.sleep(2)

    # Saving all jsons
    for signal in signals_with_description:
        if signal.description == '':
            print(f'🟨 CHECK: no description for {signal.pageid} {signal.title[:20]} ({signal.url})')
        signal.save()
