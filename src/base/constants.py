""" Core constants """

from enum import Enum, IntEnum, unique


@unique
class Activity(IntEnum):
    DAILY_TRACKING = 1
    BUDGETING = 2


@unique
class General(IntEnum):
    EXIT = 0
    CRASHED = 1


class System(Enum):
    APP_NAME = 'XXXChange'
    APP_STDIN = 'XXXChange ==> '
    LOGGER_NAME = 'XXXChange'
    SECONDARY_LEFT_ALIGN = len(APP_STDIN)
    CONSOLE_MENU_ALIGN_SIZE = 3