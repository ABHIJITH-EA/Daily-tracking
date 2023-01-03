""" """

import pool
from base.datetime_utils import current_date, to_db_date
from PyQt6.QtCore import QDate
from datetime import datetime
from logger import logger
from api.validations.daily_tracking import DailyTrackingValidation

class DailyTrackingController:

    def __init__(self) -> None:
        self.api_validation = DailyTrackingValidation()


    def save(self, data: list):
        processed_data = []
        tracking_date:QDate = data[0]
        sleepy_time = data[2]
        sleepy_date = data[3].toPyDate().strftime('%d-%m-%Y')

        if not self.api_validation.ispropertime(sleepy_time):
            logger.error('Invalid time format')
            return False
        processed_data.append(tracking_date.toPyDate().strftime('%d-%m-%Y'))
        processed_data.append(data[1])
        sleepy_datetime = sleepy_date + ' ' + sleepy_time
        try:
            dt = datetime.strptime(sleepy_datetime, '%d-%m-%Y %I:%M %p')
            processed_data.append(dt.strftime('%d-%m-%Y %H:%M:%S'))
        except ValueError as e:
            logger.error("Failed to make sleepy datetime")
            return False
            
        return pool.daily_tracking_api.save_tracking_data(processed_data)