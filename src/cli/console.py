""" Console window for the cli """

import sys
import time
from datetime import date
from cli import core
from base.constants import Activity, General, System
from logger import logger
from api import daily_tracking, budget_tracking


def log_message(msg: str):
    log_time = time.strftime('%H:%M:%S')
    log_text = f'[{log_time}] [INFO] {msg}'
    align_length = len(log_text) + System.SECONDARY_LEFT_ALIGN.value
    print(log_text.rjust(0))


def menu_printer(text: str) -> None:
    align_size = System.SECONDARY_LEFT_ALIGN.value \
                + System.CONSOLE_MENU_ALIGN_SIZE.value
    if len(text) > align_size:
        align_size = len(text) \
                    + System.CONSOLE_MENU_ALIGN_SIZE.value
    print(f'{text}'.rjust(align_size))


def menu_header(header: str):
    today = date.today()
    day = date(today.year, today.month, today.day)
    tracking_date = day.strftime('%A %d %B %Y')
    lines = '-'*len(header)
    menu_printer(header)
    menu_printer(lines)
    menu_printer(tracking_date)


def daily_tracking_menu():
    menu_header('Daily tracking')
    menu_printer('wake up time? ')
    menu_printer('time went to sleep? ')
    log_message('ACTIVITY RECORDED AT (0.03 sec)')

def budget_tracking_menu():
    pass


def repl():
    while True:
        try:
            user_input = int(input(System.APP_NAME.value))
            match user_input:
                case Activity.DAILY_TRACKING:
                    daily_tracking_menu()
                case Activity.BUDGETING:
                    budget_tracking_menu()
                case General.EXIT:
                    log_message('EXITING')
                    sys.exit(0)
                case _:
                    pass
        except ValueError as e:
            logger.error(e)


def init():
    core.banner()
    core.application_menu()

    repl()

    # core.debugger()
