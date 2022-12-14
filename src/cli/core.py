import version
from utils import get_yaml_config, parse_config_file
from logger import logger


def parse_config(key: str) -> dict | None:
    config_data = get_yaml_config('cli.yaml')
    try:
        return config_data[key]
    except KeyError:
        logger.info(f'{key} not found in the config file')


# TODO: it's a bad implementation not logical
# to get the author from config file.
def get_author() -> str:
    author = parse_config('author')
    if author is not None:
        return author['name']
    return ''


def get_app_menu() -> str:
    menu = parse_config('menu')
    if menu is not None:
        return menu['application']
    return ''


def banner() -> None:
    print('                                                       ')
    print('                                                       ')
    print('                                                       ')
    print(' __  ____  ____  __  ___ _                             ')
    print(' \ \/ /\ \/ /\ \/ / / __\ |__   __ _ _ __   __ _  ___  ')
    print("  \  /  \  /  \  / / /  | '_ \ / _` | '_ \ / _` |/ _ \ ")
    print('  /  \  /  \  /  \/ /___| | | | (_| | | | | (_| |  __/ ')
    print(' /_/\_\/_/\_\/_/\_\____/|_| |_|\__,_|_| |_|\__, |\___| ')
    print('                                            |___/      ')
    print('                                                       ')
    print(f' Version  {version.__version__}                       ')
    print(f' Coded by {get_author()}                              ')
    print('                                                       ')


# TODO: Fix manual `print sizing`
#       make a function to do it
def application_menu() -> None:
    print('                                                       ')
    print('                                                       ')
    print('                                                       ')

    menu_list = get_app_menu()
    for menu in menu_list:
        print(f' [*] {menu}')

    print('                                                       ')
    print('                                                       ')


# Debugger for the cli system
def debugger():
    pass
