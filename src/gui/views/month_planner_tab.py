""" """

from PyQt6.QtWidgets import QWidget
from PyQt6 import QtWidgets, QtCore


class MonthPlannerTab(QWidget):

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
        self.end_date_label = QtWidgets.QLabel('End date')
        self.end_date_label.setObjectName('end-date-label')
        self.end_date_input = QtWidgets.QDateEdit(self)
        self.end_date_input.setObjectName('end-date-input')
        self.end_date_input.setCalendarPopup(True)
        self.end_date_input.setDate(QtCore.QDate.currentDate())

        self.month_goal_label = QtWidgets.QLabel('Goal')
        self.month_goal_label.setObjectName('month-goal-label')
        self.month_goal_input = QtWidgets.QTextEdit(self)
        self.month_goal_input.setObjectName('month-goal-input')

        self.main_layout.addWidget(self.start_date_label)
        self.main_layout.addWidget(self.start_date_input)
        self.main_layout.addWidget(self.end_date_label)
        self.main_layout.addWidget(self.end_date_input)
        self.main_layout.addWidget(self.month_goal_label)
        self.main_layout.addWidget(self.month_goal_input)