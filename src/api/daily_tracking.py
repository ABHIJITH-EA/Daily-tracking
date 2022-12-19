""" API for daily tracking activties """

from database import connector

class DailyTracking:
    
    def __init__(self):
        self.connect = connector.connect(driver='mysql')

    def save_tracking_data(self, data:list) -> None:
        pass

    def update_wakeup_time(self) -> None:
        pass

    def update_sleepy_time(self) -> None:
        pass