import sqlite3
from contextlib import closing
from utils.constants import Query, Path


class Database():
    """ General superclass for SQLite DB manipulation.
        Supports both isolated single executions and long-lived transactions.
        Foreign keys are activated (otherwise disabled by default for compatibility purposes).
    """
    def __init__(self, sql_path):
        self.sql_path = sql_path
        self._shared_conn = None  # Holds a connection during a transaction block


    def begin_transaction(self):
        """ Opens a long-lived connection and begins a transaction block. """
        if self._shared_conn is None:
            self._shared_conn = sqlite3.connect(self.sql_path, check_same_thread=False)
            self._shared_conn.execute('PRAGMA foreign_keys = ON;')
            self._shared_conn.execute('PRAGMA secure_delete = ON;')
            self._shared_conn.execute('BEGIN TRANSACTION;')


    def commit_transaction(self):
        """ Commits the active transaction and closes the shared connection. """
        if self._shared_conn:
            self._shared_conn.commit()
            self._shared_conn.close()
            self._shared_conn = None


    def rollback_transaction(self):
        """ Rolls back the active transaction in case of an error and closes it. """
        if self._shared_conn:
            self._shared_conn.rollback()
            self._shared_conn.close()
            self._shared_conn = None


    def execute(self, query, parameters=None, last_rowid=False):
        """ Executes a query. If inside a transaction, uses the shared connection.
            Otherwise, safely opens, commits, and closes an isolated connection.
        """
        # Scenario A: We are inside a transaction block (Batch processing)
        if self._shared_conn is not None:
            curs = self._shared_conn.cursor()
            if parameters:
                curs.execute(query, parameters)
            else:
                curs.execute(query)
            
            return curs.lastrowid if last_rowid else curs.fetchall()

        # Scenario B: Single independent query execution (Standard fallback)
        with closing(sqlite3.connect(self.sql_path, check_same_thread=False)) as conn:
            conn.execute('PRAGMA foreign_keys = ON;')
            conn.execute('PRAGMA secure_delete = ON;')

            curs = conn.cursor()
            if parameters:
                curs.execute(query, parameters)
            else:
                curs.execute(query)

            conn.commit()
            return curs.lastrowid if last_rowid else curs.fetchall()


class ArtemisDB(Database):
    """ Class of the main Artemis database. Inherits from the Database superclass """

    def __init__(self, db_name):
        sql_path = Path.DATA_DIR / "{}.sqlite".format(db_name)
        super().__init__(sql_path)   

    def create_db(self):
        """ Creates all tables and views wrapped inside a safe setup transaction """
        self.begin_transaction()
        try:
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
            self.commit_transaction()
        except Exception as e:
            self.rollback_transaction()
            raise e


    def add_signal(self, name, description, url):
        return self.execute(Query.INSERT_SIGNAL, [name, description, url], True)

    def add_category(self, sig_id, clb_id):
        self.execute(Query.INSERT_CATEGORY, [sig_id, clb_id])


    def add_category_label(self, value):
        return self.execute(Query.INSERT_CATEGORY_LABEL, [value], True)


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
        return self.execute(Query.INSERT_DOCUMENTS, [extension, sig_id, name, description, type, preview], True)


    def sign_db(self, name, date, version, editable):
        self.execute(Query.INSERT_INFO, [name, date, version, editable])

    ######################## Post-process only

    def select_all_modulation(self):
        return self.execute(Query.SELECT_ALL_MODULATION)


    def update_modulation(self, mdl_id, value, description):
        self.execute(Query.UPDATE_MODULATION, [value, description, mdl_id])
