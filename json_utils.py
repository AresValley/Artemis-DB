import json
from constants import Path


class Signal():
    def __init__(self) -> None:
        self.dir = None
        self.media_dir = None
        self.name = None
        self.url = None
        self.description = None

        self.category = None
        self.frequency = None
        self.bandwidth = None
        self.acf = None
        self.modulation = None
        self.mode = None
        self.location = None

        self.media = None


    def load(self, dir_name):
        self.dir = Path.STATIC_DIR / str(dir_name)
        self.media_dir = self.dir / 'media'
        self._read_sig_json()
        self._read_description()
        self._read_media_json()


    def _read_sig_json(self):
        with open(self.dir / 'signal.json') as file:
            sig_json = json.load(file)

        self.name = sig_json['signal']['name']
        self.url = sig_json['signal']['url']
        self.category = sig_json['category']
        self.frequency = sig_json['frequency']
        self.bandwidth = sig_json['bandwidth']
        self.acf = sig_json['acf']
        self.mode = sig_json['mode']
        self.modulation = sig_json['modulation']
        self.location = sig_json['location']


    def _read_description(self):
        with open(self.dir / 'description.md', encoding='utf-8') as file:
            self.description = file.read()   


    def _read_media_json(self):
        with open(self.dir / 'media.json') as file:
            self.media = json.load(file)
