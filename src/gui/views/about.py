
from PyQt6.QtWidgets import QDialog
from PyQt6 import QtWidgets
from PyQt6 import QtCore
from gui.config import ABOUT_WINDOW_TITLE, ABOUT_WINDOW_HEIGHT, ABOUT_WINDOW_WIDTH
from base.constants import System


class AboutWindow(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(ABOUT_WINDOW_TITLE)
        self.setMinimumSize(ABOUT_WINDOW_WIDTH, ABOUT_WINDOW_HEIGHT)


    def create_ui(self):
        self.layout = QtWidgets.QGridLayout(self)

        self.aboutWindowLabel = QtWidgets.QLabel(System.APP_NAME.value)
        self.aboutWindowLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
        self.licenceLabel = QtWidgets.QLabel('Licence')
        self.licenceLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)