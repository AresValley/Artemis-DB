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
    Recupera tutte le pagine nella Category:Signal tramite
    categorymembers, con paginazione automatica.
    """
    print("Connessione all'API di sigidwiki.com...")
    all_signals = []
    params = {
        "action":     "query",
        "list":      "categorymembers",
        "cmtitle":   "Category:Signal",   # categoria dei segnali identificati
        "cmnamespace": "0",               # solo articoli
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

        # Paginazione: legge dinamicamente qualsiasi chiave di continuazione
        if "query-continue" in data:
            print(f"  ... recuperati {page_count} segnali finora ...")
            continuation = data["query-continue"]["categorymembers"]
            params.update(continuation)
        elif "continue" in data:
            print(f"  ... recuperati {page_count} segnali finora ...")
            params.update(data["continue"])
        else:
            print(f"  ... recuperati {page_count} segnali in totale.")
            break

        time.sleep(1.0)

    return all_signals


def update_index_json(all_signals: list[Signal]):
    """
    Carica l'index.json se esiste, altrimenti lo crea.
    Aggiorna il file inserendo i nuovi URL.
    """
    # 1. Carica l'indice esistente o ne inizializza uno vuoto
    if os.path.exists(ProjectPath.INDEX_JSON):
        with open(ProjectPath.INDEX_JSON, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
    else:
        index_data = {}

    new_entries_record = []

    # 3. Itera sui segnali appena scaricati
    for signal in all_signals:
        page_id_str = str(signal.pageid)
        
        # Se l'URL non è presente nell'indice, viene aggiunto come nuova voce
        if page_id_str not in index_data:
            new_entries_record.append(signal.title)
        
        # Aggiorna o inserisce il valore (usando la stringa come chiave per coerenza con il JSON)
        index_data[page_id_str] = signal.title

    # 4. Salva l'indice aggiornato
    with open(ProjectPath.INDEX_JSON, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, ensure_ascii=False, indent=4)

    print(f"Operazione completata. Aggiunti {len(new_entries_record)} nuovi segnali nel file {ProjectPath.INDEX_JSON}.")
    if new_entries_record:
        print("Nuovi segnali trovati:")
        for record in new_entries_record:
            print(f" - {record}")
    else:
        print("Nessun nuovo segnale da aggiungere.")


if __name__ == "__main__":
    signals_scraped = get_identified_signal_urls()
    update_index_json(signals_scraped)
