""" """

from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

from gui import config, utils
from logger import logger
from gui.controllers.spent_tracking_controller import SpentTrackingController
from gui.controllers.income_tracking_controller import IncomeTrackingController
from gui.controllers.daily_tracking_controller import DailyTrackingController


class HomeWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle(config.APP_MAINWINDOW_TITLE)

        self.setMinimumSize(config.APP_MAINWINDOW_MIN_WIDTH,
                            config.APP_MAINWINDOW_MIN_HEIGHT)

        self.main_frame = QtWidgets.QFrame(self)
        self.main_frame.setObjectName('Main-frame')
        self.central_layout = QtWidgets.QVBoxLayout(self.main_frame)
        self.setCentralWidget(self.main_frame)

        try:
            styles = utils.read_style_sheet('home_window.css')
            self.setStyleSheet(styles)
        except FileNotFoundError as e:
            logger.warning(f'Cannot find stylesheet')

        self.spent_controller = SpentTrackingController()
        self.income_controller = IncomeTrackingController()
        self.daily_tracking_controller = DailyTrackingController()

        self.create_ui()

    def create_ui(self):
        self.daily_tracking_box = QtWidgets.QFormLayout()
        self.daily_tracking_groupbox = QtWidgets.QGroupBox(
            'Daily tracking', self.main_frame)
        self.daily_tracking_groupbox.setLayout(self.daily_tracking_box)
        self.central_layout.addWidget(self.daily_tracking_groupbox)

        # self.day_input = QtWidgets.QLineEdit()
        # self.daily_tracking_box.addRow('Day', self.day_input)
        self.wakeup_time = QtWidgets.QLineEdit()
        self.daily_tracking_box.addRow('Wakeup time', self.wakeup_time)
        self.sleepy_time_input = QtWidgets.QLineEdit()
        self.daily_tracking_box.addRow('Sleepy time', self.sleepy_time_input)
        self.daily_tracking_button_box = QtWidgets.QHBoxLayout()
        self.daily_tracking_save_btn = QtWidgets.QPushButton(
            'Save', self.daily_tracking_groupbox)
        self.daily_tracking_button_box.addWidget(
            self.daily_tracking_save_btn, 0, Qt.AlignmentFlag.AlignRight)
        self.daily_tracking_box.setLayout(
            3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.daily_tracking_button_box)

        self.budget_tracking_groupbox = QtWidgets.QGroupBox(
            'Budget tracking', self.main_frame)
        self.budget_tracking_layout = QtWidgets.QHBoxLayout()
        self.budget_tracking_groupbox.setLayout(self.budget_tracking_layout)
        self.central_layout.addWidget(self.budget_tracking_groupbox)

        self.income_tracking_box = QtWidgets.QFormLayout()
        self.income_tracking_groupbox = QtWidgets.QGroupBox(
            'Income tracking', self.budget_tracking_groupbox)
        self.income_tracking_groupbox.setLayout(self.income_tracking_box)
        self.income_amount_input = QtWidgets.QLineEdit()
        self.income_tracking_box.addRow('Amount', self.income_amount_input)
        self.income_remarks_input = QtWidgets.QLineEdit()
        self.income_tracking_box.addRow('Remarks', self.income_remarks_input)
        self.income_tracking_button_box = QtWidgets.QHBoxLayout()
        self.income_tracking_save_btn = QtWidgets.QPushButton(
            'Save', self.income_tracking_groupbox)
        self.income_tracking_button_box.addWidget(
            self.income_tracking_save_btn, 0, Qt.AlignmentFlag.AlignRight)
        self.income_tracking_box.setLayout(
            3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.income_tracking_button_box)

        self.spent_tracking_box = QtWidgets.QFormLayout()
        self.spent_tracking_groupbox = QtWidgets.QGroupBox(
            'Spent tracking', self.budget_tracking_groupbox)
        self.spent_tracking_groupbox.setLayout(self.spent_tracking_box)
        self.spent_amount_input = QtWidgets.QLineEdit()
        self.spent_tracking_box.addRow('Amount', self.spent_amount_input)
        self.spent_remarks_input = QtWidgets.QLineEdit()
        self.spent_tracking_box.addRow('Remarks', self.spent_remarks_input)
        self.spent_tracking_button_box = QtWidgets.QHBoxLayout()
        self.spent_tracking_save_btn = QtWidgets.QPushButton(
            'Save', self.spent_tracking_groupbox)
        self.spent_tracking_button_box.addWidget(
            self.spent_tracking_save_btn, 0, Qt.AlignmentFlag.AlignRight)
        self.spent_tracking_box.setLayout(
            3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.spent_tracking_button_box)

        self.daily_tracking_save_btn.clicked.connect(lambda: self.daily_tracking_controller.save(
            [self.wakeup_time.text(), self.sleepy_time_input.text()]))
        self.income_tracking_save_btn.clicked.connect(lambda: self.income_controller.save(
            [self.income_amount_input.text(), self.income_remarks_input.text()]))
        self.spent_tracking_save_btn.clicked.connect(
            lambda: self.spent_controller.save([self.spent_amount_input.text(), self.spent_remarks_input.text()]))

        self.budget_tracking_layout.addWidget(self.income_tracking_groupbox)
        self.budget_tracking_layout.addWidget(self.spent_tracking_groupbox)
