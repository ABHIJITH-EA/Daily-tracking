""" """

from database import connector
from database.driver.sqlite import SqliteDb


class WakeupTimeBackupModel:

    __table = 'wakeup_time_backup'
    __time = 'time'
    __day = 'day'

    def __init__(self) -> None:
        self.sqlite_db:SqliteDb = connector.connect(driver='sqlite')

    
    def save(self, values:list):
        columns = ','.join([WakeupTimeBackupModel.__time, WakeupTimeBackupModel.__day])
        sub_values = ','.join(['%r'] * len(values))

        statement = f"INSERT INTO {WakeupTimeBackupModel.__table} ({columns}) VALUES ({sub_values});"
        return self.sqlite_db.execute((statement % tuple(values)), True)
