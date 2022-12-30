
from database.models.budget_tracking import BudgetTrackingModel
from base.datetime_utils import current_date
from base.datetime_utils import to_db_datetime, current_datetime, to_db_date, to_db_datetime


class SpentTrackingModel(BudgetTrackingModel):
    __table = 'spent'

    __id = 'id'
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
        """ Save the spent details of the day
        """
        day  = to_db_date(current_date())
        columns = self._all_columns()
        budgeting_id = super().get_id(day)
        created_at = updated_at = to_db_datetime(current_datetime())

        values = [budgeting_id, amount, remarks, created_at, updated_at]

        status = self.mysql_db.insert_value(self.__table, columns, values)

        return status

    
    def delete(self, id):
        delete_stm = self.mysql_db.delete_query(self.__table, where_column=self.__id, value=id).create()
        status = self.mysql_db.delete_row(delete_stm)

        return status

    def _all_columns(self) -> list:
        """ Get all the attributes of the table
        """
        columns = [self.__budgeting_id, self.__amount, self.__remarks,
                    self.__created_at, self.__updated_at]

        return columns