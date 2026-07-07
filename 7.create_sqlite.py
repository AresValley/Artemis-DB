import json
import os
import argparse
import datetime
import shutil

from tqdm import tqdm

from utils.constants import ProjectPath, Constants
from utils.generic_utils import checksum_sha256

from models.signal import Signal
from models.model import (
    database, Info, Signals, Category, CategoryLabel, Frequency, Bandwidth, 
    Modulation, Mode, Location, Acf, Documents, SqliteDatabase
)


class Static2Sqlite:
    def __init__(self, db_version):

        db = SqliteDatabase(ProjectPath.DATA_DIR / "data.sqlite", autoconnect=False)
        database.initialize(db)

        with database:

            database.create_tables([
                Info, Signals, Acf, Bandwidth, CategoryLabel, 
                Category, Documents, Frequency, Location, Mode, Modulation
            ])

        ####################### MARK: Sign DB
            Info.create(
                name='SigID',
                date=str(datetime.date.today()),
                version=db_version,
                editable=Constants.EDITABLE
            )

            with open(ProjectPath.INDEX_JSON) as file:
                index = json.load(file)

            all_signals = []

        ####################### MARK: Scan Tags
            print("Extracting signals and unique category tags...")
            for pageid, data in index.items():
                title = data['title']
                added_since = data['added_in_db']
                sig = Signal(pageid, title, added_since)
                sig.load()
                all_signals.append(sig)

            cat_idx = {}
            for cat in Constants.CATEGORIES:
                category = CategoryLabel.create(value=cat)
                cat_idx[cat] = category.clb_id

        ####################### MARK: Scan & Batch Insert Signals
            print("Executing fast batch load into SQLite database...")
            
            for sig in tqdm(all_signals):
                signal = Signals.create(
                    name=sig.title,
                    description=sig.full_description,
                    url=sig.url,
                    since_version=sig.added_since
                )
                sig_id = signal.sig_id

                for cat in sig.category:
                    Category.create(sig=sig_id, clb=cat_idx[cat])

                for freq in sig.frequency:
                    Frequency.create(sig=sig_id, value=freq['value'], description=freq['description'])

                for band in sig.bandwidth:
                    Bandwidth.create(sig=sig_id, value=band['value'], description=band['description'])

                for acf in sig.acf:
                    Acf.create(sig=sig_id, value=acf['value'], description=acf['description'])

                for modulation in sig.modulation:
                    Modulation.create(sig=sig_id, value=modulation['value'], description=modulation['description'])

                for mode in sig.mode:
                    Mode.create(sig=sig_id, value=mode['value'], description=mode['description'])

                for location in sig.location:
                    Location.create(sig=sig_id, value=location['value'], description=location['description'])

                ####################### MARK: Copy Media
                # Process Spectrum Image
                if sig.spectrum.get('url'):
                    document = Documents.create(
                        extension='png',
                        sig=sig_id,
                        name='Main',
                        description='This is the wiki spectrum of the signal from www.sigidwiki.com',
                        type='Image',
                        preview=1
                    )
                    doc_id = document.doc_id
                    src_file_path = sig.media_dir / "1.png"
                    dst_file_path = ProjectPath.MEDIA_DIR / f"{doc_id}.png"
                    
                    if src_file_path.exists():
                        shutil.copy(src_file_path, dst_file_path)
                    else:
                        print(f"\n[Warning] Spectrum file missing on disk: {src_file_path}")

                # Process Audio
                if sig.audio.get('url'):
                    document = Documents.create(
                        extension='ogg',
                        sig=sig_id,
                        name='Main',
                        description='This is the wiki audio of the signal from www.sigidwiki.com',
                        type='Audio',
                        preview=1
                    )
                    doc_id = document.doc_id
                    src_file_path = sig.media_dir / "1.ogg"
                    dst_file_path = ProjectPath.MEDIA_DIR / f"{doc_id}.ogg"
                    
                    if src_file_path.exists():
                        shutil.copy(src_file_path, dst_file_path)
                    else:
                        print(f"\n[Warning] Audio file missing on disk: {src_file_path}")


def make_archive():
    shutil.make_archive('sigID', 'tar', 'sigID')

    print("SHA256:\t{}".format(checksum_sha256('sigID.tar')))
    print("BYTES:\t{}".format(os.path.getsize('sigID.tar')))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Artemis DB Parser")
    parser.add_argument("-v", "--version", type=int, help="Database version", required=True)
    args = parser.parse_args()

    os.makedirs(ProjectPath.DATA_DIR, exist_ok=True)
    os.makedirs(ProjectPath.MEDIA_DIR, exist_ok=True)

    Static2Sqlite(args.version)
    make_archive()
