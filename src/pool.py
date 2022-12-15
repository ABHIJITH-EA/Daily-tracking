""" Active instances of API's """

from api.daily_tracking import DailyTracking
from api.budget_tracking import BudgetTracking

daily_tracking_api = None
budget_tracking_api = None


def _get_daily_tracking_api_instance() -> DailyTracking:
    return DailyTracking()


def _get_budget_tracking_api_instance() -> BudgetTracking:
    return BudgetTracking()


def activate() -> None:
    global daily_tracking_api,\
            budget_tracking_api

    daily_tracking_api = _get_daily_tracking_api_instance()
    budget_tracking_api = _get_budget_tracking_api_instance()


def check_status() -> bool:
    if not daily_tracking_api or not budget_tracking_api:
        return False

    return True
    