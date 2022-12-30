""" """

from api.validations.budget_tracking import BudgetTrackingValidation


class IncomeTrackingValidation(BudgetTrackingValidation):
    
    def __init__(self) -> None:
        super().__init__()