""" Validations for daily tracking activities """

import datetime
from logger import logger


class DailyTrackingValidation:

    @staticmethod
    def ispropertime(time: str) -> bool:
        fmt = '%I:%M %p'
        try:
            datetime.datetime.strptime(time, fmt)
            return True
        except ValueError as e:
            logger.error(e)
            return False