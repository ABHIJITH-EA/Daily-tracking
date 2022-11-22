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


def get_yaml_config(filename: str, dir: str = config.CONFIG_DIR) -> None | str:
    filepath = os.path.join(dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return yaml.full_load(f)