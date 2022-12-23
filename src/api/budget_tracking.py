""" API for budget tracking activities """

from database.models.budget_tracking import BudgetTrackingModel

class BudgetTracking:

    def __init__(self) -> None:
        self.model = BudgetTrackingModel()

    
    def get_budgettracking_id(self, day:str) -> int:
        
        return self.model.get_id(day)


    def create_budgettracking_data(self):
        self.model.save()