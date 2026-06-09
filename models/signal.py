import json
import urllib.parse

from pathlib import Path

from utils.constants import ProjectPath


class Signal:
    def __init__(self, pageid: int, title: str):
        self.pageid = pageid
        self.title = title

        self.spectrum_filename = None
        self.audio_filename = None

        self.category = []
        self.frequency = []
        self.bandwidth = []
        self.acf = []
        self.modulation = []
        self.mode = []
        self.location = []

        self.short_description = None
        self.description = None

    @property
    def url(self) -> str:
        encoded_title = urllib.parse.quote(self.title.replace(" ", "_"), safe=":/")
        return f"{ProjectPath.SIGID_DOMAIN}/wiki/{encoded_title}"

    @property
    def dir(self) -> Path:
        return ProjectPath.STATIC_DIR / str(self.pageid)

    @property
    def json_path(self) -> str:
        return self.dir / 'signal.json'

    def save_json(self):
        output_data = {
            "pageid": self.pageid,
            "title": self.title,
            "spectrum": self.spectrum_filename,
            "audio": self.audio_filename,
            "category": self.category,
            "frequency": self.frequency,
            "bandwidth": self.bandwidth,
            "acf": self.acf,
            "modulation": self.modulation,
            "mode": self.mode,
            "location": self.location,
            "short description": self.short_description,
            "description": self.description
        }

        self.dir.mkdir(parents=True, exist_ok=True)

        with open(self.json_path, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=4)


    def load_json(self):
        if not self.json_path.exists():
            print(f"Error: file {self.json_path} does not exist.")
            return False

        try:
            with open(self.json_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.pageid = data['pageid']
            self.title = data['title']
            self.spectrum_filename = data['spectrum']
            self.audio_filename = data['audio']
            self.category = data['category']
            self.frequency = data['frequency']
            self.bandwidth = data['bandwidth']
            self.acf = data['acf']
            self.modulation = data['modulation']
            self.mode = data['mode']
            self.location = data['location']
            self.short_description = data['short description']
            self.description = data['description']

            return True

        except json.JSONDecodeError:
            print(f"Error: The file {self.json_path} is not valid JSON.")
            return False

        except Exception as e:
            print(f"Error during JSON loading: {e}")
            return False
