""" Sqlite connection class """

import sys
import sqlite3
from sqlite3 import OperationalError, DatabaseError
from database.config import SQLITEDB_PATH
from logger import logger
from base.constants import General


class SqliteDb(object):

    # TODO: Add in memory DB support
    def __init__(self):
        try:
            self.connection = sqlite3.connect(SQLITEDB_PATH)
        except OperationalError:
            logger.warning(f'Cannot find database {SQLITEDB_PATH}')
            sys.exit(General.CRASHED)


    def connect(self):
        self.cursor = self.connection.cursor()


    def execute(self, statement: str, commit=False, get=False):
        try:
            self.cursor.execute(statement)
        except DatabaseError as e:
            logger.debug(statement)
            logger.error(e)
            return False

        if commit:
                self.connection.commit()
                return True

        if get:
            ouput = self.cursor.fetchall()
            return ouput


    def execute_script(self, source: list):
        pass


    def close(self):
        self.cursor.close()
