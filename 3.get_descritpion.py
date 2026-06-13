import re
import requests
import json
import time
import urllib.parse

import wikitextparser as wtp
from tqdm import tqdm

from utils.constants import ProjectPath
from models.signal import Signal


def _wikitext2markdown(wikitext):
    """
    Rielaborazione contenuto mediawiki in markdown con conversione tabelle robusta
    """
    base_url = "https://www.sigidwiki.com/wiki/"

    # 1. Rimuove i menu/navigazione iniziale in HTML (span/div)
    wikitext = re.sub(
        r"^\s*<(span|div)[^>]*>[\s\S]*?<\/\1>", "", wikitext, flags=re.IGNORECASE
    )
    
    # 1b. Rimuove i tag di citazione <ref> lasciando il contenuto interno
    wikitext = re.sub(r"</?ref[^>]*>", "", wikitext, flags=re.IGNORECASE)

    # 2. Parsing del Wikitext iniziale per rimuovere i template
    parsed = wtp.parse(wikitext)
    for template in parsed.templates:
        template.string = ""

    # 3. ISOLAMENTO DELL'INTRODUZIONE
    clean_parsed = wtp.parse(parsed.string)
    if clean_parsed.sections:
        testo = clean_parsed.sections[0].contents
    else:
        testo = clean_parsed.string

    # 4. CONVERSIONE DELLE TABELLE DIRECTLY ON STRING
    # Usiamo wtp.parse sul blocco di testo isolato per trovare le tabelle stabili
    testo_parsed = wtp.parse(testo)
    for table in testo_parsed.tables:
        try:
            raw_data = table.data()
            if not raw_data:
                testo = testo.replace(table.string, "")
                continue
                
            md_table = []
            rows = []
            for r in raw_data:
                # Sostituiamo i \n con gli spazi e forziamo la stringa
                cleaned_row = [str(cell).replace('\n', ' ').strip() for cell in r]
                if any(cleaned_row):
                    rows.append(cleaned_row)
            
            if len(rows) > 0:
                header = rows[0]
                md_table.append("| " + " | ".join(header) + " |")
                md_table.append("| " + " | ".join(["---" for _ in header]) + " |")
                
                for row in rows[1:]:
                    while len(row) < len(header):
                        row.append("")
                    md_table.append("| " + " | ".join(row[:len(header)]) + " |")
                
                formatted_md_table = "\n\n" + "\n".join(md_table) + "\n\n"
                # Sostituiamo brutalmente il vecchio blocco tabella text con il nuovo MD
                testo = testo.replace(table.string, formatted_md_table)
            else:
                testo = testo.replace(table.string, "")
        except Exception:
            testo = testo.replace(table.string, "")

    # 5. CONVERSIONE E PULIZIA LINK
    # 5a. Link con testo esplicito URL -> [testo](URL)
    testo = re.sub(r"\[(https?://[^\s\]]+)\s+([^\]]+)\]", r" [\2](\1)", testo)

    # 5b. Link "nudi" (es. https://...) in [LINK](https://...)
    testo = re.sub(r"(?<![\(\[])(https?://[^\s,;\)\"\]]+)", r" [LINK](\1)", testo)

    # 5c. Link interni del Wiki
    parsed_testo = wtp.parse(testo)
    for link in parsed_testo.wikilinks:
        target = link.title.strip()
        if target.lower().startswith(('file:', 'image:')):
            link.string = ""
            continue
        text = link.text.strip() if link.text else target
        safe_target = urllib.parse.quote(target.replace(' ', '_'))
        link.string = f" [{text}]({base_url}{safe_target})"
    testo = parsed_testo.string

    # 6. FORMATTAZIONE (Grassetto e Corsivo)
    testo = re.sub(r"'''(.*?)'''", r"**\1**", testo)
    testo = re.sub(r"''(.*?)''", r"*\1*", testo)

    # 7. FIX LISTE PUNTATE
    testo = re.sub(r"^\*(?!\*)(?:\s*)", "- ", testo, flags=re.MULTILINE)

    # 8. PULIZIA FINALE TAG HTML E SPAZI
    testo = testo.replace("<br>", "\n").replace("<br />", "\n").replace("<br/>", "\n")
    testo = re.sub(r"</?(span|div|p|b|i|strong|em|code)[^>]*>", "", testo, flags=re.IGNORECASE)

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
