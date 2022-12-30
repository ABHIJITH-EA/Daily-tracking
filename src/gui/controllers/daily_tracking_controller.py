""" """

import pool
from base.datetime_utils import current_date

class DailyTrackingController:

    def __init__(self) -> None:
        pass


    def save(self, data: list):
        data.insert(0, current_date())
        return pool.daily_tracking_api.save_tracking_data(data)