import requests
import os

from PIL import Image

from constants import Path


def download_file(url, destination):
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(destination, 'wb') as file:
            file.write(response.content)
    else:
        # Report failed download
        pass
  
def download_spectrum(url, file_name, save_path):
    output_path = save_path / "{}.png".format(file_name)
    download_file(url, output_path)

    im = Image.open(output_path) 
    im = im.convert("RGB")
    im.save(output_path, "PNG")

def download_audio(url, file_name, save_path):
    audio_path = save_path / "{}.m4a".format(file_name)
    os.system("ffmpeg -i {} -ar 48000 -loglevel error -hide_banner -nostats {}".format(url, audio_path))
