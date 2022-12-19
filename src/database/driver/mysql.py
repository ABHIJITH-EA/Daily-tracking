""" Mysql connection class"""

import sys
import mysql.connector
from mysql.connector import Error
from database.config import get_mysql_config
from logger import logger
from base.constants import General


class MysqlDb(object):

    def __init__(self):
        self.config = get_mysql_config()


    def connect(self):
        try:
            self.connection = mysql.connector.connect(**self.config)
        except Error as e:
            logger.error(e)
            sys.exit(General.CRASHED)
        
        return self.connection


    def close(self):
        self.connection.close()

    def create_db(self, name: str) -> None:
        pass

    def create_table(self, name) -> None:
        pass
    def insert_value(self) -> None:
        pass
