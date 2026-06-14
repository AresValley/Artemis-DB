import json
import os
import argparse
import datetime
import shutil

from tqdm import tqdm

from utils.constants import ProjectPath, Constants
from utils.sql_utils import ArtemisDB
from utils.generic_utils import checksum_sha256
from models.signal import Signal


class Static2Sqlite:
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

        with open(ProjectPath.INDEX_JSON) as file:
            index = json.load(file)

        all_signals = []

        ####################### MARK: Scan Tags
        print("Extracting signals and unique category tags...")
        for pageid, title in index.items():
            sig = Signal(pageid, title)
            sig.load()
            all_signals.append(sig)

        cat_idx = {}
        for cat in Constants.CATEGORIES:
            clb_id = sig_db.add_category_label(cat)
            cat_idx[cat] = clb_id

        ####################### MARK: Scan & Batch Insert Signals
        print("Executing fast batch load into SQLite database...")
        
        # Open transaction block
        sig_db.begin_transaction()

        try:
            for sig in tqdm(all_signals):
                sig_id = sig_db.add_signal(
                    sig.title,
                    sig.full_description,
                    sig.url
                )

                for cat in sig.category:
                    sig_db.add_category(sig_id, cat_idx[cat])

                for freq in sig.frequency:
                    sig_db.add_frequency(sig_id, freq['value'], freq['description'])

                for band in sig.bandwidth:
                    sig_db.add_bandwidth(sig_id, band['value'], band['description'])

                for acf in sig.acf:
                    sig_db.add_acf(sig_id, acf['value'], acf['description'])

                for modulation in sig.modulation:
                    sig_db.add_modulation(sig_id, modulation['value'], modulation['description'])

                for mode in sig.mode:
                    sig_db.add_mode(sig_id, mode['value'], mode['description'])

                for location in sig.location:
                    sig_db.add_location(sig_id, location['value'], location['description'])

                ####################### MARK: Copy Media
                # Process Spectrum Image
                if sig.spectrum.get('url'):
                    doc_id = sig_db.add_document(
                        'png',
                        sig_id,
                        'Main',
                        'This is the wiki spectrum of the signal from www.sigidwiki.com',
                        'Image',
                        1
                    )
                    src_file_path = sig.media_dir / "1.png"
                    dst_file_path = ProjectPath.MEDIA_DIR / f"{doc_id}.png"
                    
                    if src_file_path.exists():
                        shutil.copy(src_file_path, dst_file_path)
                    else:
                        print(f"\n[Warning] Spectrum file missing on disk: {src_file_path}")

                # Process Audio
                if sig.audio.get('url'):
                    doc_id = sig_db.add_document(
                        'ogg',
                        sig_id,
                        'Main',
                        'This is the wiki audio of the signal from www.sigidwiki.com',
                        'Audio',
                        1
                    )
                    src_file_path = sig.media_dir / "1.ogg"
                    dst_file_path = ProjectPath.MEDIA_DIR / f"{doc_id}.ogg"
                    
                    if src_file_path.exists():
                        shutil.copy(src_file_path, dst_file_path)
                    else:
                        print(f"\n[Warning] Audio file missing on disk: {src_file_path}")

            # Commit everything onto disk in one sequence
            sig_db.commit_transaction()
            print("Import successfully completed!")

        except Exception as e:
            # Revert entire process if something breaks midway to prevent DB corruption
            sig_db.rollback_transaction()
            print(f"\n[Critical Error] ETL Pipeline aborted. Database rolled back. Error: {e}")
            raise e


def make_archive():
    shutil.make_archive('sigID', 'tar', 'sigID')

    print("SHA256:\t{}".format(checksum_sha256('sigID.tar')))
    print("BYTES:\t{}".format(os.path.getsize('sigID.tar')))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Artemis DB Parser")
    parser.add_argument("--version", type=int, help="Database version", required=True)
    args = parser.parse_args()

    os.makedirs(ProjectPath.DATA_DIR, exist_ok=True)
    os.makedirs(ProjectPath.MEDIA_DIR, exist_ok=True)

    Static2Sqlite(args.version)
    make_archive()
