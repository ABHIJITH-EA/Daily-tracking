""" """

from api.validations.week_planner_validation import WeekPlannerValidation
from database.models.week_plan_model import WeekPlanModel
from api.month_planner import MonthPlanner
from base.datetime_utils import add_date, to_db_date, to_app_date
from logger import logger


class WeekPlanner(MonthPlanner):

    def __init__(self) -> None:
        super().__init__()

        self.validation = WeekPlannerValidation()
        self.model = WeekPlanModel()
        self._super = MonthPlanner()


    def save_week_planner_data(self, data: list):
        month_id = self._super.get_id(data[0].strftime('%d-%m-%Y'))
        if not month_id:
            return False
        start_date = data[0]
        end_date = to_db_date(add_date(start_date, 7))
        goal = data[1]

        values = [month_id, start_date, end_date, goal]
        result = self.model.save_week_plan(values)

        if not result:
            logger.info('Failed to save week planner data')
            return False
        else:
            logger.info('Week planner data saved')
            return True

    
    def get_week_plans(self, month_start_date: str):
        """ Get week plans
            :param start_date: start date of the month
            : return : list
        """
        month_id = self._super.get_id(month_start_date.strftime('%d-%m-%Y'))

        result = self.model.get_data_with_month_id(month_id)

        if not result:
            logger.info('Failed to fetch week plans')
            return False
        
        data = []
        
        for item in result:
            item_list = []

            item_list.append(to_app_date(item[0]))
            item_list.append(to_app_date(item[1]))
            item_list.append(item[2])
            item_list.append(item[3])

            data.append(item_list)

        return data
