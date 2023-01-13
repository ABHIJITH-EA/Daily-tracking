""" """

from database.driver.mysql import MysqlDb
from database import connector
from base.datetime_utils import to_db_datetime, current_datetime

class WeekPlanModel:

    __table = 'week_plan'
    __month_id = 'month_id'
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


    def save_week_plan(self, values: list):
        columns = [WeekPlanModel.__month_id, WeekPlanModel.__start_date, WeekPlanModel.__end_date, WeekPlanModel.__goal,
                WeekPlanModel.__created_at, WeekPlanModel.__updated_at]

        created_at = updated_at = to_db_datetime(current_datetime())
        values.append(created_at)
        values.append(updated_at)

        return self.mysql_db.insert_value(WeekPlanModel.__table, columns, values)


    def get_data_with_month_id(self, id: int):
        columns = [WeekPlanModel.__start_date, WeekPlanModel.__end_date, WeekPlanModel.__goal,
                WeekPlanModel.__status]

        statement = self.mysql_db.select_where(WeekPlanModel.__table, columns, WeekPlanModel.__month_id, id).create()

        return self.mysql_db.execute_select_where(statement)