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
    # --- FASE 1: Query Semantica per i Metadati Tecnici ---
    query_string = f"[[{signal.title}]]|" + "|".join(f"?{f}" for f in query_fields)
    params_semantici = {"action": "ask", "query": query_string, "format": "json"}

    try:
        response = requests.get(ProjectPath.SIGID_API, params=params_semantici, timeout=10)
        response.raise_for_status()

        data = response.json()
        
        # Gestione sicura degli errori ritornati dall'API (Evita il KeyError)
        if 'error' in data:
            error_msg = data['error'].get('query', data['error'])
            raise ValueError(f"L'API ha restituito un errore per '{signal.title}': {error_msg}")

        # Controllo sicuro della presenza della chiave 'query'
        if 'query' not in data or 'meta' not in data['query']:
            raise ValueError(f"Risposta API malformata per il segnale: {signal.title}")

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

            return signal

        else:
            raise ValueError(f"Segnale non trovato. Il nome del segnale ({signal.title}) è corretto?")

    except requests.exceptions.HTTPError as e:
        raise RuntimeError(f"Errore HTTP: {e}")

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Errore rete/API: {e}")


if __name__ == "__main__":
    with open(ProjectPath.INDEX_JSON, 'r', encoding='utf-8') as f:
        index = json.load(f)
    
    for pageid, title in tqdm(index.items(), desc="Elaborazione segnali"):
        tqdm.write(f"In corso: {title}")
        
        # Tentativi di recupero dati con gestione dell'errore
        signal_json = None
        tentativi = 0
        attesa_base = 5  # secondi da aspettare se veniamo bloccati
        
        while signal_json is None:
            try:
                signal_json = get_signal_data(Signal(pageid, title))

            except Exception as e: 
                # Nota: qui dovresti intercettare l'eccezione specifica delle richieste (es. requests.exceptions.HTTPError)
                # Se l'errore è un 429:
                tentativi += 1
                tempo_di_attesa = attesa_base * tentativi # Più fallisce, più aspetta (Exponential Backoff)
                tqdm.write(f"⚠️ Bloccato da 429. Tentativo {tentativi}. Aspetto {tempo_di_attesa}s...")
                time.sleep(tempo_di_attesa)
                
                if tentativi > 5: # Evita cicli infiniti se il ban è permanente
                    tqdm.write("❌ Troppi fallimenti. Salto questo segnale.")
                    break

        if signal_json is None:
            continue # Salta il salvataggio se non abbiamo dati
        
        signal_json.save_json()
        time.sleep(2)
