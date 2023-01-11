""" Daily tracking data model """

from database.driver.mysql import MysqlDb
from database import connector

class DailyTrackingModel:
    __table = 'daily_tracking'

    __id = 'id'
    __day = 'day'
    __wakeup_time = 'wakeup_time'
    __sleepy_time = 'sleepy_time'
    __created_at = 'created_at'
    __updated_at = 'updated_at'
    __deleted_at = 'deleted_at'
    __created_by = 'created_by'
    __updated_by = 'updated_by'
    __deleated_by = 'deleated_by'

    
    def __init__(self):
        self.mysql_db:MysqlDb = connector.connect(driver='mysql')


    def save_tracking_data(self, values: list):
        columns = [DailyTrackingModel.__day, DailyTrackingModel.__wakeup_time, DailyTrackingModel.__sleepy_time,
                    DailyTrackingModel.__created_at, DailyTrackingModel.__updated_at]
        return self.mysql_db.insert_value(DailyTrackingModel.__table, columns, values)


    def list_data(self, start:int, end: int):
        columns = [DailyTrackingModel.__day, DailyTrackingModel.__wakeup_time, DailyTrackingModel.__sleepy_time]
        return self.mysql_db.select(DailyTrackingModel.__table, columns, end)