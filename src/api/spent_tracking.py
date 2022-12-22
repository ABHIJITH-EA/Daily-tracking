

from api.budget_tracking import BudgetTracking
from base.datetime_utils import to_db_datetime, current_datetime
from api.validations.budget_tracking import BudgetTrackingValidation

class SpentTracking(BudgetTracking):
    
    table = 'spent'

    def __init__(self) -> None:
        super().__init__()
    

    def save_spent_data(self, data: list):
        # 'budgeting_id', 
        columns = ['budgeting_id', 'amount', 'remarks', 'created_at', 'updated_at']

        created_at = updated_at = to_db_datetime(current_datetime())

        amnt = data[0]
        remarks = data[1]

        values = [amnt, remarks, created_at, updated_at]

        result = self.mysql_db.insert_value(SpentTracking.table, columns, values)

        return False if not result else True