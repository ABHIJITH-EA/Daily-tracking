""" """
from api.validations.budget_tracking import BudgetTrackingValidation


class SpentTrackingValidation(BudgetTrackingValidation):

    def __init__(self) -> None:
        super().__init__()