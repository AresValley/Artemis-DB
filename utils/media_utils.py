import subprocess
import requests
import time

from pathlib import Path
from PIL import Image


def download_file(url: str, destination: Path) -> bool:
    try:
        with requests.get(url, stream=True, timeout=15) as response:
            response.raise_for_status() 
            if 200 <= response.status_code < 300:
                with open(destination, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            file.write(chunk)
                return True
            else:
                print(f"Error during download {url}: {response.status_code}")
                return False
    except requests.RequestException as e:
        print(f"Error during download {url}: {e}")
        return False


def download_spectrum(url: str, file_name: str, save_path: Path):
    """Scarica lo spettro, gestisce l'estensione temporanea univoca e lo converte in PNG."""
    orig_ext = Path(url).suffix or ".tmp"

    temp_path = save_path / f"{file_name}_temp_{orig_ext}"
    output_path = save_path / f"{file_name}.png"

    save_path.mkdir(parents=True, exist_ok=True)

    if download_file(url, temp_path):
        try:
            with Image.open(temp_path) as im:
                im.load() 
                im.convert("RGB").save(output_path, "PNG")
        except Exception as e:
            print(f"Error: image conversione failed {file_name}: {e}")
        finally:
            try:
                temp_path.unlink(missing_ok=True)
            except Exception as e:
                print(f"Error: cannot remove {temp_path}: {e}")
    else:
        print(f"Download failed for {file_name}")


def download_audio(url: str, file_name: str, save_path: Path, allvorbis: bool = False, retries: int = 2, delay: int = 5):
    """
    Scarica e taglia i primi 60 secondi di un audio da un URL usando FFmpeg,
    con gestione dei tentativi in caso di errore.
    """
    save_path.mkdir(parents=True, exist_ok=True)

    orig_ext = Path(url).suffix.lower()
    if (orig_ext in ['.wav', '.flac']) and not allvorbis:
        codec = 'flac'
    else:
        codec = 'libvorbis'

    audio_path = save_path / f"{file_name}.ogg"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

    cmd = [
        "ffmpeg", "-y",
        "-rw_timeout", "60000000",
        "-user_agent", user_agent,
        "-ss", "0",
        "-t", "60",
        "-i", url,
        "-c:a", codec,
        "-fflags", "+bitexact",
        "-flags:a", "+bitexact",
        "-loglevel", "error",
        "-hide_banner",
        "-nostats",
        str(audio_path)
    ]

    for attempt in range(1, retries + 1):
        try:
            subprocess.run(cmd, check=True, timeout=75)
            return True
            
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
            if audio_path.exists():
                audio_path.unlink()

            if isinstance(e, subprocess.TimeoutExpired):
                print(f"[{attempt}/{retries}] Timeout {file_name}.")
            else:
                print(f"[{attempt}/{retries}] FFmpeg error with file {file_name}: {e}")

            if attempt < retries:
                print(f"Retry in {delay} s...")
                time.sleep(delay)
            else:
                print(f"All {retries} retries have failed for {file_name}.")
                
    return False
