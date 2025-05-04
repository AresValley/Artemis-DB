import os

from pathlib import Path


class Path():
    BASE_DIR        = Path(os.path.dirname(__file__)) / '..'
    DATA_DIR        = BASE_DIR / "sigID"
    MEDIA_DIR       = DATA_DIR / "media"
    STATIC_DIR      = BASE_DIR / "static"

class Url():
    SIGID_DOMAIN        = "https://www.sigidwiki.com"
    SIGID_ALL           = "https://www.sigidwiki.com/wiki/Database"
    SIGID_CAT           = "https://www.sigidwiki.com/wiki/Category:"
    IMG_EXCLUSION_URL   = ["https://www.sigidwiki.com/images/1/12/NoWaterfallFiller.png"]

class Constants():
    EDITABLE = -1
    
    UNIT_TO_FACTOR = {"Hz": 1, "kHz": 10**3, "MHz": 10**6, "GHz": 10**9}

    CATEGORIES = [
        "Aviation",
        "Marine",
        "Navigation",
        "Amateur Radio",
        "Trunked Radio",
        "Military",
        "Commercial",
        "Utility",
        "Analogue",
        "Digital",
        "Satellite",
        "Radar",
        "Interfering",
        "Numbers Stations",
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
    # Analog Modulation
    'AM': 'Amplitude Modulation',
    'FM': 'Frequency Modulation',
    'PM': 'Phase Modulation',
    'DSB': 'Double-Sideband Modulation',
    'DSB-WC': 'Double-Sideband with Carrier',
    'DSB-SC': 'Double-Sideband Suppressed Carrier',
    'DSB-RC': 'Double-Sideband Reduced Carrier',
    'SSB': 'Single-Sideband Modulation',
    'SSB-WC': 'Single-Sideband with Carrier',
    'SSB-SC': 'Single-Sideband Suppressed Carrier',
    'SSB-RC': 'Single-Sideband Reduced Carrier',
    'LSB': 'Lower Sideband', # Often part of SSB
    'USB': 'Upper Sideband', # Often part of SSB
    'VSB': 'Vestigial Sideband Modulation',

    # Digital Keying / Digital Modulation
    'ASK': 'Amplitude-Shift Keying',
    'BASK': 'Binary Amplitude-Shift Keying', # Equivalent to OOK
    'OOK': 'On-Off Keying', # Equivalent to BASK
    'M-ary ASK': 'M-ary Amplitude-Shift Keying',
    'FSK': 'Frequency-Shift Keying',
    'AFSK': 'Audio Frequency-Shift Keying',
    'BFSK': 'Binary Frequency-Shift Keying',
    'M-ary FSK': 'M-ary Frequency-Shift Keying',
    'GFSK': 'Gaussian Frequency-Shift Keying',
    'CPFSK': 'Continuous Phase Frequency-Shift Keying',
    'MSK': 'Minimum-Shift Keying', # A type of CPFSK
    'GMSK': 'Gaussian Minimum-Shift Keying',
    'C4FM': '4-level FSK Technology', # Introduced by Yaesu
    'FSK-CW': 'Frequency-Shift Keying Continuous Wave',
    'IFK': 'Incremental Frequency Keying',
    'PSK': 'Phase-Shift Keying',
    'BPSK': 'Binary Phase-Shift Keying',
    'QPSK': 'Quadrature Phase-Shift Keying',
    'OQPSK': 'Offset Quadrature Phase-Shift Keying',
    'DPSK': 'Differential Phase-Shift Keying',
    'SDPSK': 'Symmetric Differential Phase-Shift Keying',
    'DQPSK': 'Differential Quadrature Phase-Shift Keying',
    'D8PSK': 'Differential 8-Phase-Shift Keying',
    'M-ary PSK': 'M-ary Phase-Shift Keying',
    'APSK': 'Amplitude Phase-Shift Keying', # Hybrid ASK and PSK
    'QAM': 'Quadrature Amplitude Modulation', # Hybrid ASK and PSK
    'TCM': 'Trellis Coded Modulation', # Modulation + Coding

    # Pulse Modulation
    'PCM': 'Pulse Code Modulation',
    'PFM': 'Pulse Frequency Modulation',
    'DPCM': 'Differential Pulse Code Modulation',
    'ADPCM': 'Adaptive Differential Pulse Code Modulation',
    'DM': 'Delta Modulation',
    'ADM': 'Adaptive Delta Modulation',
    'CVSDM': 'Continuously Variable Slope Delta Modulation',
    'ΣΔ': 'Sigma-Delta Modulation', # Corrected name order, kept key
    'PAM': 'Pulse Amplitude Modulation',
    'PAM4': '4-Level Pulse Amplitude Modulation',
    'PWM': 'Pulse Width Modulation', # Often synonymous with PDM/PLM
    'PPM': 'Pulse Position Modulation',
    'PDM': 'Pulse Duration Modulation', # Often synonymous with PWM/PLM
    'PLM': 'Pulse Length Modulation', # Often synonymous with PWM/PDM
    'Pulse': 'Undisclosed Pulse Modulation',

    # Spread Spectrum & Advanced Techniques
    'CW': 'Continuous Wave', # Often baseline for other modulations like OOK
    'CSS': 'Chirp Spread Spectrum',
    'LFM': 'Linear Frequency Modulation', # Type of chirp
    'FMCW': 'Frequency-Modulated Continuous Wave', # Often used in Radar
    'DSSS': 'Direct Sequence Spread Spectrum',
    'FHSS': 'Frequency Hopping Spread Spectrum',
    'THSS': 'Time Hopping Spread Spectrum',
    'BOC': 'Binary Offset Carrier Modulation', # Used in GNSS
    'IM/DD': 'Intensity Modulation with Direct Detection', # Optical only

    # Multiplexing / Multiple Access / Carrier Schemes
    'FDM': 'Frequency-Division Multiplexing',
    'OFDM': 'Orthogonal Frequency-Division Multiplexing',
    'DMT': 'Discrete Multitone', # Often used with/as OFDM (e.g., in DSL)
    'FBMC': 'Filter Bank Multi-Carrier',
    'UFMC': 'Universal Filtered Multi-Carrier',
    'OTFS': 'Orthogonal Time Frequency Space',
    'TDMA': 'Time-Division Multiple Access',
    'CDMA': 'Code-Division Multiple Access',
    'NOMA': 'Non-Orthogonal Multiple Access',

    # Pulse Shaping / Modulation on Pulse (Less common stand-alone terms)
    'FMOP': 'Frequency Modulation on Pulse',
    'PMOP': 'Phase Modulation on Pulse',
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
