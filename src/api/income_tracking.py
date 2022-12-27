
from api.budget_tracking import BudgetTracking
from database.models.income_tracking import IncomeTrackingModel
from api.validations.budget_tracking import BudgetTrackingValidation


class IncomeTracking(BudgetTracking):
    
    def __init__(self) -> None:
        super().__init__()
        # NOTE: Work around for java type inheritance
        # Have to change later in a pythonic way.
        self._super = BudgetTracking()
        self.model = IncomeTrackingModel()


    def save_income_data(self, data: list):
        if BudgetTrackingValidation.is_firsttime_today():
            if not self._super.create_budgettracking_data():
                return None

        amnt = data[0]
        remarks = data[1]

        result = self.model.save(amount=amnt, remarks=remarks)

        return False if not result else True