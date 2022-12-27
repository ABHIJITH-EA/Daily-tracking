
from database import connector
from database.driver.mysql import MysqlDb
from base.datetime_utils import current_date, current_datetime, to_db_datetime, to_db_date
from logger import logger


class BudgetTrackingModel:
    
    __table = 'budget_tracking'

    __id = 'id'
    __day = 'day'
    __created_at = 'created_at'
    __updated_at = 'updated_at'
    __deleted_at = 'deleted_at'
    __created_by = 'created_by'
    __updated_by = 'updated_by'
    __deleated_by = 'deleated_by'


    def __init__(self) -> None:
        self.mysql_db:MysqlDb = connector.connect(driver='mysql')


    # TODO: Code review, params
    def get_id(self, day:str):
        colums = [self.__id]
        where_column = self.__day

        statement = self.mysql_db.select_where(self.__table, colums, where_column, day).create()

        try:
            budget_id = self.mysql_db.execute_select_where(statement)[0][0]
        except IndexError as e:
            logger.error(e)
            budget_id = None

        return budget_id

    def save(self):
        day = to_db_date(current_date())

        columns = [self.__day, self.__created_at, self.__updated_at]

        created_at = updated_at =  to_db_datetime(current_datetime())

        values = [day, created_at, updated_at]

        status = self.mysql_db.insert_value(self.__table, columns, values)

        return status