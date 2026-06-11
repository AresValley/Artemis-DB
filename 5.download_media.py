import json
import os

from tqdm import tqdm

from utils.constants import ProjectPath
from utils.media_utils import download_spectrum, download_audio
from models.signal import Signal


if __name__ == "__main__":
    """
    Questo modulo permette il download dei media per ogni segnale.
    Viene effettuata la conversione dei file secondo protocollo documentato.
    """
    with open(ProjectPath.INDEX_JSON, 'r', encoding='utf-8') as f:
        index = json.load(f)

    tqdm.write(f"Processing {len(index)} signals...")

    for pageid, title in tqdm(index.items()):
        try:
            tqdm.write(f'{pageid}\t{title}\t\t\t')
            signal = Signal(pageid, title)
            signal.load()

            os.makedirs(signal.media_dir, exist_ok=True)

            if signal.spectrum['url']:
                download_spectrum(signal.spectrum["url"], "1", signal.media_dir)

            if signal.audio['url']:
                download_audio(signal.audio["url"], "1", signal.media_dir)

        except Exception as e:
            tqdm.write(f"[ERROR] {title} ({pageid}): {e}")
