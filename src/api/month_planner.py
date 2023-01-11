""" """

from api.validations.month_planner_validation import MonthPlannerValidation
from database.models.month_plan_model import MonthPlanModel
from base.datetime_utils import to_db_date
from logger import logger

class MonthPlanner():
    
    def __init__(self) -> None:
        self.validation = MonthPlannerValidation()
        self.model = MonthPlanModel()


    def save_month_planner_data(self, data: list):
        start_date = to_db_date(data[0])
        end_date = to_db_date(data[1])
        goal = data[2]

        values = [start_date, end_date, goal]

        result = self.model.save_month_plan(values)

        if not result:
            logger.info('Failed to save month planner data')
            return False
        else:
            logger.info('Month planner data saved')
            return True


    def get_id(self):
        """ Get current month id
            :return int
        """
        pass