""" """

from database.models.wakeup_time_backup_model import WakeupTimeBackupModel
from base.datetime_utils import  to_db_date, to_db_time, current_date
from logger import logger

class WakeupTimeBackup:

    def __init__(self) -> None:
        self.model = WakeupTimeBackupModel()

    
    def save_data(self, time:str):
        data = []
        time = to_db_time(time)
        day = to_db_date(current_date())
        data.append(time)
        data.append(day)
        status = self.model.save(data)

        if status:
            logger.info('Wakeup time backup succefull')
        else:
            logger.info('Failed to backup wakeup time')

        return status
