
import pool

class IncomeTrackingController:
    
    def __init__(self) -> None:
        pass


    def save(self, data: list):
        return pool.income_tracking_api.save_income_data(data)