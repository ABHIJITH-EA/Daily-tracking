""" Entry file """

import sys
import traceback
from logger import logger, config_logger
from cli import console
from handlers import init_handlers
import pool
from base.constants import General
from database.models import app_initializer
from utils import read_sql_file
from gui.main import run


def create_app():
    sql_script = read_sql_file()
    db_status = app_initializer.AppInitializer.create_mysql_tables(sql_script)

    if not db_status:
        sys.exit(General.EXIT)


def precheck():
    app_model = app_initializer.AppInitializer()

    if app_model.check_database_status():
        logger.info('Database connected')
        return True
    else:
        logger.info('Application loading for first time')
        return False


if __name__ == '__main__':
    config_logger()
    init_handlers()
    try:
        if not precheck():
            create_app()
        pool.activate()
        # console.init()
        run()
    except Exception as e:
        logger.error(traceback.format_exc())
