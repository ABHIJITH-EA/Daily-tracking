""" """

from PyQt6.QtWidgets import QWidget
from PyQt6 import QtWidgets, QtCore

from gui.controllers.week_planner_controller import WeekPlannerController

class WeekPlannerTab(QWidget):

    def __init__(self) -> None:
        super().__init__()

        self.week_planner_controller = WeekPlannerController()
        self.status_bar = QtWidgets.QStatusBar(self)
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
        self.button_box = QtWidgets.QFrame(self)
        self.button_box.setObjectName('button-box')
        self.save_btn = QtWidgets.QPushButton('Save')
        self.button_box_layout = QtWidgets.QHBoxLayout(self.button_box)
        self.save_btn.setObjectName('save-btn')
        self.clear_btn = QtWidgets.QPushButton('Clear')
        self.clear_btn.setObjectName('clear-btn')
        self.button_box_layout.setSpacing(10)
        self.button_box_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self.button_box_layout.addStretch(1)
        self.button_box_layout.addWidget(self.clear_btn)
        self.button_box_layout.addWidget(self.save_btn)

        self.main_layout.addWidget(self.start_date_label)
        self.main_layout.addWidget(self.start_date_input)
        self.main_layout.addWidget(self.week_goal_label)
        self.main_layout.addWidget(self.week_goal_input)
        self.main_layout.addWidget(self.button_box)
        self.main_layout.addWidget(self.status_bar)        
        self.main_layout.addStretch(1)

        self.save_btn.clicked.connect(self.confirm_save)


    def save_data(self):
        data = [self.start_date_input.date().toPyDate(), self.week_goal_input.toPlainText()]
        status = self.week_planner_controller.save(data)
        
        if status:
            self.status_bar.showMessage('Saved successfully', 3000)
        else:
            self.status_bar.showMessage('Failed to save', 3000)


    def confirm_save(self):
        message_box = QtWidgets.QMessageBox(self)
        message_box.setWindowTitle('Confirm month data')
        message_box.setIcon(QtWidgets.QMessageBox.Icon.Question)
        message_box.setText('Are you sure want to save')
        message_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes
                                       | QtWidgets.QMessageBox.StandardButton.No)
        result = message_box.exec()

        if result == QtWidgets.QMessageBox.StandardButton.Yes:
            self.save_data()