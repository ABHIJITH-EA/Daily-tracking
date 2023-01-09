
import pool

class IncomeTrackingController:
    
    def __init__(self) -> None:
        pass


    def save(self, data: list):
        return pool.income_tracking_api.save_income_data(data)


    # TODO: return data as supporting format
    #       eg: send amount as `str` type not as int
    def show_data(self, start: int, end: int):
        return pool.income_tracking_api.show_spent_tracking_data(start, end)