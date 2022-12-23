""" API for daily tracking activties """

from database import connector
from base.datetime_utils import current_datetime, to_db_datetime, to_db_time, to_db_date


class DailyTracking:
    
    table = 'daily_tracking'

    def __init__(self):
        self.mysql_db = connector.connect(driver='mysql')

    # TODO: interface with model class
    def save_tracking_data(self, data:list) -> None:
        columns = ['day', 'wakeup_time', 'sleepy_time', 'created_at', 'updated_at']
        
        created_at = updated_at = to_db_datetime(current_datetime())
        
        fmt = '%I:%M %p'

        wakeup_time = to_db_time(data[1], fmt)
        sleepy_time = to_db_time(data[2], fmt)
        day = to_db_date(data[0])

        values = [day, wakeup_time, sleepy_time, created_at, updated_at]
        result = self.mysql_db.insert_value(table = DailyTracking.table,
                        columns = columns, values = values)
        
        return False if not result else True


    def update_wakeup_time(self, wake_time: str) -> None:
        pass


    def update_sleepy_time(self, sleepy_time: str) -> None:
        pass