""" """

from database.driver.mysql import MysqlDb
from database import connector
from base.datetime_utils import to_db_datetime, current_datetime

class MonthPlanModel:

    __table = 'month_plan'
    __start_date = 'start_date'
    __end_date = 'end_date'
    __goal = 'goal'
    __status = 'status'
    __created_at = 'created_at'
    __updated_at = 'updated_at'
    __deleted_at = 'deleted_at'
    __created_by = 'created_by'
    __updated_by = 'updated_by'
    __deleated_by = 'deleated_by'

    def __init__(self):
        self.mysql_db:MysqlDb = connector.connect(driver='mysql')


    def save_month_plan(self, values: list):
        columns = [MonthPlanModel.__start_date, MonthPlanModel.__end_date, MonthPlanModel.__goal,
                MonthPlanModel.__created_at, MonthPlanModel.__updated_at]
        
        created_at = updated_at = to_db_datetime(current_datetime())

        values.append(created_at)
        values.append(updated_at)

        return self.mysql_db.insert_value(MonthPlanModel.__table, columns, values)