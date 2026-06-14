import subprocess
import requests

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
                print(f"Impossibile rimuovere il file temporaneo {temp_path}: {e}")
    else:
        print(f"Download fallito per {file_name}, conversione annullata.")


def download_audio(url: str, file_name: str, save_path: Path, allvorbis: bool = False):
    """
    Scarica e taglia i primi 60 secondi di un audio da un URL usando FFmpeg.
    """
    save_path.mkdir(parents=True, exist_ok=True)

    orig_ext = Path(url).suffix.lower()
    if (orig_ext in ['.wav', '.flac']) and not allvorbis:
        codec = 'flac'
    else:
        codec = 'libvorbis'

    audio_path = save_path / f"{file_name}.ogg"

    cmd = [
        "ffmpeg", "-y",
        "-rw_timeout", "15000000",      # Timeout di rete (15 secondi)
        "-ss", "0",                     # PRIMA di -i: interrompe il download appena ha i dati sufficienti
        "-t", "60",                     # Limita a 60 secondi
        "-i", url,
        "-c:a", codec,
        "-fflags", "+bitexact",
        "-flags:a", "+bitexact",
        "-loglevel", "error",
        "-hide_banner",
        "-nostats",
        str(audio_path)
    ]

    try:
        subprocess.run(cmd, check=True, timeout=45)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error during execution of ffmpeg {file_name}: {e}")
        if audio_path.exists():
            audio_path.unlink()
        return False
    except subprocess.TimeoutExpired:
        print(f"Error: conversion of {file_name} is taking too much time.")
        if audio_path.exists():
            audio_path.unlink()
        return False
