import json
import urllib.parse

from pathlib import Path

from utils.constants import ProjectPath


class Signal:
    def __init__(self, pageid: int, title: str):
        self.pageid = pageid
        self.title = title

        self.spectrum = {
            'filename': None,
            'url': None
        }
        self.audio = {
            'filename': None,
            'url': None
        }

        self.category = []
        self.frequency = []
        self.bandwidth = []
        self.acf = []
        self.modulation = []
        self.mode = []
        self.location = []

        self.short_description = ''
        self.description = ''

    @property
    def url(self) -> str:
        encoded_title = urllib.parse.quote(self.title.replace(" ", "_"), safe=":/")
        return f"{ProjectPath.SIGID_DOMAIN}/wiki/{encoded_title}"

    @property
    def dir(self) -> Path:
        return ProjectPath.STATIC_DIR / str(self.pageid)

    @property
    def media_dir(self) -> Path:
        return ProjectPath.STATIC_DIR / str(self.pageid) / 'media'

    @property
    def json_path(self) -> str:
        return self.dir / 'signal.json'

    @property
    def full_description(self) -> str:
        return f'# SUMMARY\n{self.short_description}\n# DETAILS\n{self.description}'

    def save(self):
        output_data = {
            "pageid": self.pageid,
            "title": self.title,
            "spectrum": self.spectrum,
            "audio": self.audio,
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


    def load(self):
        if not self.json_path.exists():
            print(f"Error: file {self.json_path} does not exist.")
            return False

        try:
            with open(self.json_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.pageid = data['pageid']
            self.title = data['title']
            self.spectrum = data['spectrum']
            self.audio = data['audio']
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
    
    def check_integrity(self):
        # 1. Helper per il controllo della virgola (campi testuali)
        def check_comma(items, alert_msg):
            for item in items:
                if ',' in item['value']:
                    print(alert_msg)
                    print(f'{self.pageid}\t{item["value"]}')

        # 2. Helper per il controllo dei numeri interi non negativi
        def check_non_negative_int(items, field_name):
            for item in items:
                val = item['value']
                # Verifica se è convertibile in intero positivo o zero
                try:
                    # str(int(val)) == str(val) gestisce stringhe come '120'
                    # ma fallisce giustamente su '120.5' o '-5'
                    if int(val) < 0:
                        raise ValueError
                except (ValueError, TypeError):
                    print(f'{field_name} non valido (richiesto intero >= 0)')
                    print(f'{self.pageid}\t{val}')

        # Esecuzione controlli stringhe
        check_comma(self.mode, 'modo malformato')
        check_comma(self.modulation, 'modulazione malformata')
        check_comma(self.location, 'location malformata')

        # Esecuzione controlli numerici
        check_non_negative_int(self.frequency, 'frequency')
        check_non_negative_int(self.bandwidth, 'bandwidth')
