

from api.budget_tracking import BudgetTracking
from api.validations.spent_tracking_validation import SpentTrackingValidation
from database.models.spent_tracking import SpentTrackingModel

from logger import logger

class SpentTracking(BudgetTracking):
    def __init__(self) -> None:
        super().__init__()
        # NOTE: Work around for java type inheritance
        # Have to change later in a pythonic way.
        self._super = BudgetTracking()
        self.model = SpentTrackingModel()
        self.validation = SpentTrackingValidation()
    

    def save_spent_data(self, data: list):
        if self.validation.is_firsttime_today():
            if not self._super.create_budgettracking_data():
                return None

        if not self.validation.is_proper_data(data):
            return None

        amnt = int(data[0])
        remarks = data[1]

        result = self.model.save(amount=amnt, remarks=remarks)

        if not result:
            logger.info('Spent data saving failed')
            return False 

        logger.info('Spent data saved successfully')
        return True


    def delete_spent_data(self, id: int):
        if not self.model.delete(id):
            logger.info('Spent data delete failed')
            return False

        logger.info('Spent data deleted successfully')
        return True