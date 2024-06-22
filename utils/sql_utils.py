import sqlite3

from utils.constants import Query, Path
from contextlib import closing


class Database():
    """ General superclass for SQLite DB manipulation.
        Foreign keys are activated (otherwise disabled by default for compatibility purposes)
    """
    def __init__(self, sql_path):
        self.sql_path = sql_path

    def execute(self, query, parameters=None, last_rowid=False):
        """ Open a connection, execute the given query with optional parameters and close the connection. 
            In the case of a SELECT query, returns the results as a fetchall().
            If last_rowid == True, this function returns a tuple with the result of the fetchall() and
            the latest modified row id of the current connection.
        """
        with closing(sqlite3.connect(self.sql_path, check_same_thread=False)) as conn:
            conn.execute('PRAGMA foreign_keys = ON;')
            conn.execute('PRAGMA secure_delete = ON;')

            curs = conn.cursor()

            if parameters:
                curs.execute(query, parameters)
            else:
                curs.execute(query)

            conn.commit()

            if last_rowid:
                return curs.lastrowid
            else:
                return curs.fetchall()


class ArtemisDB(Database):
    """ Class of the main Artemis database. Inherits from the Database superclass
    """

    def __init__(self, db_name):
        sql_path = Path.DATA_DIR / "{}.sqlite".format(db_name)
        super().__init__(sql_path)   

    def create_db(self):
        self.execute(Query.CREATE_SIGNALS)
        self.execute(Query.CREATE_CATEGORY)
        self.execute(Query.CREATE_CATEGORY_LABELS)
        self.execute(Query.CREATE_FREQUENCY)
        self.execute(Query.CREATE_BANDWIDTH)
        self.execute(Query.CREATE_MODULATION)
        self.execute(Query.CREATE_MODE)
        self.execute(Query.CREATE_LOCATION)
        self.execute(Query.CREATE_ACF)
        self.execute(Query.CREATE_DOCUMENTS)
        self.execute(Query.CREATE_INFO)

        self.execute(Query.CREATE_VIEW_FREQ)
        self.execute(Query.CREATE_VIEW_BAND)

    def add_signal(self, name, description, url):
        last_row = self.execute(Query.INSERT_SIGNAL, [name, description, url], True)
        return last_row

    def add_category(self, sig_id, clb_id):
        self.execute(Query.INSERT_CATEGORY, [sig_id, clb_id])

    def add_category_label(self, value):
        last_row = self.execute(Query.INSERT_CATEGORY_LABEL, [value], True)
        return last_row

    def add_frequency(self, sig_id, value, description):
        self.execute(Query.INSERT_FREQUENCY, [sig_id, value, description])

    def add_bandwidth(self, sig_id, value, description):
        self.execute(Query.INSERT_BANDWIDTH, [sig_id, value, description])

    def add_modulation(self, sig_id, value, description):
        self.execute(Query.INSERT_MODULATION, [sig_id, value, description])

    def add_mode(self, sig_id, value, description):
        self.execute(Query.INSERT_MODE, [sig_id, value, description])

    def add_location(self, sig_id, value, description):
        self.execute(Query.INSERT_LOCATION, [sig_id, value, description])

    def add_acf(self, sig_id, value, description):
        self.execute(Query.INSERT_ACF, [sig_id, value, description])

    def add_document(self, extension, sig_id, name, description, type, preview):
        last_row = self.execute(Query.INSERT_DOCUMENTS, [extension, sig_id, name, description, type, preview], True)
        return last_row

    def sign_db(self, name, date, version, editable):
        self.execute(Query.INSERT_INFO, [name, date, version, editable])

######################## Post-process only

    def select_all_modulation(self):
        all_modulation = self.execute(Query.SELECT_ALL_MODULATION)
        return all_modulation

    def update_modulation(self, mdl_id, value, description):
        self.execute(Query.UPDATE_MODULATION, [value, description, mdl_id])
