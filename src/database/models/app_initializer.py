""" Application database initilizer and utility function """

from database.connector import connect
from logger import logger
from base import sqlite_queries


class AppInitializer:

    def __init__(self) -> None:
        self.db = connect('sqlite')


    def check_database_status(self):
        sqlite_db = connect('sqlite')
        query_output = sqlite_db.execute(sqlite_queries.APP_DB_TABLE_STATUS_SELECT,\
                                        get=True)
        if len(query_output) != 0:
            status = query_output.pop()[0]
            if status != 'ACTIVE':
                return None

        return True        


    def create_mysql_tables(sql_stms: list) -> bool:
        mysql_db = connect('mysql')

        if mysql_db.execute_script(sql_stms):
            logger.info('Application datbase initialized')
            AppInitializer.set_app_database_status()
            return True
        else:
            logger.info('Failed to set application database')
            return False


    def set_app_database_status() -> None:
        sqlite_db = connect('sqlite')

        sqlite_db.execute(sqlite_queries.APP_DB_TABLE_ACTIVATE, commit=True)
