""" XXXChange app gui start from here """

import sys
from PyQt6.QtWidgets import QApplication
from gui.views import home

def start_gui():
    app = QApplication([])

    maiwindow = home.Home()
    maiwindow.show()

    sys.exit(app.exec())