""" Console window for the cli """

from cli import core
from base.constants import Activity, General
from logger import logger


def repl():
    while True:
        try:
            user_input = int(input(' XXXChange ==> '))
            match user_input:
                case Activity.DAILYTRACKING:
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