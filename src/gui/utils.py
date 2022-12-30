
import os
import config


def read_style_sheet(filename: str, dir: str='styles'):
    filepath = os.path.join(config.RESOURCE_DIR, dir)
    
    if not os.path.isfile(filepath):
        raise FileNotFoundError
    
    with open(filepath, 'rb') as f:
        styles = f.read()

    return styles.decode('utf-8')