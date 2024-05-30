import datetime
import argparse
import time

import generic_utils as ut

from constants import *
from media_utils import *
from sql_utils import ArtemisDB


class SigidDataparser():

    def __init__(self, db_version, download_media=False) -> None:
        print('Extract main index...')
        idx_all = ut.extract_index(Url.SIGID_ALL)
        idx_cat = {}
        time.sleep(3)

        print('\nExtract category index...')
        for idx, cat in enumerate(Constants.CATEGORIES):
            print(f"{idx + 1}/{len(Constants.CATEGORIES)}\t{cat}")
            cat_sig = ut.extract_index(Url.SIGID_CAT + cat)
            idx_cat[cat] = list(cat_sig.keys())
            time.sleep(3)

        sig_db = ArtemisDB("data")
        sig_db.create_db()

        sig_db.sign_db(
            'SigID',
            str(datetime.date.today()),
            db_version,
            Constants.EDITABLE
        )

        #Create Standard Categories
        for cat in Constants.CATEGORIES:
            sig_db.add_category_label(
                cat.replace('_', ' ')
            )

        print('\nExtract signals...')
        for idx, sig in enumerate(idx_all):
            sig_url = idx_all[sig]
            sig_param = ut.extract_sig_param(sig_url)

            idx = sig_db.add_signal(
                sig,
                sig_param['Short Description'],
                sig_url
            )

            print(f"{idx}/{len(idx_all)}\t{sig}")

            for cat in Constants.CATEGORIES:
                if sig in idx_cat[cat]:
                    clb_id = Constants.CATEGORIES.index(cat) + 1
                    sig_db.add_category(idx, clb_id)

            if 'Frequencies' in sig_param:
                formatted_freq_list = ut.format_freq(sig_param['Frequencies'])
                for freq in formatted_freq_list:
                    sig_db.add_frequency(
                        idx,
                        freq,
                        ''
                    )

            if 'Bandwidth' in sig_param:
                formatted_band_list = ut.format_freq(sig_param['Bandwidth'])
                for band in formatted_band_list:
                    sig_db.add_bandwidth(
                        idx,
                        band,
                        ''
                    )

            formatted_acf = ut.format_acf(sig_param['ACF'])
            for acf in formatted_acf:
                sig_db.add_acf(
                    idx,
                    acf[1],
                    acf[0]
                )

            formatted_modulation = ut.format_text(sig_param['Modulation'])
            for modulation in formatted_modulation:
                sig_db.add_modulation(
                    idx,
                    modulation,
                    ''
                )

            formatted_mode = ut.format_text(sig_param['Mode'])
            for mode in formatted_mode:
                sig_db.add_mode(
                    idx,
                    mode,
                    ''
                )

            formatted_location = ut.format_text(sig_param['Location'])
            for location in formatted_location:
                if location != '':
                    sig_db.add_location(
                        idx,
                        location,
                        ''
                    )

            if download_media:
                if 'Spectrum' in sig_param and sig_param['Spectrum'] not in Url.IMG_EXCLUSION_URL:
                    last_row = sig_db.add_document(
                        'png',
                        idx,
                        'sigId Spectrum',
                        'This is the wiki spectrum of the signal from www.sigidwiki.com',
                        'Image',
                        1
                    )
                    download_spectrum(sig_param['Spectrum'], last_row)

                if 'Audio' in sig_param:
                    last_row = sig_db.add_document(
                        'm4a',
                        idx,
                        'sigId Audio',
                        'This is the wiki audio sample of the signal from www.sigidwiki.com',
                        'Audio',
                        1
                    )
                    download_audio(sig_param['Audio'], last_row)

            time.sleep(3)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Artemis DB Parser")
    parser.add_argument("--version", type=int, help="Database version", required=True)
    parser.add_argument("--media", action='store_true', help="Download media from sigid or aresvalley")
    args = parser.parse_args()
    
    os.mkdir(Path.DATA_DIR)
    os.mkdir(Path.MEDIA_DIR)

    SigidDataparser(args.version, args.media)
