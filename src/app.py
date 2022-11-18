import os
import logging


ENTRY_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(ENTRY_DIR)

DATA_DIR = os.path.join(BASE_DIR, 'data')
RESOURCE_DIR = os.path.join(BASE_DIR, 'resources')

LOGFILE = os.path.join(DATA_DIR, 'application.log')

# Logging system configuration
logging.basicConfig(filename=LOGFILE,
                    filemode='a',
                    format='%(asctime)s %(process)s %(pathname)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    style='%',
                    level='DEBUG')