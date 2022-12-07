import signal
import atexit
from logger import logger


def ctrl_c(signum, frame):
    logger.info("CTRL_C pressed")
    print("CTRL_C Can't process")

def safe_exit():
    print('\n\r Bye')

def init_handlers():
    signal.signal(signal.SIGINT, ctrl_c)
    atexit.register(safe_exit)