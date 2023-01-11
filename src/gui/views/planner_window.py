""" """

from PyQt6.QtWidgets import QMainWindow, QWidget

from gui import config

class PlannerWindow(QWidget):
    
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle(config.PLANNER_WINDOW_TITLE)
        self.setMinimumSize(config.PLANNER_WINDOW_MIN_WIDTH,
                    config.PLANNER_WINDOW_MIN_HEIGHT)

        self.create_ui()

    
    def create_ui(self):
        pass