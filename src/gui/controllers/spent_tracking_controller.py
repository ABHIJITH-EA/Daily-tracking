
import pool

class SpentTrackingController:

    def __init__(self):
        pass


    def save(self, data: list):
        return pool.spent_tracking_api.save_spent_data(data)