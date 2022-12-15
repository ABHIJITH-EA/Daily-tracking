import traceback
from logger import logger, config_logger
from cli import console
from handlers import init_handlers
import pool

config_logger()
init_handlers()

if __name__ == '__main__':
    try:
        pool.activate()
        console.init()
    except Exception as e:
        logger.error(traceback.format_exc())
