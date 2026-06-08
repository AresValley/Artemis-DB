import urllib.request
import urllib.parse
import json
import time
import os

from utils.constants import ProjectPath


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


def migrate_index_to_pageids():
    """
    Legge il file index.json esistente, interroga l'API di MediaWiki per ottenere
    i pageid mancanti risolvendo i redirect, inserisce i pageid nel JSON e
    unifica automaticamente i record duplicati mantenendo il 'dir' più vecchio.
    """
    if not os.path.exists(ProjectPath.INDEX_JSON):
        print(f"File {ProjectPath.INDEX_JSON} non trovato.")
        return

    with open(ProjectPath.INDEX_JSON, 'r', encoding='utf-8') as f:
        index_data = json.load(f)

    # Estrae i titoli dei segnali che non possiedono ancora il campo 'pageid'
    titles_to_query = [info["name"] for info in index_data.values() if "pageid" not in info]
    
    if not titles_to_query:
        print("Tutti i record nel file possiedono già un pageid.")
        return

    print(f"Rilevati {len(titles_to_query)} elementi senza pageid. Avvio recupero dall'API...")
    
    chunk_size = 50
    title_to_pid = {}
    redirect_map = {}

    # Interroga l'API a blocchi di 50 elementi (limite di MediaWiki)
    for i in range(0, len(titles_to_query), chunk_size):
        chunk = titles_to_query[i : i + chunk_size]
        params = {
            "action": "query",
            "titles": "|".join(chunk),
            "redirects": "1"  # Permette di seguire i redirect storici
        }
        try:
            data = _fetch_json(params)
            query_res = data.get("query", {})
            
            # Mappa le risoluzioni dei redirect (Vecchio Titolo -> Nuovo Titolo)
            if "redirects" in query_res:
                for redir in query_res["redirects"]:
                    redirect_map[redir["from"]] = redir["to"]
            
            # Mappa i titoli finali ai rispettivi pageid
            for pid, pinfo in query_res.get("pages", {}).items():
                if "pageid" in pinfo:
                    title_to_pid[pinfo["title"]] = pinfo["pageid"]
        except Exception as e:
            print(f"⚠️ Errore durante l'interrogazione del blocco: {e}")
        
        time.sleep(0.5)

    # 1. Associa i pageid trovati ai record correnti e aggiorna i nomi se erano dei redirect
    for url, info in index_data.items():
        if "pageid" not in info:
            title = info["name"]
            # Segue l'eventuale catena di redirect per trovare il titolo finale effettivo
            while title in redirect_map:
                title = redirect_map[title]
            
            if title in title_to_pid:
                info["pageid"] = title_to_pid[title]
                info["name"] = title

    # 2. Ricostruisce l'indice rimuovendo i doppioni e normalizzando gli URL
    cleaned_index = {}
    
    # Mantiene intatti i record per cui non è stato possibile recuperare il pageid (es. pagine eliminate)
    for url, info in index_data.items():
        if "pageid" not in info:
            cleaned_index[url] = info

    # Raggruppa i record validi in base al loro pageid univoco
    pid_groups = {}
    for url, info in index_data.items():
        if "pageid" in info:
            pid = info["pageid"]
            if pid not in pid_groups:
                pid_groups[pid] = []
            pid_groups[pid].append(info)

    # Risolve i duplicati inserendo una sola voce pulita per ogni pageid
    for pid, infos in pid_groups.items():
        # Sceglie il record con il valore di 'dir' più basso (mantiene la cartella storica originaria)
        best_info = min(infos, key=lambda x: x["dir"])
        
        # Rigenera l'URL corretto standardizzato basandosi sul nome ufficiale aggiornato
        encoded_title = urllib.parse.quote(best_info["name"].replace(" ", "_"), safe=":/")
        correct_url = f"{ProjectPath.SIGID_DOMAIN}/wiki/{encoded_title}"
        
        # Salva nel nuovo indice unificato
        cleaned_index[correct_url] = best_info

    # 3. Scrive l'indice aggiornato e bonificato su file
    with open(ProjectPath.INDEX_JSON, 'w', encoding='utf-8') as f:
        json.dump(cleaned_index, f, ensure_ascii=False, indent=4)
    
    print(f"Procedura completata! Il file {ProjectPath.INDEX_JSON} è stato aggiornato con i pageid e ripulito dai doppioni.")


if __name__ == "__main__":
    migrate_index_to_pageids()