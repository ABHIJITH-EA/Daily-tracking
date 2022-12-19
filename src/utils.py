import os
import config

try:
    import tomlib
except ModuleNotFoundError:
    import tomli as tomlib

import yaml


def get_log_file(filename: str) -> str:
    return os.path.join(config.DATA_DIR, filename)


def get_config_file(filename: str) -> str | None:
    filepath = os.path.join(config.CONFIG_DIR, filename)
    if os.path.exists(filepath):
        return filepath


def get_yaml_config(filename: str, dir: str = config.CONFIG_DIR) -> None | str:
    filepath = os.path.join(dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return yaml.full_load(f)
        

def parse_config_file(key: str) -> dict | None:
    config_file = get_config_file('config.toml')
    if config_file is not None:
        with open(config_file, 'rb') as f:
            config_data = tomlib.load(f)
            try:
                return config_data[key]
            except KeyError:
                pass

# TODO: what happens if there is no sql file
def read_sql_file(filename: str = 'sql.sql', dir: str = config.DATA_DIR) -> list:
    sql_file = os.path.join(dir, filename)

    try:
        with open(sql_file, 'r') as f:
            data = f.read()
    except FileNotFoundError:
        pass

    sql_commands = data.split(';')

    return sql_commands