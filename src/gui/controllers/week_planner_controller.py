import pool

class WeekPlannerController:

    def __init__(self) -> None:
        pass


    def save(self, data: list):
        return pool.week_planner_api.save_week_planner_data(data)


    def show_week_plans(self, start_date):
        return pool.week_planner_api.get_week_plans(start_date)