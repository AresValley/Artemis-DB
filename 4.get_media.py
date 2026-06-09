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
        
        if "imageinfo" in page:
            results_map[original_filename] = page["imageinfo"][0]["url"]
        else:
            results_map[original_filename] = None

    return results_map



def get_chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]



if __name__ == "__main__":
    # 1. Load the index
    with open(ProjectPath.INDEX_JSON, 'r', encoding='utf-8') as f:
        index = json.load(f)

    # 2. Initialize the signals list
    all_media_filename = []

    for pageid, title in index.items():
        sig = Signal(pageid, title)
        sig.load_json()
        if sig.spectrum['filename']:
            all_media_filename.append(sig.spectrum['filename'])
        if sig.audio['filename']:
            all_media_filename.append(sig.audio['filename'])

    session = requests.session()
    chunk_size = 30
    
    # Split signals into chunks
    chunks_list = list(get_chunks(all_media_filename, chunk_size))
    result = {}
    # 3. Main loop over chunks with tqdm
    tqdm.write(f"Processing a chunk of {chunk_size} media...")
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
                
                tqdm.write(f"⚠️ Error! Attempt {attempts} failed. Error: {e}")
                tqdm.write(f"... Waiting {wait_time} seconds before retrying...")
                time.sleep(wait_time)
                
                if attempts > 5:
                    raise ValueError("❌ Too many consecutive failures for this chunk. Halt.")

        if media_chunk is None:
            continue

        result.update(media_chunk)
        # Grace period between chunks
        time.sleep(2)

    # Saving all jsons
    for pageid, title in index.items():
        sig = Signal(pageid, title)
        sig.load_json()
        if sig.spectrum['filename']:
            sig.spectrum['url'] = result[sig.spectrum['filename']]
        if sig.audio['filename']:
            sig.audio['url'] = result[sig.audio['filename']]
        sig.save_json()
