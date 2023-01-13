""" """

from api.wakeup_time_backup import WakeupTimeBackup
from api.validations.daily_tracking import DailyTrackingValidation
from logger import logger


class WakeupTimeBackupController:

    def __init__(self) -> None:
        self.validation = DailyTrackingValidation()
        self.api = WakeupTimeBackup()

    # TODO: Make return properly
    def save_wakeup_time(self, time: str):

        if not self.validation.ispropertime(time):
            logger.error('Invalid time')

            return False

        status = self.api.save_data(time)

        return status