""" Console window for the cli """

import sys
import time
from datetime import date
from enum import IntEnum
from cli import core, utils
from base.constants import Activity, General, System
from logger import logger
from api.validations.daily_tracking import DailyTrackingValidation
from api.validations.budget_tracking import BudgetTrackingValidation
import pool

# TODO: Fix level ambiguity eg: `INFO` verbose
def log_message(msg: str, level = 'INFO'):
    log_time = time.strftime('%H:%M:%S')
    log_text = f'[{log_time}] [{level}] {msg}'
    align_length = len(log_text) + System.SECONDARY_LEFT_ALIGN.value
    print(log_text.rjust(0))


# BUG: Not aligning properly
def menu_printer(text: str, new_line=False) -> None:
    align_size = utils.aligner(text)
    print(f'{text}'.rjust(align_size))
    if new_line:
        print() 


# TODO: Code review
def menu_header(header: str) -> None:
    today = date.today()
    day = date(today.year, today.month, today.day)
    tracking_date = day.strftime('%A %d %B %Y')
    lines = '-' * len(header)
    menu_printer(header)
    menu_printer(lines, True)
    menu_printer(tracking_date, new_line=True)


def menu_read_input(text: str) -> str:
    align_size = len(text) + System.CONSOLE_MENU_ALIGN_SIZE.value
    data = input(text.rjust(align_size))

    return data


def menu_info(text: str) -> None:
    pass


def daily_tracking_menu() -> list | None:
    user_data = []
    select_options = IntEnum('ACTIVITY_OPTIONS',
                ['VIEW', 'ADD'])
    menu_header('Daily tracking')

    menu_printer('[*] View daily tracking data')
    menu_printer('[*] Add daily tracking data')
    
    try:
        user_selection = int(menu_read_input('Select: '))
    except ValueError:
        log_message('Bad input')
        return None

    if user_selection == select_options.VIEW:
        log_message('View data')
    elif user_selection == select_options.ADD:
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

        return user_data
    else:
        log_message('Invalid selection')
        return None



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
                        log_message('Activity closed')
                    else:
                        pool.daily_tracking_api.save_tracking_data(data)
                        log_message('Data uploaded successfully')
                        logger.info('Daily activity saved')
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

    repl()

    # core.debugger()
