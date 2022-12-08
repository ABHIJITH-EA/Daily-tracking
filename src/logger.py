import logging
import utils
from base.constants import System

logger = logging.getLogger(System.LOGGER_NAME.value)


def config_logger(filename: str = 'application.log', level: int = 10) -> None:
    global logger
    logrec_fmt_str = \
    '%(asctime)s %(process)d %(pathname)s %(msecs)d %(levelname)s %(message)s'
    logrec_datefmt_str = '%Y-%m-%d %H:%M:%S'

    logger_handler = logging.FileHandler(filename=\
                                         utils.get_log_file(filename),
                                         mode='a', encoding='utf-8',
                                         )
    logrec_fmt = logging.Formatter(fmt=logrec_fmt_str,
                                    datefmt=logrec_datefmt_str)

    #
    #   CRITICAL    50
    #   ERROR       40
    #   WARNING     30
    #   INFO        20
    #   DEBUG       10
    #   NOTSET      0   Default
    #
    logger.setLevel(level)
    logger_handler.setFormatter(logrec_fmt)
    logger.addHandler(logger_handler)
