""" Console window for the cli """

import sys
import time
from datetime import date
from cli import core, utils
from base.constants import Activity, General, System
from logger import logger
from api.validations.daily_tracking import DailyTrackingValidation
from api.validations.budget_tracking import BudgetTrackingValidation
import pool

# TODO: Fix level ambiguity
def log_message(msg: str, level = 'INFO'):
    log_time = time.strftime('%H:%M:%S')
    log_text = f'[{log_time}] [{level}] {msg}'
    align_length = len(log_text) + System.SECONDARY_LEFT_ALIGN.value
    print(log_text.rjust(0))


def menu_printer(text: str, new_line=False) -> None:
    align_size = utils.aligner(text)
    print(f'{text}'.rjust(align_size))
    if new_line:
        print() 


def menu_header(header: str) -> None:
    today = date.today()
    day = date(today.year, today.month, today.day)
    tracking_date = day.strftime('%A %d %B %Y')
    lines = '-' * len(header)
    menu_printer(header)
    menu_printer(lines, True)
    menu_printer(tracking_date)


def menu_read_input(text: str) -> str:
    align_size = utils.aligner(text)
    data = input(text.rjust(align_size))

    return data


def menu_info(text: str) -> None:
    pass


def daily_tracking_menu() -> list | None:
    user_data = []
    menu_header('Daily tracking')
    wakeup_time = menu_read_input('wake up time? ')
    sleepy_time = menu_read_input('time went to sleep? ')

    if DailyTrackingValidation.ispropertime(wakeup_time) == False:
        log_message('Invalid wake up time', level='ERROR')
        return None

    if DailyTrackingValidation.ispropertime(sleepy_time) == False:
        log_message('Invalid sleepy up time', level='ERROR')
        return None

    user_data.append(wakeup_time)
    user_data.append(sleepy_time)

    log_message('Data uploaded successfully')
    return user_data


def budget_tracking_menu() -> list | None:
    pass


def repl():
    while True:
        try:
            user_input = int(input(System.APP_NAME.value))
            match user_input:
                case Activity.DAILY_TRACKING:
                    data = daily_tracking_menu()
                    if data is None:
                        log_message('Failed to upload data')
                    else:
                        pool.daily_tracking_api.save_tracking_data(data)
                case Activity.BUDGETING:
                    data = budget_tracking_menu()
                    if data is None:
                        log_message('Failed to upload data')
                    else:
                        pass
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

    if pool.check_status() is False:
        logger.warn('API connections not active')

    # repl()

    core.debugger()
