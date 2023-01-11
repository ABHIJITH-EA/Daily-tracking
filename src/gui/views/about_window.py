
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog

from gui import config


class AboutWindow(QDialog):
    def __init__(self) -> None:
        super().__init__()
        
        self.setWindowTitle(config.ABOUT_WINDOW_TITLE)
        self.setMinimumSize(config.ABOUT_WINDOW_WIDTH, config.ABOUT_WINDOW_HEIGHT)