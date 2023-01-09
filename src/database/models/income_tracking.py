
from database.models.budget_tracking import BudgetTrackingModel
from base.datetime_utils import to_db_date, current_date, to_db_datetime, current_datetime

class IncomeTrackingModel(BudgetTrackingModel):
    __table = 'income'

    _id = 'id'
    __budgeting_id = 'budgeting_id'
    __amount = 'amount'
    __remarks = 'remarks'
    __created_at = 'created_at'
    __updated_at = 'updated_at'
    __deleted_at = 'deleted_at'
    __created_by = 'created_by'
    __updated_by = 'updated_by'
    __deleated_by = 'deleated_by'


    def __init__(self) -> None:
        super().__init__()


    def save(self, amount: int, remarks: str):
        """ Save the income details of the day
        """
        day  = to_db_date(current_date())
        columns = self._all_columns()
        budgeting_id = super().get_id(day)
        created_at = updated_at = to_db_datetime(current_datetime())

        values = [budgeting_id, amount, remarks, created_at, updated_at]

        status = self.mysql_db.insert_value(self.__table, columns, values)

        return status


    def list_data(self, start: int, end: int):
        columns = [IncomeTrackingModel.__amount, IncomeTrackingModel.__remarks]
        return self.mysql_db.select(IncomeTrackingModel.__table, columns, end)


    def _all_columns(self) -> list:
        """ Get all the attributes of the table
        """
        columns = [self.__budgeting_id, self.__amount, self.__remarks,
                    self.__created_at, self.__updated_at]

        return columns