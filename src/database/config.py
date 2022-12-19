""" Database configurations module """

from utils import parse_config_file
from logger import logger


def get_mysql_config() -> dict:
    config_data = parse_config_file('data')

    try:
        return config_data['mysql']
    except KeyError:
        logger.warning('Cannot find mysql database configurations')
        return {}
