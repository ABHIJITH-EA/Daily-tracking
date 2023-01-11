""" """

from PyQt6.QtWidgets import QDialog
from PyQt6 import QtWidgets

from gui import config
from gui.views.month_planner_tab import MonthPlannerTab
from gui.views.week_planner_tab import WeekPlannerTab

class PlannerWindow(QDialog):
    
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle(config.PLANNER_WINDOW_TITLE)
        self.setMinimumSize(config.PLANNER_WINDOW_MIN_WIDTH,
                    config.PLANNER_WINDOW_MIN_HEIGHT)

        self.main_laout = QtWidgets.QVBoxLayout()
        self.setLayout(self.main_laout)

        self.create_ui()

    
    def create_ui(self):
        self.planner_tab_box = QtWidgets.QTabWidget(self)
        self.month_planner_tab = MonthPlannerTab()
        self.week_planner_tab = WeekPlannerTab()

        self.planner_tab_box.addTab(self.week_planner_tab, 'Week')
        self.planner_tab_box.addTab(self.month_planner_tab, 'Month')

        self.main_laout.addWidget(self.planner_tab_box)
