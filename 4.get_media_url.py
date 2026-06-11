import requests
import time
import json
from tqdm import tqdm

from utils.constants import ProjectPath
from models.signal import Signal


def get_media_urls(session, filenames):
    titles = "|".join([f"File:{f}" for f in filenames])
    
    params = {
        "action": "query",
        "titles": titles,
        "prop": "imageinfo",
        "iiprop": "url",
        "format": "json"
    }

    response = session.get(ProjectPath.SIGID_API, params=params, timeout=15)
    response.raise_for_status()
    data = response.json()

    results_map = {}

    for page in data["query"]["pages"].values():
        original_filename = page["title"].replace("File:", "", 1)
        # tutta la stringa è convertita in minuscolo e gli spazi sono sostituiti da underscoe
        # questo per evitare problemi di come mediawiki dichiara i nomi dei file
        # Es. (prima lettera maiuscola, spazi vuoti multipli, etc)
        original_filename = "_".join(original_filename.lower().split())
        
        if "imageinfo" in page:
            results_map[original_filename] = page["imageinfo"][0]["url"]
        else:
            results_map[original_filename] = None

    return results_map


def get_chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]



if __name__ == "__main__":
    with open(ProjectPath.INDEX_JSON, 'r', encoding='utf-8') as f:
        index = json.load(f)

    all_media_filename = []

    for pageid, title in index.items():
        sig = Signal(pageid, title)
        sig.load()
        if sig.spectrum['filename']:
            all_media_filename.append(sig.spectrum['filename'])
        if sig.audio['filename']:
            all_media_filename.append(sig.audio['filename'])

    session = requests.session()
    chunk_size = 30
    
    chunks_list = list(get_chunks(all_media_filename, chunk_size))
    result = {}

    tqdm.write(f"🟦 Processing a chunk of {chunk_size} media...")
    for chunk in tqdm(chunks_list):
    
        media_chunk = None
        attempts = 0
        base_wait = 5  # base seconds for backoff

        while media_chunk is None:
            try:
                media_chunk = get_media_urls(session, chunk)

            except Exception as e:
                attempts += 1
                wait_time = base_wait * attempts
                
                tqdm.write(f"🟨 Error! Attempt {attempts} failed. Error: {e}")
                tqdm.write(f"🟦 Waiting {wait_time} seconds before retrying...")
                time.sleep(wait_time)

                if attempts > 5:
                    raise ValueError("🟥 Too many consecutive failures for this chunk. Halt.")

        if media_chunk is None:
            continue

        result.update(media_chunk)
        # Grace period
        time.sleep(2)

    # Saving all jsons
    for pageid, title in index.items():
        sig = Signal(pageid, title)
        sig.load()

        if sig.spectrum['filename']:
            # Come spiegato sopra si cerca il nome del file normalizzato in modo da escludere
            # mismatch dovute alla formattazione mediawiki
            normalized_filename = "_".join(sig.spectrum['filename'].lower().split())
            sig.spectrum['url'] = result[normalized_filename]
            if sig.spectrum['url'] is None:
                print(f'WARNING:{sig.title} {sig.pageid}')

        if sig.audio['filename']:
            # idem
            normalized_filename = "_".join(sig.audio['filename'].lower().split())
            sig.audio['url'] = result[normalized_filename]
            if sig.audio['url'] is None:
                print(f'WARNING:{sig.title} {sig.pageid}')

        sig.save()
