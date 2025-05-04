import difflib

from utils.sql_utils import ArtemisDB
from utils.constants import Constants


DRY_RUN = True  # Imposta a False per eseguire l'update

DB = ArtemisDB('data')
all_modulations = DB.select_all_modulation()

for mod in all_modulations:
    mdl_id = mod[0]
    value = mod[1]

    best_match = None
    best_ratio = 0.0

    for known in Constants.KNOWN_MODULATIONS:
        ratio = difflib.SequenceMatcher(None, value, known).ratio()
        if ratio > best_ratio:
            best_match = known
            best_ratio = ratio

    percentage = round(best_ratio * 100, 2)

    if best_match:
        if DRY_RUN:
            if percentage < 85:
                print(f"{value}  -->  {best_match}  ({percentage}%)")
        else:
            DB.update_modulation(
                mdl_id,
                best_match,
                value
            )
    else:
        print('NO MATCH:', value)
