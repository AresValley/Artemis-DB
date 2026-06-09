import requests
import json
import time

from tqdm import tqdm

from utils.constants import Constants, ProjectPath
from models.signal import Signal


query_fields = [
    "Additional_categories",
    "ACF",
    "Bandwidth",
    "Frequencies",
    "Location",
    "Mode",
    "Modulation",
    "Picture",
    "Signal_description",
    "Signal_file",
    "Title",
]

def get_media_url(filename):
    params = {
        "action": "query",
        "titles": f"File:{filename}",
        "prop": "imageinfo",
        "iiprop": "url",
        "format": "json"
    }

    response = requests.get(ProjectPath.SIGID_API, params=params)
    data = response.json()

    page = next(iter(data["query"]["pages"].values()))
    image_url = page["imageinfo"][0]["url"]

    return image_url


def get_signal_data(signal: Signal):
    query_string = f"[[{signal.title}]]|" + "|".join(f"?{f}" for f in query_fields)
    params_semantici = {"action": "ask", "query": query_string, "format": "json"}

    try:
        response = requests.get(ProjectPath.SIGID_API, params=params_semantici, timeout=10)
        response.raise_for_status()

        data = response.json()
        
        if 'error' in data:
            error_msg = data['error'].get('query', data['error'])
            raise ValueError(f"API returned an error for signal '{signal.title}': {error_msg}")

        if 'query' not in data or 'meta' not in data['query']:
            raise ValueError(f"Malformed API reply for signal: {signal.title}")

        signal_found = True if data['query']['meta'].get('count', 0) == 1 else False

        if signal_found:
            signal_data = data['query']['results'][signal.title]['printouts']

            signal.spectrum_filename = signal_data['Picture']
            signal.audio_filename = signal_data['Signal file']

            for cat in signal_data['Additional categories']:
                if cat in Constants.CATEGORIES:
                    signal.category.append(cat)

            for frequency in signal_data['Frequencies']:
                signal.frequency.append({"value": frequency, "description": ""})

            for bandwidth in signal_data['Bandwidth']:
                signal.bandwidth.append({"value": bandwidth, "description": ""})

            for acf in signal_data['ACF']:
                signal.acf.append({"value": acf, "description": ""})

            for modulation in signal_data['Modulation']:
                signal.modulation.append({"value": modulation, "description": ""})

            for mode in signal_data['Mode']:
                signal.mode.append({"value": mode, "description": ""})

            for location in signal_data['Location']:
                signal.location.append({"value": location, "description": ""})
            
            signal.short_description = signal_data['Signal description'][0] if signal_data['Signal description'] else None

            return signal

        else:
            raise ValueError(f"Segnal not found. Are you sure about signal name ({signal.title}) ?")

    except requests.exceptions.HTTPError as e:
        raise RuntimeError(f"Error HTTP: {e}")

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error network/API: {e}")


if __name__ == "__main__":
    with open(ProjectPath.INDEX_JSON, 'r', encoding='utf-8') as f:
        index = json.load(f)
    
    for pageid, title in tqdm(index.items()):
        tqdm.write(f"Downloading: {title}")

        signal_json = None
        attempts = 0
        base_wait = 5
        
        while signal_json is None:
            try:
                signal_json = get_signal_data(Signal(pageid, title))

            except Exception as e: 
                attempts += 1
                wait_time = base_wait * attempts

                tqdm.write(f"⚠️ Error! Attempt {attempts} failed. Error: {e}")
                tqdm.write(f"... Waiting {wait_time} seconds before retrying...")
                time.sleep(wait_time)
                
                if attempts > 5:
                    raise ValueError("❌ Too many consecutive failures for this chunk. Halt.")

        if signal_json is None:
            continue
        
        signal_json.save_json()
        time.sleep(2)
