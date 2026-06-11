import urllib.request
import urllib.parse
import json
import time
import os

from utils.constants import Constants, ProjectPath
from models.signal import Signal


def _fetch_json(params: dict) -> dict:
    params["format"] = "json"
    query_string = urllib.parse.urlencode(params)
    url = f"{ProjectPath.SIGID_API}?{query_string}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "SigidWikiScraper/1.0"}
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))


def get_identified_signal_urls() -> list[Signal]:
    """
    Interroga mediawiki tramite API con l'azione query. Essendo il limite interno di max 500
    segnali alla volta la funzione continua lo scraping finchè non trova più il segnale di
    continuazione nel chunk 
    """
    print("Connect to sigidwiki.com API...")
    all_signals = []
    params = {
        "action":    "query",
        "list":      "categorymembers",
        "cmtitle":   "Category:Signal",
        "cmnamespace": "0",               # only article
        "cmlimit":   "500",
    }

    page_count = 0
    while True:
        data = _fetch_json(params)
        pages = data.get("query", {}).get("categorymembers", [])

        for page in pages:
            if page["title"] not in Constants.SIG_EXCLUSION:
                signal = Signal(page["pageid"], page["title"])
                all_signals.append(signal)

        page_count += len(pages)

        if "query-continue" in data:
            print(f"  ... found {page_count} signals yet ...")
            continuation = data["query-continue"]["categorymembers"]
            params.update(continuation)
        elif "continue" in data:
            print(f"  ... found {page_count} signals yet ...")
            params.update(data["continue"])
        else:
            print(f"  ... found {page_count} total signals.")
            break

        time.sleep(1.0)

    return all_signals


def update_index_json(all_signals: list[Signal]):
    """
    Questa funzione aggiorna l'indice index.json dove:
    - I nuovi segnali vengono aggiunti tramitet l'identificatore unico pageid
    - I segnali esistenti vengono aggiornati (se il titolo dovesse cambiare)
    """
    if os.path.exists(ProjectPath.INDEX_JSON):
        with open(ProjectPath.INDEX_JSON, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
    else:
        index_data = {}

    new_entries_record = []

    for signal in all_signals:
        page_id_str = str(signal.pageid)
        
        if page_id_str not in index_data:
            new_entries_record.append(signal.title)
        
        index_data[page_id_str] = signal.title

    with open(ProjectPath.INDEX_JSON, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, ensure_ascii=False, indent=4)

    print(f"🟩 Completed. Added {len(new_entries_record)} new signals {ProjectPath.INDEX_JSON}.")
    print("="*50)
    print("SUMMARY:\n")
    print(f"SEGNALI TOTALI\t{len(index_data)}\n")

    if new_entries_record:
        print("NEW SIGNALS FOUND:")
        for record in new_entries_record:
            print(f"- {record}")
    else:
        print("No new signals.")

    print("="*50)

if __name__ == "__main__":
    signals_scraped = get_identified_signal_urls()
    update_index_json(signals_scraped)
