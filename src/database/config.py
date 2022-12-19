""" Database configurations module """

import os
from utils import parse_config_file
from logger import logger
import config

_SQLITEDB_NAME = 'xxxchange.db'

SQLITEDB_PATH = os.path.join(config.DATA_DIR, _SQLITEDB_NAME)

def get_mysql_config() -> dict:
    config_data = parse_config_file('database')

    try:
        return config_data['mysql']
    except KeyError:
        logger.warning('Cannot find mysql database configurations')
        return {}
