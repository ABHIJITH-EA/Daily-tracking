""" Connect to the database driver """

from database.driver import mysql

class _DatabaseDriver(mysql.MysqlDb):
    _dbinstance = None

    def __new__(cls, driver):
        if cls._dbinstance is None:
            cls._dbinstance = super().__new__(cls)
        return cls._dbinstance


def connect(driver: str = 'mysql'):
    return _DatabaseDriver(driver)
