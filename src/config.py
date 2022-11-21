import os

try:
    import tomlib
except ModuleNotFoundError:
    import tomli as tomlib


ENTRY_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(ENTRY_DIR)

DATA_DIR = os.path.join(BASE_DIR, 'data')
RESOURCE_DIR = os.path.join(BASE_DIR, 'resources')
