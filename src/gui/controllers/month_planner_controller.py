""" """

import pool

class MonthPlannerController:

    def __init__(self) -> None:
        pass


    def save(self, data: list):
        return pool.month_planner_api.save_month_planner_data(data)