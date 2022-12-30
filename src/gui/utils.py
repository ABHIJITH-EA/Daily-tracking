import os

BASE = os.getcwd()

RESOURCE_DIR = os.path.join(BASE, 'resources')
STYLESHEET_DIR = os.path.join(RESOURCE_DIR, 'styles')

def read_style_sheet(filename: str, dir: str=STYLESHEET_DIR):
    filepath = os.path.join(dir, filename)

    if not os.path.isfile(filepath):
        raise FileNotFoundError
    
    with open(filepath, 'rb') as f:
        styles = f.read()

    return styles.decode('utf-8')