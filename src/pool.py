""" Active instances of API's """

from api.daily_tracking import DailyTracking
from api.budget_tracking import BudgetTracking
from api.spent_tracking import SpentTracking
from api.income_tracking import IncomeTracking
from api.week_planner import WeekPlanner
from api.month_planner import MonthPlanner

daily_tracking_api = None
budget_tracking_api = None
income_tracking_api = None
spent_tracking_api = None
week_planner_api = None
month_planner_api = None

_API_CONNECTION_STATUS = False

def _get_daily_tracking_api_instance() -> DailyTracking:
    return DailyTracking()


def _get_budget_tracking_api_instance() -> BudgetTracking:
    return BudgetTracking()


def _get_spent_tracking_api() -> SpentTracking:
    return SpentTracking()


def _get_income_tracking_api() -> IncomeTracking:
    return IncomeTracking()


def _get_week_planner_api() -> WeekPlanner:
    return WeekPlanner()


def _get_month_planner_api() -> MonthPlanner:
    return MonthPlanner()


def activate() -> None:
    global daily_tracking_api,\
            budget_tracking_api, income_tracking_api,\
            spent_tracking_api, week_planner_api,\
            month_planner_api
    
    global _API_CONNECTION_STATUS

    try:
        daily_tracking_api = _get_daily_tracking_api_instance()
        budget_tracking_api = _get_budget_tracking_api_instance()
        income_tracking_api = _get_income_tracking_api()
        spent_tracking_api = _get_spent_tracking_api()
        month_planner_api = _get_month_planner_api()
        week_planner_api = _get_week_planner_api()
        _API_CONNECTION_STATUS = True
    except Exception:
        _API_CONNECTION_STATUS = False


def check_status() -> bool:
    if not _API_CONNECTION_STATUS:
        return False

    return True
    