""" API for daily tracking activties """

from database.connect import connect

class DailyTracking:
    
    def __init__(self):
        mysql_db = connect('mysql')
        sqlite_db = connect('sqlite')

    def save_tracking_data(self, data:list) -> None:
        pass

    def update_wakeup_time(self) -> None:
        pass

    def update_sleepy_time(self) -> None:
        pass