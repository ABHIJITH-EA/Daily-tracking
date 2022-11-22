import version
from utils import get_yaml_config


def parse_config(key: str) -> dict | None:
    config_data = get_yaml_config('cli.yaml')
    try:
        return config_data[key]
    except KeyError:
        pass


def get_author():
    author = parse_config('author')
    return author['name']

def get_app_menu():
    menu = parse_config('menu')
    return menu['application']


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
def application_menu():
    print('                                                       ')
    print('                                                       ')
    print('                                                       ')
    
    menu_list = get_app_menu()
    for menu in menu_list:
        print(f' [*] {menu}')