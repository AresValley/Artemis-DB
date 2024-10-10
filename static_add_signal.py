import os
import json

import utils.generic_utils as ut

from utils.constants import Path, Url
from utils.media_utils import download_spectrum, download_audio


class SigidDataparser():

    def __init__(self):

        sig_url     = 'https://www.sigidwiki.com/wiki/Radar_altimeter'
        sig_name    = 'Radar altimeter'

        with open(Path.STATIC_DIR / 'index.json') as file:
            sigs_idx = json.load(file)
        
        last_sig = list(sigs_idx)[-1]
        last_dir = sigs_idx[last_sig]['dir']
        sig_id = last_dir + 1

        sig_param = ut.extract_sig_param(sig_url)

        sigs_idx[sig_name] = {
            'dir': sig_id,
            'url': sig_url
        }

        with open(Path.STATIC_DIR / 'index.json', 'w') as json_file:
            json.dump(sigs_idx, json_file, indent=4)

        sig_json = {}

        sig_dir = Path.STATIC_DIR / str(sig_id)
        os.mkdir(sig_dir)

        sig_json['signal'] = {
            'name': sig_name,
            'url': sig_url
        }

        with open(sig_dir / 'description.md', 'w', encoding='utf-8') as f:
            f.write(sig_param['Short Description'])


        sig_json['category'] = sig_param['Category']


        sig_json['frequency'] = []
        if 'Frequencies' in sig_param:
            formatted_freq_list = ut.format_freq(sig_param['Frequencies'])
            for freq in formatted_freq_list:
                sig_json['frequency'].append(
                    {
                        'value': freq,
                        'description': ''
                    }
                )


        sig_json['bandwidth'] = []
        if 'Bandwidth' in sig_param:
            formatted_band_list = ut.format_freq(sig_param['Bandwidth'])
            for band in formatted_band_list:
                sig_json['bandwidth'].append(
                    {
                        'value': band,
                        'description': ''
                    }
                )


        formatted_acf = ut.format_acf(sig_param['ACF'])
        sig_json['acf'] = []
        for acf in formatted_acf:
            sig_json['acf'].append(
                {
                    'value': acf[1],
                    'description': acf[0]
                }
            )


        formatted_modulation = ut.format_text(sig_param['Modulation'])
        sig_json['modulation'] = []
        for modulation in formatted_modulation:
            sig_json['modulation'].append(
                {
                    'value': modulation,
                    'description': ''
                }
            )


        formatted_mode = ut.format_text(sig_param['Mode'])
        sig_json['mode'] = []
        for mode in formatted_mode:
            sig_json['mode'].append(
                {
                    'value': mode,
                    'description': ''
                }
            )


        formatted_location = ut.format_text(sig_param['Location'])
        sig_json['location'] = []
        for location in formatted_location:
            if location != '':
                sig_json['location'].append(
                    {
                        'value': location,
                        'description': ''
                    }
                )

        with open(sig_dir / 'signal.json', 'w') as json_file:
            json.dump(sig_json, json_file, indent=4)


        sig_media_dir = sig_dir / 'media'
        os.mkdir(sig_media_dir)
        media_json = []
        if 'Spectrum' in sig_param and sig_param['Spectrum'] not in Url.IMG_EXCLUSION_URL:
            file_name = '1'
            media_json.append(
                {
                    'file_name': file_name,
                    'extension': 'png',
                    'name': 'Main',
                    'description': 'This is the wiki spectrum of the signal from www.sigidwiki.com',
                    'type': 'Image',
                    'preview': 1
                }
            )
            download_spectrum(sig_param['Spectrum'], file_name, sig_media_dir)

            if 'Audio' in sig_param:
                file_name = '1'
                media_json.append(
                    {
                        'file_name': file_name,
                        'extension': 'ogg',
                        'name': 'Main',
                        'description': 'This is the wiki audio sample of the signal from www.sigidwiki.com',
                        'type': 'Audio',
                        'preview': 1
                    }
                )
                download_audio(sig_param['Audio'], file_name, sig_media_dir, allvorbis=False)

        with open(sig_dir / 'media.json', 'w') as json_file:
            json.dump(media_json, json_file, indent=4)


if __name__ == "__main__":
    SigidDataparser()
