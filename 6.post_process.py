import json
import difflib
import rapidfuzz

from tqdm import tqdm

from utils.constants import ProjectPath, Constants
from models.signal import Signal


def normalize_modulation(signal: Signal):
    post_modulations = []

    for mod_data in signal.modulation:
        modulation = mod_data['value']

        best_match = None
        best_ratio = 0.0

        for known in Constants.KNOWN_MODULATIONS:
            ratio = difflib.SequenceMatcher(None, modulation, known).ratio()
            if ratio > best_ratio:
                best_match = known
                best_ratio = ratio

        percentage = round(best_ratio * 100, 2)

        chosen_match = None

        if best_match and percentage >= 85:
            # Se la confidenza è alta (>85%) viene automaticamente convertito
            chosen_match = best_match
            print(f"🟦 [AUTO] {modulation} --> {best_match} ({percentage}%)")
        else:
            # Se la confidenza è bassa viene chiesto intervento manuale
            print("\n" + "="*50)
            if best_match:
                print(f"🟨 MODULATION: '{modulation}' not found")
                print(f"Suggestion: '{best_match}' - {percentage}% match")
            else:
                print(f"🟥 NO MATCH FOUND for: '{modulation}'")
            print("="*50)

            # Loop interativo
            while True:
                if best_match:
                    print("\n  [y] Accept the suggestion")
                print("  [s] Skip this modulation (do not include it)")
                print("  [valid modulation] Enter a valid modulation (e.g., AM, FM, SSB...)")

                scelta = input("Choice: ").strip()

                if scelta.lower() == 'y' and best_match:
                    chosen_match = best_match
                    break
                elif scelta.lower() == 's':
                    print(f"Skipped: {modulation}")
                    break
                elif scelta in Constants.KNOWN_MODULATIONS:
                    chosen_match = scelta
                    print(f"🟩 Manually assigned: {chosen_match}")
                    break
                else:
                    print(f"\n🟥 Error: '{scelta}' is not a valid option (does not exist in KNOWN_MODULATIONS).\n")

        if chosen_match:
            post_modulations.append(
                {
                    'value': chosen_match,
                    'description': Constants.KNOWN_MODULATIONS[chosen_match]
                }
            )

    signal.modulation = post_modulations
    signal.save()


def normalize_location(signal: Signal):
    post_location = []

    for loc_data in signal.location:
        location = loc_data['value']

        best_match = None

        best_match, score, _ = rapidfuzz.process.extractOne(
            location,
            Constants.KNOWN_LOCATIONS,
            scorer=rapidfuzz.fuzz.WRatio,
            processor=rapidfuzz.utils.default_process
        )

        percentage = round(score, 2)

        chosen_match = None

        if best_match and percentage >= 95:
            # Se la confidenza è alta (>85%) viene automaticamente convertito
            chosen_match = best_match
            print(f"🟦 [AUTO] {location} --> {best_match} ({percentage}%)")
        else:
            # Se la confidenza è bassa viene chiesto intervento manuale
            print("\n" + "="*50)
            if best_match:
                print(f"🟨 LOCATION: '{location}' not found")
                print(f"Suggestion: '{best_match}' - {percentage}% match")
            else:
                print(f"🟥 NO MATCH FOUND for: '{location}'")
            print("="*50)

            # Loop interativo
            while True:
                if best_match:
                    print("\n\t[y] Accept the suggestion")
                print("\t[s] Skip this location (do not include it)")
                print("\t[valid location] Enter a valid location")

                choice = input("Choice: ").strip()

                if choice.lower() == 'y' and best_match:
                    chosen_match = best_match
                    break
                elif choice.lower() == 's':
                    print(f"Skipped: {location}")
                    break
                elif choice in Constants.KNOWN_LOCATIONS:
                    chosen_match = choice
                    print(f"🟩 Manually assigned: {chosen_match}")
                    break
                else:
                    print(f"\n🟥 Error: '{choice}' is not a valid option (does not exist in KNOWN_LOCATIONS).\n")

        if chosen_match:
            post_location.append(
                {
                    'value': chosen_match,
                    'description': ''
                }
            )

    signal.location = post_location
    signal.save()


if __name__ == "__main__":
    """
    Postprocess svolge compiti multipli:
    - Normalizza la modulazione: controlla nel dizionario di modulazioni riconosciute e
      se non trova un match ne suggerisce uno. E' possibile applicare un valore custom
      purchè sia presente nelle modulazioni valide.
      L'algoritmo di match è Ratcliff/Obershelp pattern recognition:
        È molto sensibile all'ordine delle parole e ai piccoli cambi di struttura
    - Normalizza la location: come sopra ma per i luoghi validi. La lista è direttamente estrapolata
      da pycountry.
      L'algoritmo di match è Weighted Ratio:
        Gestisce bene stringhe di lunghezze diverse, l'inversione dell'ordine delle parole e le parole mancanti.
    - Controllo di integrità: il segnale controlla che i suoi attributi siano validi e cerca possibili
      pattern di malformazione dovuti a typo, parsing errati, etc 
    """
    with open(ProjectPath.INDEX_JSON, 'r', encoding='utf-8') as f:
        index = json.load(f)
    
    for pageid, title in tqdm(index.items()):
        signal = Signal(pageid, title)
        signal.load()
        normalize_modulation(signal)
        normalize_location(signal)
        signal.check_integrity()
