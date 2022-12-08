""" Connect to the database driver """


class DatabaseDriver(object):
    _dbinstance = None

    def __new__(cls):
        if cls._dbinstance is None:
            cls._dbinstance = super().__new__(cls)
        return cls._dbinstance


def connect(driver: str = 'mysql'):
    return DatabaseDriver()
