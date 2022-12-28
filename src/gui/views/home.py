""" The home window of the application """

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow
from base.constants import System
from gui.config import APP_WINDOW_HEIGHT, APP_WINDOW_WIDTH


class Home(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(System.APP_NAME.value)

        self.setMinimumSize(APP_WINDOW_WIDTH, APP_WINDOW_HEIGHT)

        self.create_actions()
        self.create_menus()

    def create_actions(self):
        pass

    def create_menus(self):
        menubar = self.menuBar()

        self.settings_menu = menubar.addMenu('&Settings')
        self.settings_menu.addSeparator()

        self.help_menu = menubar.addMenu('&Help')