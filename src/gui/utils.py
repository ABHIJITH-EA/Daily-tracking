
import os
import config


def read_style_sheet(filename: str, dir: str='styles'):
    filepath = os.path.join(config.RESOURCE_DIR, dir, filename)
    
    if not os.path.isfile(filepath):
        raise FileNotFoundError
    
    with open(filepath, 'rb') as f:
        styles = f.read()

    return styles.decode('utf-8')


def get_icon_path(icon_name: str, dir: str = 'img'):
    icon_path = os.path.join(config.RESOURCE_DIR, dir, icon_name)

    if not os.path.isfile(icon_path):
        raise FileNotFoundError

    return icon_path