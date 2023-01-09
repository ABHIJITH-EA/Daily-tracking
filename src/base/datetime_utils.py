""" Utils for support date and time datas """

from datetime import date, datetime, timedelta
from logger import logger

app_datetime_fmt = '%d-%m-%Y %H:%M:%S'
app_date_fmt = '%d-%m-%Y'
app_time_fmt = '%I:%M %p'


# TODO:Code review
def to_db_datetime(datetime_str: str, fmt: str=app_datetime_fmt):
    mysql_datetime_fmt = '%Y-%m-%d %H:%M:%S'
    try:
        dt = datetime.strptime(datetime_str, fmt)
        return dt.strftime(mysql_datetime_fmt)
    except ValueError as e:
        logger.error('Failed to convert datetime to DB datetime format')


# TODO:Code review
def to_db_time(time_str: str, fmt: str = app_time_fmt):
    mysql_time_fmt = '%H:%M:%S'
    
    try:
        dt = datetime.strptime(time_str, fmt)
        return dt.strftime(mysql_time_fmt)
    except ValueError as e:
        logger.error('Failed to convert time to DB time format')


# TODO:Code review
def to_db_date(date_str: str, fmt: str = app_date_fmt):
    mysql_date_fmt = '%Y-%m-%d'
    try:
        dt = datetime.strptime(date_str, fmt)
        return dt.strftime(mysql_date_fmt)
    except ValueError as e:
        logger.error('Failed to convert date to DB date format')


# BUG: Need return something when exception happend
def to_app_date(date_str: date, fmt: str = app_date_fmt):
    try:
        return date_str.strftime(fmt)
    except ValueError as e:
        logger.error('Failed to convert date to app date format')


# BUG: Need return something when exception happend        
def to_app_datetime(datetime_str:datetime, fmt:str = '%d-%m-%Y %I:%M %p'):
    try:
        return datetime_str.strftime(fmt)
    except ValueError as e:
        logger.error('Failed to convert datetime to app datetime format')


# BUG: Need return something when exception happend  
def db_time_to_app_time(time_str: timedelta, fmt: str = app_time_fmt):
    app_time = (datetime.min + time_str).time()
    try:
        return app_time.strftime(fmt)
    except ValueError as e:
        logger.error('Failed to convert time from db time to app time format')


def current_datetime():
    now = datetime.now()

    fmt = app_datetime_fmt

    return now.strftime(fmt)


def current_date():
    today = date.today()
    
    fmt = app_date_fmt

    return today.strftime(fmt)


def yesterday_date():
    pass