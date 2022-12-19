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


    def create_db(self, name: str) -> None:
        pass


    def create_table(self, name) -> None:
        pass


    def insert_value(self) -> None:
        pass


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
