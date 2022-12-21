""" API for daily tracking activties """

from database import connector
from base.datetime_utils import current_datetime, datetime_to_db

class DailyTracking:
    
    table = 'daily_tracking'

    def __init__(self):
        self.mysql_db = connector.connect(driver='mysql')

    def save_tracking_data(self, data:list) -> None:
        columns = ['day', 'wakeup_time', 'sleepy_time', 'created_at', 'updated_at']
        
        created_at = updated_at = datetime_to_db(current_datetime())

        values = [data[0], data[1], data[2], created_at, updated_at]

        result = self.mysql_db.insert_value(table = DailyTracking.table,
                        columns = columns, values = values)
        
        return False if not result else True

    def update_wakeup_time(self) -> None:
        pass

    def update_sleepy_time(self) -> None:
        pass