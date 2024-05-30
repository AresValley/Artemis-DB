import difflib

from sql_utils import ArtemisDB
from constants import Constants


WRITE = 0

DB = ArtemisDB('data')
all_modulations = DB.select_all_modulation()

for mod in all_modulations:
    mdl_id = mod[0]
    value = mod[1]

    try:
        closer_match = difflib.get_close_matches(value, Constants.KNOWN_MODULATIONS, cutoff=0.5)[0]
        closer_match_description = Constants.KNOWN_MODULATIONS[closer_match]

        if WRITE:
            DB.update_modulation(
                mdl_id,
                closer_match,
                value
            )
        else:
            #print(value, closer_match)
            pass

    except:
        print('ERROR:', value)
