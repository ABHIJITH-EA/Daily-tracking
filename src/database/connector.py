""" Database connection manager """

import os
import config
import importlib

_db_driver_instances = {}


def _driver_initializer(driver: str):
    db_driver_path = os.path.join(config.ENTRY_DIR, 'database', 'driver')
    
    driver_module = importlib.import_module('.mysql', db_driver_path)

    print(driver_module)


def connect(driver:str = 'mysql'):
    global _db_driver_instances
    if _db_driver_instances.get(driver):
        return _db_driver_instances.get(driver)
    else:
        db_driver_instance = _driver_initializer(driver)
        _db_driver_instances[driver] = db_driver_instance

    return _db_driver_instances[driver]