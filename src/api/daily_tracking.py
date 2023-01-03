""" API for daily tracking activties """

from database import connector
from base.datetime_utils import current_datetime, to_db_datetime, to_db_time, to_db_date
from api.validations.daily_tracking import DailyTrackingValidation
from database.models.daily_tracking import DailyTrackingModel

from logger import logger


class DailyTracking:
    
    table = 'daily_tracking'

    def __init__(self):
        self.mysql_db = connector.connect(driver='mysql')
        self.validation = DailyTrackingValidation()
        self.model = DailyTrackingModel()

    # TODO: interface with model class
    def save_tracking_data(self, data:list) -> None:
        columns = ['day', 'wakeup_time', 'sleepy_time', 'created_at', 'updated_at']
        
        created_at = updated_at = to_db_datetime(current_datetime())
        
        fmt = '%I:%M %p'
        
        if not self.validation.ispropertime(data[1]):
            logger.error('Invalid time format')
            return False

        wakeup_time = to_db_time(data[1], fmt)
        # sleepy_time = to_db_time(data[2], fmt)
        sleepy_time = to_db_datetime(data[2])
        day = to_db_date(data[0])

        values = [day, wakeup_time, sleepy_time, created_at, updated_at]
        result = self.mysql_db.insert_value(table = DailyTracking.table,
                        columns = columns, values = values)
        
        if not result:
            logger.info('Failed to save daily tracking data')
            return False
        else:
            logger.info('Daily tracking data saved successfully')
            return True


    def update_wakeup_time(self, wake_time: str) -> None:
        pass


    def update_sleepy_time(self, sleepy_time: str) -> None:
        pass

    
    def show_daily_tracking_data(self, start: int = 1, end: int = 10):
        return self.model.list_data(start, end)