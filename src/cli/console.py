""" Console window for the cli """

from cli import core
from base.constants import Activity, General, System
from logger import logger
from api import daily_tracking, budgeting
import time

def log_message(msg: str):
    log_time = time.strftime('%H:%M:%S')
    log_text = f'[{log_time}] [INFO] {msg}'
    align_length = len(log_text) + System.SECONDARY_LEFT_ALIGN.value
    print(log_text.rjust(0))


def repl():
    while True:
        try:
            user_input = int(input(System.APP_NAME.value))
            match user_input:
                case Activity.DAILY_TRACKING:
                    log_message('Activity created')
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
