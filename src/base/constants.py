""" Core constants """

from enum import Enum, IntEnum, unique


@unique
class Activity(IntEnum):
    DAILY_TRACKING = 1
    BUDGETING = 2


@unique
class General(IntEnum):
    EXIT = 0


class System(Enum):
    APP_NAME = ' XXXChange ==> '
    LOGGER_NAME = 'XXXChange'
    SECONDARY_LEFT_ALIGN = len(APP_NAME)