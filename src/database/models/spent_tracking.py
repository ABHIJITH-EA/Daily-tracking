
from database.models.budget_tracking import BudgetTrackingModel
from base.datetime_utils import current_date
from base.datetime_utils import to_db_datetime, current_datetime, to_db_date, to_db_datetime


class SpentTrackingModel(BudgetTrackingModel):
    table = 'spent'

    _id = 'id'
    _budgeting_id = 'budgeting_id'
    _amount = 'amount'
    _remarks = 'remarks'
    _created_at = 'created_at'
    _updated_at = 'updated_at'
    _deleted_at = 'deleted_at'
    _created_by = 'created_by'
    _updated_by = 'updated_by'
    _deleated_by = 'deleated_by'

    def __init__(self) -> None:
        super().__init__()

    
    def save(self, amount: int, remarks: str):
        """ Save the spent details of the day
        """
        day  = to_db_date(current_date())
        columns = self._all_columns()
        budgeting_id = self.get_id(day)
        created_at = updated_at = to_db_datetime(current_datetime())

        values = [budgeting_id, amount, remarks, created_at, updated_at]

        status = self.mysql_db.insert_value(self._table, columns, values)

        return status


    def _all_columns(self) -> list:
        """ Get all the attributes of the table
        """
        columns = [self._budgeting_id, self._amount, self._remarks,
                    self._created_at, self._updated_at]

        return columns