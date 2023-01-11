""" """

from PyQt6.QtWidgets import QWidget
from PyQt6 import QtWidgets, QtCore


class WeekPlannerTab(QWidget):

    def __init__(self) -> None:
        super().__init__()

        self.main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.main_layout)

        self.create_ui()

    
    def create_ui(self):
        self.start_date_label = QtWidgets.QLabel('Start date')
        self.start_date_label.setObjectName('start-date-label')
        self.start_date_input = QtWidgets.QDateEdit(self)
        self.start_date_input.setObjectName('start-date-input')
        self.start_date_input.setCalendarPopup(True)
        self.start_date_input.setDate(QtCore.QDate.currentDate())

        self.week_goal_label = QtWidgets.QLabel('Goal')
        self.week_goal_label.setObjectName('week-goal-label')
        self.week_goal_input = QtWidgets.QTextEdit(self)
        self.week_goal_input.setObjectName('week-goal-input')

        self.main_layout.addWidget(self.start_date_label)
        self.main_layout.addWidget(self.start_date_input)
        self.main_layout.addWidget(self.week_goal_label)
        self.main_layout.addWidget(self.week_goal_input)