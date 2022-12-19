""" Database connection manager """

import os
import importlib
from logger import logger

_db_driver_instances = {}
_DB_DRIVER_PATH = os.path.dirname(__file__).rpartition('/')[-1] + '.driver.'


def _driver_initializer(driver: str):
    db_driver_path = _DB_DRIVER_PATH +  driver
    driver_suffix = 'Db'
    db_class = driver.capitalize() + driver_suffix
    try:
        driver_module = importlib.import_module(db_driver_path)
        driver_instance = getattr(driver_module, db_class)
    except ModuleNotFoundError:
        driver_instance = None
        logger.warn(f'No {driver} driver found')

    return driver_instance


# BUG: Why return a None db connection ?
def connect(driver:str = 'mysql'):
    global _db_driver_instances
    if _db_driver_instances.get(driver):
        return _db_driver_instances.get(driver)
    else:
        db_driver_instance = _driver_initializer(driver)
        if db_driver_instance is  None:
            return None
        _db_driver_instances[driver] = db_driver_instance

    logger.info(f'{driver} driver initialized')
    
    return _db_driver_instances[driver]