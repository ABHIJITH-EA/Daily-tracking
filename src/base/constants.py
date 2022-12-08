""" Core constants """

from enum import IntEnum, unique


@unique
class Activity(IntEnum):
    DAILY_TRACKING = 1
    BUDGETING = 2


@unique
class General(IntEnum):
    EXIT = 0
