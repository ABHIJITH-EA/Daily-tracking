""" API for budget tracking activities """

from database import connector

class BudgetTracking:
    
    table = 'budget_tracking'

    def __init__(self) -> None:
        self.mysql_db = connector.connect(driver='mysql')

    
    def get_id(self, day:str):
        pass