

from api.budget_tracking import BudgetTracking
from api.validations.budget_tracking import BudgetTrackingValidation
from database.models.spent_tracking import SpentTrackingModel


class SpentTracking(BudgetTracking):
    def __init__(self) -> None:
        super().__init__()

        self.model = SpentTrackingModel()
    

    def save_spent_data(self, data: list):
        # ?
        if BudgetTrackingValidation.is_firsttime_today():
            pass

        self.model.save()

        amnt = data[0]
        remarks = data[1]

        result = self.model.save(amount=amnt, remarks=remarks)

        return False if not result else True