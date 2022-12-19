""" Application database initilizer and utility function """

from database.connector import connect

class AppInitializer:

    def __init__(self) -> None:
        self.db = connect('sqlite')


    def check_database_status(self):
        pass


    def create_mysql_tables(sql_stms: list):
        mysql_db = connect('mysql')
        mysql_db.execute_script(sql_stms)