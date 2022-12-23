""" Mysql connection class"""

import sys
import mysql.connector
from database.config import get_mysql_config
from logger import logger
from base.constants import General


class MysqlDb(object):

    def __init__(self, limit: int = 10):
        self.config = get_mysql_config()
        self.limit = limit
        try:
            self.connection = mysql.connector.connect(**self.config)
            self.connection.autocommit = False
        except mysql.connector.Error as e:
            logger.error(e)
            sys.exit(General.CRASHED)


    def connect(self):
        self.cursor = self.connection.cursor()


    def close(self):
        self.connection.close()


    def execute(self, statement):
        try:
            self.cursor.execute(statement)
        except mysql.connector.Error as e:
            logger.error(e)
            return False

    def create_db(self, name: str) -> None:
        pass


    def create_table(self, name) -> None:
        pass


    def select(self, table:str, columns: list, limit:int = None):
        columns = ','.join(columns)
        statement = f"SELECT {columns} FROM {table};"
        
        # Checking default limit changed or not
        limit = self.limit if limit is None else limit
        
        try:
            self.cursor.execute(statement)
            return self.cursor.fetchmany(limit)
        except mysql.connector.Error as e:
            logger.error(e)
            return None


    # TODO: multi-value insertation
    # TODO: Review code
    def insert_value(self, table: str, columns: list, values: list) -> None:
        columns = ','.join(columns)
        sub_values = ','.join(['%s'] * len(values))

        statement = f"INSERT INTO {table} ({columns}) VALUES ({sub_values});"
        try:
            self.cursor.execute(statement, values)
            self.connection.commit()
            return True
        except mysql.connector.Error as e:
            logger.error(e)
            return False


    def execute_script(self, statments: list) -> bool:
        try:
            for stm in statments:
                self.cursor.execute(stm)
            self.connection.commit()
            return True
        except mysql.connector.Error as e:
            self.connection.rollback()
            logger.error(e)
            return False

    
    # BUG: Not accounting for the `execute` failure scenario
    def first_row(self):
        return self.cursor.fetchone()