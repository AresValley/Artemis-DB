import subprocess
import os
import requests

from pathlib import Path
from PIL import Image


def download_file(url: str, destination: Path) -> bool:
    try:
        with requests.get(url, stream=True, timeout=15) as response:
            if response.status_code == 200:
                with open(destination, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)
                return True
            else:
                print(format(f"Errore download {url}: Stato {response.status_code}"))
                return False
    except requests.RequestException as e:
        print(f"Errore di rete durante il download di {url}: {e}")
        return False


def download_spectrum(url: str, file_name: str, save_path: Path):
    """Scarica lo spettro, gestisce l'estensione temporanea e lo converte in PNG."""
    orig_ext = Path(url).suffix
    temp_path = save_path / f"{file_name}_temp{orig_ext}"
    output_path = save_path / f"{file_name}.png"

    if download_file(url, temp_path):
        try:
            with Image.open(temp_path) as im:
                im.convert("RGB").save(output_path, "PNG")
        except Exception as e:
            print(f"Errore durante la conversione dell'immagine: {e}")
        finally:
            if temp_path.exists():
                os.remove(temp_path)


def download_audio(url: str, file_name: str, save_path: Path, allvorbis: bool = False):
    ext = Path(url).suffix
    audio_path = save_path / f"{file_name}.ogg"

    if (ext in ['.wav', '.flac']) and not allvorbis:
        codec = 'flac'
    else:
        codec = 'libvorbis'

    cmd = [
        "ffmpeg", "-y",                # -y sovrascrive se il file esiste già
        "-i", url,                     # ffmpeg sa leggere direttamente gli URL di rete!
        "-ss", "0", 
        "-t", "60", 
        "-c:a", codec, 
        "-loglevel", "error", 
        "-hide_banner", 
        "-nostats", 
        str(audio_path)
    ]

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Errore durante l'esecuzione di ffmpeg per l'audio: {e}")
    except FileNotFoundError:
        print("Errore: 'ffmpeg' non è installato o non è presente nel PATH del sistema.")
