import os

from pathlib import Path


class Path():
    BASE_DIR        = Path(os.path.dirname(__file__))
    DATA_DIR        = BASE_DIR / "sigID"
    MEDIA_DIR       = DATA_DIR / "media"

class Url():
    SIGID_DOMAIN        = "https://www.sigidwiki.com"
    SIGID_ALL           = "https://www.sigidwiki.com/wiki/Database"
    SIGID_CAT           = "https://www.sigidwiki.com/wiki/Category:"
    IMG_EXCLUSION_URL   = ["https://www.sigidwiki.com/images/1/12/NoWaterfallFiller.png"]

class Constants():
    EDITABLE = 0
    
    UNIT_TO_FACTOR = {"Hz": 1, "kHz": 10**3, "MHz": 10**6, "GHz": 10**9}

    CATEGORIES = [
        "Aviation",
        "Marine",
        "Navigation",
        "Amateur_Radio",
        "Trunked_Radio",
        "Military",
        "Commercial",
        "Utility",
        "Analogue",
        "Digital",
        "Satellite",
        "Radar",
        "Interfering",
        "Numbers_Stations",
        "Time"
    ]

    SIG_EXCLUSION = [
        "Unknown Data Transmission",
        "Unknown tone on MURS 154.600",
        "Unidentified modem sound",
        "Unidentified Pulsating Signal 1915 KHz",
        "1234",
        "Errant Signal on 2m Ham Band",
        "AC Interference",
        "HP laptop",
        "Interferance signal from old computer screen"
    ]

    KNOWN_MODULATIONS = {
    'AM': 'Amplitude Modulation',
    'FM': 'Frequency Modulation',
    'PM': 'Phase Modulation',
    'LSB': 'Lower Side Band',
    'USB': 'Upper Side Band',
    'VSB': 'Vestigial Sideband Modulation',
    'QAM': 'Quadrature Amplitude Modulation',
    'PSK': 'Phase-Shift Keying',
    'FSK': 'Frequency-Shift Keying',
    'ASK': 'Amplitude-Shift Keying',
    'MSK': 'Minimum-Shift Keying',
    'IFK': 'Incremental frequency keying',
    'OOK': 'On-Off Keying',
    'FDM': 'Frequency-Division Multiplexing',
    'BOC': 'Binary Offset Carrier Modulation',
    'CDMA': 'Code Division Multiple Access',
    'TDMA': 'Time Division Multiple Access',
    'CSS': 'Chirp Spread Spectrum',
    'CW': 'Continuous Wave',
    'DSSS': 'Direct Sequence Spread Spectrum',
    'FBMC': 'Filter Bank Multi Carrier',
    'UFMC': 'Universal Filtered Multi Carrier',
    'FHSS': 'Frequency Hopping Spread Spectrum',
    'PCM': 'Pulse Code Modulation',
    'PPM': 'Pulse Position Modulation',
    'FMCW': 'Frequency-Modulated Continuous Wave',
    'Pulse': 'Pulse'
    }

class Query():
    CREATE_SIGNALS = """
        CREATE TABLE signals (
            SIG_ID      INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME        TEXT,
            DESCRIPTION TEXT,
            URL         TEXT
        )
    """

    CREATE_CATEGORY = """
        CREATE TABLE category (
            CAT_ID      INTEGER PRIMARY KEY AUTOINCREMENT,
            SIG_ID      INTEGER,
            CLB_ID      INTEGER,
            FOREIGN KEY (SIG_ID) REFERENCES signals (SIG_ID) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (CLB_ID) REFERENCES category_label (CLB_ID) ON DELETE CASCADE ON UPDATE CASCADE
        )
    """

    CREATE_CATEGORY_LABELS = """
        CREATE TABLE category_label (
            CLB_ID      INTEGER PRIMARY KEY AUTOINCREMENT,
            VALUE       TEXT
        )   
    """

    CREATE_DOCUMENTS = """
        CREATE TABLE documents (
            DOC_ID      INTEGER PRIMARY KEY AUTOINCREMENT,
            SIG_ID      INTEGER,
            EXTENSION   TEXT,
            NAME        TEXT,
            DESCRIPTION TEXT,
            TYPE        TEXT,
            PREVIEW     INTEGER,
            FOREIGN KEY (SIG_ID) REFERENCES signals (SIG_ID) ON DELETE CASCADE ON UPDATE CASCADE
        )
    """
    
    CREATE_FREQUENCY = """
        CREATE TABLE frequency (
            FREQ_ID     INTEGER PRIMARY KEY AUTOINCREMENT,
            SIG_ID      INTEGER,
            VALUE       INTEGER,
            DESCRIPTION TEXT,
            FOREIGN KEY (SIG_ID) REFERENCES signals (SIG_ID) ON DELETE CASCADE ON UPDATE CASCADE
        )    
    """
    
    CREATE_BANDWIDTH = """
        CREATE TABLE bandwidth (
            BAND_ID     INTEGER PRIMARY KEY AUTOINCREMENT,
            SIG_ID      INTEGER,
            VALUE       INTEGER,
            DESCRIPTION TEXT,
            FOREIGN KEY (SIG_ID) REFERENCES signals (SIG_ID) ON DELETE CASCADE ON UPDATE CASCADE
        )    
    """    

    CREATE_MODULATION = """
        CREATE TABLE modulation (
            MDL_ID      INTEGER PRIMARY KEY AUTOINCREMENT,
            SIG_ID      INTEGER,
            VALUE       TEXT,
            DESCRIPTION TEXT,
            FOREIGN KEY (SIG_ID) REFERENCES signals (SIG_ID) ON DELETE CASCADE ON UPDATE CASCADE
        )    
    """    

    CREATE_MODE = """
        CREATE TABLE mode (
            MOD_ID      INTEGER PRIMARY KEY AUTOINCREMENT,
            SIG_ID      INTEGER,
            VALUE       TEXT,
            DESCRIPTION TEXT,
            FOREIGN KEY (SIG_ID) REFERENCES signals (SIG_ID) ON DELETE CASCADE ON UPDATE CASCADE
        )    
    """

    CREATE_LOCATION = """
        CREATE TABLE location (
            LOC_ID      INTEGER PRIMARY KEY AUTOINCREMENT,
            SIG_ID      INTEGER,
            VALUE       TEXT,
            DESCRIPTION TEXT,
            FOREIGN KEY (SIG_ID) REFERENCES signals (SIG_ID) ON DELETE CASCADE ON UPDATE CASCADE
        )    
    """

    CREATE_ACF = """
        CREATE TABLE acf (
            ACF_ID      INTEGER PRIMARY KEY AUTOINCREMENT,
            SIG_ID      INTEGER,
            VALUE       FLOAT,
            DESCRIPTION TEXT,
            FOREIGN KEY (SIG_ID) REFERENCES signals (SIG_ID) ON DELETE CASCADE ON UPDATE CASCADE
        )    
    """

    CREATE_INFO = """
        CREATE TABLE info (
            NAME        TEXT,
            DATE        TEXT,
            VERSION     INTEGER,
            EDITABLE    INTEGER
        )   
    """

    CREATE_VIEW_FREQ = """
        CREATE VIEW FREQ_RANGE AS
            SELECT SIG_ID,
                MIN(VALUE) AS MIN_VALUE,
                MAX(VALUE) AS MAX_VALUE
            FROM frequency
            GROUP BY SIG_ID
    """        

    CREATE_VIEW_BAND = """
        CREATE VIEW BAND_RANGE AS
            SELECT SIG_ID,
                MIN(VALUE) AS MIN_VALUE,
                MAX(VALUE) AS MAX_VALUE
            FROM bandwidth
            GROUP BY SIG_ID 
    """

    INSERT_SIGNAL = """
        INSERT INTO signals (
            NAME,
            DESCRIPTION,
            URL
        ) VALUES (?,?,?)
    """

    INSERT_CATEGORY = """
        INSERT INTO category (
            SIG_ID,
            CLB_ID
        ) VALUES (?,?)
    """

    INSERT_CATEGORY_LABEL = """
        INSERT INTO category_label (
            VALUE
        ) VALUES (?)
    """

    INSERT_INFO = """
        INSERT INTO info (
            NAME,
            DATE,
            VERSION,
            EDITABLE
        ) VALUES (?,?,?,?)
    """

    INSERT_DOCUMENTS = """
        INSERT INTO documents (
            EXTENSION,
            SIG_ID,
            NAME,
            DESCRIPTION,
            TYPE,
            PREVIEW 
        ) VALUES (?,?,?,?,?,?)
    """

    INSERT_FREQUENCY = """
        INSERT INTO frequency (
            SIG_ID,
            VALUE,
            DESCRIPTION
        ) VALUES (?,?,?)
    """

    INSERT_BANDWIDTH = """
        INSERT INTO bandwidth (
            SIG_ID,
            VALUE,
            DESCRIPTION
        ) VALUES (?,?,?)
    """

    INSERT_MODULATION = """
        INSERT INTO modulation (
            SIG_ID,
            VALUE,
            DESCRIPTION
        ) VALUES (?,?,?)
    """

    INSERT_MODE = """
        INSERT INTO mode (
            SIG_ID,
            VALUE,
            DESCRIPTION
        ) VALUES (?,?,?)
    """

    INSERT_LOCATION = """
        INSERT INTO location (
            SIG_ID,
            VALUE,
            DESCRIPTION
        ) VALUES (?,?,?)
    """

    INSERT_ACF = """
        INSERT INTO acf (
            SIG_ID,
            VALUE,
            DESCRIPTION
        ) VALUES (?,?,?)
    """

######################## Post-process only

    SELECT_ALL_MODULATION = "SELECT MDL_ID, VALUE FROM modulation"

    UPDATE_MODULATION = """
        UPDATE modulation SET
            VALUE = ?,
            DESCRIPTION = ?
        WHERE MDL_ID = ?
    """
