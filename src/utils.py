import os
import config

try:
    import tomlib
except ModuleNotFoundError:
    import tomli as tomlib


def get_log_file(filename: str) -> str:
    return os.path.join(config.DATA_DIR, filename)

def get_config_file(filename: str) -> str:
    return os.path.join(config.DATA_DIR, 'filename')