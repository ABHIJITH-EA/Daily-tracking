""" Console window for the cli """

from cli import core
from base.constants import Activity, General, System
from logger import logger
from api import daily_tracking, budgeting

def repl():
    while True:
        try:
            user_input = int(input(System.APP_NAME.value))
            match user_input:
                case Activity.DAILY_TRACKING:
                    pass
                case Activity.BUDGETING:
                    pass
                case General.EXIT:
                    pass
                case _:
                    pass
        except ValueError as e:
            logger.error(e)


def init():
    core.banner()
    core.application_menu()

    repl()

    # core.debugger()
