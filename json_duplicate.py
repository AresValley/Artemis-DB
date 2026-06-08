import json
import os
import urllib.parse
from difflib import SequenceMatcher

INDEX_FILE = "index.json"

def cerca_nomi_simili(filepath: str, soglia: float = 0.85):
    if not os.path.exists(filepath):
        print(f"Errore: Il file {filepath} non esiste.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print(f"Errore: Il file {filepath} non è un JSON valido.")
            return

    # Estraiamo tutti i nomi e i relativi dettagli
    # Creiamo una lista di tuple: (nome_pulito_per_confronto, nome_originale, url, dir)
    segnali = []
    for url, info in data.items():
        nome_originale = info.get("name", "")
        # Pulizia base per il confronto: tutto minuscolo e senza spazi extra
        nome_pulito = nome_originale.lower().strip()
        segnali.append((nome_pulito, nome_originale, url, info.get("dir")))

    print(f"=== CONTROLLO NOMI SIMILI (Soglia somiglianza: {soglia*100}%) ===")
    print(f"Confronto di {len(segnali)} segnali in corso... Potrebbe richiedere qualche secondo.")
    
    simili_trovati = False
    coppie_esaminate = set()

    # Confronto incrociato (O(N^2), accettabile per qualche migliaio di voci)
    for i in range(len(segnali)):
        for j in range(i + 1, len(segnali)):
            nome_p1, nome_orig1, url1, dir1 = segnali[i]
            nome_p2, nome_orig2, url2, dir2 = segnali[j]

            # Se i nomi puliti sono identici ma hanno URL diversi (es. "Ghadir" vs "ghadir")
            if nome_p1 == nome_p2:
                simili_trovati = True
                print(f"\n⚠️ Nomi identici (case-insensitive) assegnati a cartelle diverse:")
                print(f"   - Dir [{dir1}]: '{nome_orig1}' -> {url1}")
                print(f"   - Dir [{dir2}]: '{nome_orig2}' -> {url2}")
                continue

            # Altrimenti calcoliamo la somiglianza testuale complessiva
            # Usiamo un controllo rapido sulla lunghezza per saltare confronti inutili
            if abs(len(nome_p1) - len(nome_p2)) > 5: 
                continue

            ratio = SequenceMatcher(None, nome_p1, nome_p2).ratio()
            if ratio >= soglia:
                simili_trovati = True
                print(f"\n⚠️ Elevata somiglianza rilevata ({round(ratio*100, 1)}%):")
                print(f"   - Dir [{dir1}]: '{nome_orig1}'")
                print(f"   - Dir [{dir2}]: '{nome_orig2}'")

    if not simili_trovati:
        print("✅ Nessun segnale con nome simile o ambiguo rilevato.")


if __name__ == "__main__":
    # Esegui il controllo dei nomi simili sul tuo index.json
    # Puoi abbassare la soglia (es. 0.75) se vuoi una ricerca più "aggressiva"
    cerca_nomi_simili(INDEX_FILE, soglia=0.95)