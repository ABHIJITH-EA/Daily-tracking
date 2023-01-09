
import pool

class SpentTrackingController:

    def __init__(self):
        pass


    def save(self, data: list):
        return pool.spent_tracking_api.save_spent_data(data)


    # TODO: return data as supporting format
    #       eg: send amount as `str` type not as int
    def show_data(self, start: int, end: int):
        return pool.spent_tracking_api.show_spent_tracking_data(start, end)