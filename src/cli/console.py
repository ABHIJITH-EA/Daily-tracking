""" Console window for the cli """

from cli import core


def repl():
    while True:
        user_input = input(' XXXChange ==> ')


def init():
    core.banner()
    core.application_menu()

    repl()