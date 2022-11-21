import os
import config


def get_log_file(filename: str) -> str:
    return os.path.join(config.DATA_DIR, filename)

def get_config_file(filename: str) -> str:
    return os.path.join(config.DATA_DIR, 'filename')