
from api.budget_tracking import BudgetTracking
from database.models.income_tracking import IncomeTrackingModel
from api.validations.income_tracking_validation import IncomeTrackingValidation

from logger import logger

class IncomeTracking(BudgetTracking):
    
    def __init__(self) -> None:
        super().__init__()
        # NOTE: Work around for java type inheritance
        # Have to change later in a pythonic way.
        self._super = BudgetTracking()
        self.model = IncomeTrackingModel()
        self.validation = IncomeTrackingValidation()


    def save_income_data(self, data: list):
        if self.validation.is_firsttime_today():
            if not self._super.create_budgettracking_data():
                return None

        if not self.validation.is_proper_data(data):
            return None

        amnt = int(data[0])
        remarks = data[1]

        result = self.model.save(amount=amnt, remarks=remarks)

        if not result:
            logger.info('Income data saving failed')
            return False 

        logger.info('Income data saved successfully')
        return True