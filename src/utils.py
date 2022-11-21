import os
import config

try:
    import tomlib
except ModuleNotFoundError:
    import tomli as tomlib

import yaml


def get_log_file(filename: str) -> str:
    return os.path.join(config.DATA_DIR, filename)


def get_config_file(filename: str) -> str:
    return os.path.join(config.DATA_DIR, 'filename')


def get_yaml_config(filename: str) -> None:
    if not os.path.exists(filename):
        pass
