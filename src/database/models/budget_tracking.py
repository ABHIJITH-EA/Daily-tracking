
from database import connector
from database.driver.mysql import MysqlDb

class BudgetTrackingModel:
    
    _table = 'budget_tracking'

    _id = 'id'
    _day = 'day'
    _created_at = 'created_at'
    _updated_at = 'updated_at'
    _deleted_at = 'deleted_at'
    _created_by = 'created_by'
    _updated_by = 'updated_by'
    _deleated_by = 'deleated_by'


    def __init__(self) -> None:
        self.mysql_db:MysqlDb = connector.connect(driver='mysql')


    # TODO: Code review, params
    def get_id(self, day:str):
        colums = [self._id]
        where_column = self._day

        statement = self.mysql_db.select_where(self._table, colums, where_column, day).create()

        budget_id = self.mysql_db.execute_select_where(statement)

        return budget_id