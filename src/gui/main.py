""" """

import sys
from PyQt6.QtWidgets import QApplication

from gui.views.home_window import HomeWindow


def run():
    app = QApplication([])

    home_window = HomeWindow()
    home_window.show()

    sys.exit(app.exec())