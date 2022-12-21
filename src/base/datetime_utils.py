""" Utils for support date and time datas """

from datetime import date, datetime
from logger import logger

app_datetime_fmt = '%d-%m-%Y %H:%M:%S'
app_date_fmt = '%d-%m-%Y'


def datetime_to_db(datetime_str: str, fmt: str=app_datetime_fmt):
    mysql_datetime_fmt = '%Y-%m-d %H:%M:%S'
    try:
        dt = datetime.strptime(datetime_str, fmt)
        return dt.strftime(mysql_datetime_fmt)
    except ValueError as e:
        logger.error('Failed to convert date to DB date format')


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