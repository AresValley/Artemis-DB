import json
import os
import shutil

import utils.generic_utils as ut
from utils.constants import Path, Url
from utils.media_utils import download_audio, download_spectrum


class SigidDataparser:

    def __init__(self, sig_name: str, sig_url: str):
        self.sig_name = sig_name
        self.sig_url = sig_url

    def _build_metadata_list(self, sig_param: dict, param_key: str, format_func=ut.format_text) -> list:
        """Helper per evitare la ripetizione dei cicli dei metadati."""
        result = []
        if param_key in sig_param:
            formatted_list = format_func(sig_param[param_key])
            for item in formatted_list:
                # Nel caso di ACF, format_acf restituisce una tupla (desc, valore)
                if param_key == 'ACF':
                    result.append({'value': item[1], 'description': item[0]})
                elif item != '':
                    result.append({'value': item, 'description': ''})
        return result

    def run(self):
        sig_param = ut.extract_sig_param(self.sig_url)
        print("Dati estratti con successo!")

        index_path = Path.STATIC_DIR / 'index.json'
        
        with open(index_path, encoding='utf-8') as file:
            sigs_idx = json.load(file)

        # 1. Gestione Indice e Directory
        if self.sig_name not in sigs_idx:
            print('NEW signal')
            last_sig = list(sigs_idx)[-1] if sigs_idx else None
            sig_id = (sigs_idx[last_sig]['dir'] + 1) if last_sig else 1

            sigs_idx[self.sig_name] = {'dir': sig_id, 'url': self.sig_url}

            with open(index_path, 'w', encoding='utf-8') as json_file:
                json.dump(sigs_idx, json_file, indent=4)

            sig_dir = Path.STATIC_DIR / str(sig_id)
            os.makedirs(sig_dir, exist_ok=True)
        else:
            print('UPDATING existing signal')
            sig_id = sigs_idx[self.sig_name]['dir']
            sig_dir = Path.STATIC_DIR / str(sig_id)
            if sig_dir.exists():
                shutil.rmtree(sig_dir)
            os.makedirs(sig_dir, exist_ok=True)

        # 2. Costruzione del JSON del segnale
        sig_json = {
            'signal': {'name': self.sig_name, 'url': self.sig_url},
            'category': sig_param.get('Category', ''),
            'frequency': self._build_metadata_list(sig_param, 'Frequencies', ut.format_freq),
            'bandwidth': self._build_metadata_list(sig_param, 'Bandwidth', ut.format_freq),
            'acf': self._build_metadata_list(sig_param, 'ACF', ut.format_acf),
            'modulation': self._build_metadata_list(sig_param, 'Modulation'),
            'mode': self._build_metadata_list(sig_param, 'Mode'),
            'location': self._build_metadata_list(sig_param, 'Location')
        }

        # Scrittura Descrizione
        if 'Short Description' in sig_param:
            with open(sig_dir / 'description.md', 'w', encoding='utf-8') as f:
                f.write(sig_param['Short Description'])

        with open(sig_dir / 'signal.json', 'w', encoding='utf-8') as json_file:
            json.dump(sig_json, json_file, indent=4)

        # 3. Gestione Media
        sig_media_dir = sig_dir / 'media'
        os.makedirs(sig_media_dir, exist_ok=True)
        media_json = []

        # Blocco Spectrum
        if 'Spectrum' in sig_param and sig_param['Spectrum'] not in Url.IMG_EXCLUSION_URL:
            media_json.append({
                'file_name': '1',
                'extension': 'png',
                'name': 'Main',
                'description': 'This is the wiki spectrum of the signal from www.sigidwiki.com',
                'type': 'Image',
                'preview': 1
            })
            download_spectrum(sig_param['Spectrum'], '1', sig_media_dir)

        # Blocco Audio
        if 'Audio' in sig_param:
            media_json.append({
                'file_name': '1',
                'extension': 'ogg',
                'name': 'Main',
                'description': 'This is the wiki audio sample of the signal from www.sigidwiki.com',
                'type': 'Audio',
                'preview': 1
            })
            download_audio(sig_param['Audio'], '1', sig_media_dir, allvorbis=False)

        with open(sig_dir / 'media.json', 'w', encoding='utf-8') as json_file:
            json.dump(media_json, json_file, indent=4)


if __name__ == "__main__":
    parser = SigidDataparser(sig_name='SKiYMET', sig_url='https://www.sigidwiki.com/wiki/SKiYMET_meteor_radar')
    parser.run()
