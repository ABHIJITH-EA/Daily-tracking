""" Mysql connection class"""

import sys
import mysql.connector
from database.config import get_mysql_config
from logger import logger
from base.constants import General


class WhereCondition:

    def __init__(self, statement:str):
        self.statement = statement


    def and_cond(self, column: str, value: str):
        try:
            self.statement += f" AND {column} = {value}"
        except TypeError as e:
            logger.error(f'invalid data type of {value}')
            return None

        return WhereCondition(self.statement)

    def or_cond(self, column: str, value: str):
        try:
            self.statement += f" OR {column} = {value}"
        except TypeError as e:
            logger.error(f'invalid data type of {value}')
            return None

        return WhereCondition(self.statement)


    # TODO: Remove hardcoding `;`
    def create(self):
        self.statement += ';'
        return self.statement


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
        self.cursor = self.connection.cursor(buffered=True)


    def close(self):
        self.connection.close()


    def execute(self, statement):
        try:
            self.cursor.execute(statement)
            return True
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
        if not self.execute(statement):
            return None
        return self.cursor.fetchmany(limit)


    def select_where(self, table:str, columns: str, where_colum: str, value: str) -> WhereCondition:
        columns = ','.join(columns)
        statement = f"SELECT {columns} FROM {table} WHERE {where_colum} = '{value}'"

        return WhereCondition(statement=statement)


    # TODO: Remove hardcoding `;`
    def execute_select_where(self, statement: str, limit: int = None):
        # Checking default limit changed or not
        limit = self.limit if limit is None else limit

        if not self.execute(statement=statement):
            return None
        return self.cursor.fetchmany(limit)


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


    def delete_query(self, table: str, where_column: str, value):
        statement = f"DELETE FROM {table} WHERE {where_column} = '{value}'"

        return WhereCondition(statement)


    def delete_row(self, statement: str):
        if not self.execute(statement):
            return False
        self.connection.commit()
        return True


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