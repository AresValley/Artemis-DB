import requests
import os

from PIL import Image
from utils.generic_utils import get_extension

def download_file(url, destination):
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(destination, 'wb') as file:
            file.write(response.content)
    else:
        # Report failed download
        pass

def download_spectrum(url, file_name, save_path):
    """ Download Spectrum sample and convert it to .png file
    """
    output_path = save_path / "{}.png".format(file_name)
    download_file(url, output_path)

    im = Image.open(output_path) 
    im = im.convert("RGB")
    im.save(output_path, "PNG")

def download_audio(url, file_name, save_path, allvorbis=False):
    """ Download Audio sample and convert it to .ogg file
        Audio codedc is different based on the source file:
            - flac if the origin file is lossless
            - libvorbis if the file is already compressed
        Audio is cropped to 60s (if longer)
        allvorbis forces to use always the vorbis codec (max compression)
    """
    ext = get_extension(url)
    audio_path = save_path / "{}.ogg".format(file_name)

    if ext == 'wav' or ext == 'flac' and not allvorbis:
        print('flac')
        codec = 'flac'
    else:
        codec = 'libvorbis'
    
    os.system("ffmpeg -i {} -ss 0 -t 60 -c:a {} -loglevel error -hide_banner -nostats {}".format(url, codec, audio_path))
