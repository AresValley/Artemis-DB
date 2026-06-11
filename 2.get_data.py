import requests
import json
import time

from tqdm import tqdm

from utils.constants import Constants, ProjectPath
from utils.generic_utils import format_text, format_acf
from models.signal import Signal


QUERY_FIELDS = [
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
    "Title"
]


def get_signal_data(session, signal: Signal):
    """
    La funzione interroga le API di mediawiki e ne estrae i dati per ogni segnali.
    ACF, Mode e Modulation vengono pulite perchè a quanto pare, anche se gli elementi
    vengono separati con  la virgola, non vengono parsate come liste dal API

    TODO: sarebbe ideale velocizzare dividendo la lista segnali in chunk ma l'azione
    ask delle API mi pare non lo permetta. Non ne sono sicuro...da investigare...
    forse askargs (?). Da evitare approcci paralleli con threads o async per non stressare
    il firewall o fail2ban del server (visto che già così, con l'approccio seriale, il server
    da dei tempi di ban, corti ma li da).
    """
    query_string = f"[[{signal.title}]]|" + "|".join(f"?{f}" for f in QUERY_FIELDS)
    params = {"action": "ask", "query": query_string, "format": "json"}

    try:
        response = session.get(ProjectPath.SIGID_API, params=params, timeout=10)
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

            signal.spectrum['filename'] = signal_data['Picture'][0] if signal_data['Picture'] else None
            signal.audio['filename'] = signal_data['Signal file'][0] if signal_data['Signal file'] else None

            for cat in signal_data['Additional categories']:
                if cat in Constants.CATEGORIES:
                    signal.category.append(cat)

            for frequency in signal_data['Frequencies']:
                signal.frequency.append({"value": frequency, "description": ""})

            for bandwidth in signal_data['Bandwidth']:
                signal.bandwidth.append({"value": bandwidth, "description": ""})

            for acf in signal_data['ACF']:
                acf = format_acf(acf)
                for i in acf:
                    signal.acf.append({"value": i[1], "description": i[0]})

            for modulation in signal_data['Modulation']:
                modulation = format_text(modulation)
                for i in modulation:
                    signal.modulation.append({"value": i, "description": ""})

            for mode in signal_data['Mode']:
                mode = format_text(mode)
                for i in mode:
                    signal.mode.append({"value": i, "description": ""})

            for location in signal_data['Location']:
                location = format_text(location)
                for i in location:
                    signal.location.append({"value": i, "description": ""})
            
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
    
    session = requests.session()
    
    for pageid, title in tqdm(index.items()):
        tqdm.write(f"🟦 Downloading: {title}")

        signal_json = None
        attempts = 0
        base_wait = 5
        
        while signal_json is None:
            try:
                signal_json = get_signal_data(session, Signal(pageid, title))

            except Exception as e: 
                attempts += 1
                wait_time = base_wait * attempts

                tqdm.write(f"🟨 Error! Attempt {attempts} failed. Error: {e}")
                tqdm.write(f"🟦 Waiting {wait_time} seconds before retrying...")
                time.sleep(wait_time)
                
                if attempts > 5:
                    raise ValueError("🟥 Too many consecutive failures for this chunk. Halt.")

        if signal_json is None:
            continue

        signal_json.save()
        time.sleep(2)
