import json
import os
import argparse
import datetime
import shutil

import utils.json_utils as js

from tqdm import tqdm
from utils.constants import Path, Constants
from utils.sql_utils import ArtemisDB


class Static2Sqlite():

    def __init__(self, db_version):
        sig_db = ArtemisDB('data')
        sig_db.create_db()

####################### MARK: Sign DB
        sig_db.sign_db(
            'SigID',
            str(datetime.date.today()),
            db_version,
            Constants.EDITABLE
        )

        with open(Path.STATIC_DIR / 'index.json') as file:
            sigs_idx = json.load(file)

####################### MARK: Scan Tags
        all_cat = set()
        for sig_idx in sigs_idx.values():
            sig = js.Signal()
            sig.load(sig_idx['dir'])
            for cat in sig.category:
                all_cat.add(cat)

        cat_idx = {}
        for cat in sorted(all_cat):
            clb_id = sig_db.add_category_label(
                cat
            )
            cat_idx[cat] = clb_id

####################### MARK: Scan Signals
        for sig_idx in tqdm(sigs_idx.values()):
            sig = js.Signal()
            sig.load(sig_idx['dir'])
            
            sig_id = sig_db.add_signal(
                sig.name,
                sig.description,
                sig.url
            )

            for cat in sig.category:
                sig_db.add_category(
                    sig_id,
                    cat_idx[cat]
                )

            for freq in sig.frequency:
                sig_db.add_frequency(
                    sig_id,
                    freq['value'],
                    freq['description']
                )

            for band in sig.bandwidth:
                sig_db.add_bandwidth(
                    sig_id,
                    band['value'],
                    band['description']
                )

            for acf in sig.acf:
                sig_db.add_acf(
                    sig_id,
                    acf['value'],
                    acf['description']
                )

            for modulation in sig.modulation:
                sig_db.add_modulation(
                    sig_id,
                    modulation['value'],
                    modulation['description']
                )

            for mode in sig.mode:
                sig_db.add_mode(
                    sig_id,
                    mode['value'],
                    mode['description']
                )

            for location in sig.location:
                sig_db.add_location(
                    sig_id,
                    location['value'],
                    location['description']
                )

####################### MARK: Copy Media

            for media in sig.media:
                doc_id = sig_db.add_document(
                    media['extension'],
                    sig_id,
                    media['name'],
                    media['description'],
                    media['type'],
                    media['preview']
                )
                src_file_path = sig.media_dir / '{}.{}'.format(media['file_name'], media['extension'])
                dst_file_path = Path.MEDIA_DIR / '{}.{}'.format(doc_id, media['extension'])
                shutil.copy(src_file_path, dst_file_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Artemis DB Parser")
    parser.add_argument("--version", type=int, help="Database version", required=True)
    args = parser.parse_args()
    
    os.mkdir(Path.DATA_DIR)
    os.mkdir(Path.MEDIA_DIR)

    Static2Sqlite(args.version)
