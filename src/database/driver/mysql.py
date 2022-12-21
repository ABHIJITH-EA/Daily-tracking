""" Mysql connection class"""

import sys
import mysql.connector
from database.config import get_mysql_config
from logger import logger
from base.constants import General


class MysqlDb(object):

    def __init__(self):
        self.config = get_mysql_config()

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
        pass

    def create_db(self, name: str) -> None:
        pass


    def create_table(self, name) -> None:
        pass


    # TODO: multi-value insertation
    # TODO: Review code
    def insert_value(self, table: str, columns: tuple, values: tuple) -> None:
        columns = ','.join(columns)
        sub_values = ','.join(['%s'] * len(values))
        # values = ','.join(values)

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
