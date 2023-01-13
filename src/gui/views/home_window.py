""" """

from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from PyQt6.QtCharts import QPieSeries, QPieSlice, QChart, QChartView

from gui import config, utils
from logger import logger
from gui.controllers.spent_tracking_controller import SpentTrackingController
from gui.controllers.income_tracking_controller import IncomeTrackingController
from gui.controllers.daily_tracking_controller import DailyTrackingController
from gui.controllers.wakeup_time_backup_controller import WakeupTimeBackupController
from gui.controllers.week_planner_controller import WeekPlannerController
from gui.controllers.month_planner_controller import MonthPlannerController
from gui.views.about_window import AboutWindow
from gui.views.planner_window import PlannerWindow


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

        self.spent_tracking_controller = SpentTrackingController()
        self.income_tracking_controller = IncomeTrackingController()
        self.daily_tracking_controller = DailyTrackingController()
        self.wakeup_time_backup_controller = WakeupTimeBackupController()
        self.month_planner_controller = MonthPlannerController()
        self.week_planner_controller = WeekPlannerController()
        self.tracking_date = QtCore.QDate()

        self.create_actions()
        self.create_toolbar()
        self.create_menubar()
        self.create_ui()


    def create_actions(self):
        exit_icon = utils.get_icon_path('exit_menu.png')
        analysis_icon = utils.get_icon_path('analysis_window.png')
        backup_icon = utils.get_icon_path('backup_window.png')
        save_icon = utils.get_icon_path('save_menu.png')
        about_icon = utils.get_icon_path('about_menu.png')
        planner_icon = utils.get_icon_path('planner_window.png')
        import_icon = utils.get_icon_path('import_menu.png')
        export_icon = utils.get_icon_path('export_menu.png')
        log_icon = utils.get_icon_path('log_icon.png')
        
        self.exit_action = QtGui.QAction('Exit', self)
        self.exit_action.setIcon(QIcon(exit_icon))
        self.exit_action.setShortcut(QtGui.QKeySequence(QtGui.QKeySequence.StandardKey.Quit))
        self.exit_action.setWhatsThis('Exit app')
        self.exit_action.triggered.connect(self.close_app)

        self.import_action = QtGui.QAction('Import', self)
        self.import_action.setIcon(QIcon(import_icon))

        self.export_action = QtGui.QAction('Export', self)
        self.export_action.setIcon(QIcon(export_icon))

        self.about_action = QtGui.QAction('About', self)
        self.about_action.setIcon(QIcon(about_icon))
        self.about_action.triggered.connect(self.open_about_window)

        # Toolbar actions
        self.analysis_action = QtGui.QAction('Analysis', self)
        self.analysis_action.setIcon(QIcon(analysis_icon))
        self.about_action.setWhatsThis('About the application')

        self.backup_action = QtGui.QAction('Backup', self)
        self.backup_action.setIcon(QIcon(backup_icon))

        self.wakeup_time_backup_action = QtGui.QAction('Wakeup time', self)
        self.wakeup_time_backup_action.triggered.connect(self.open_wakeup_time_backup_window)

        self.planner_action = QtGui.QAction('Planner', self)
        self.planner_action.setIcon(QIcon(planner_icon))
        self.planner_action.triggered.connect(self.open_planner_window)

        self.log_view_action = QtGui.QAction('Log', self)
        self.log_view_action.setIcon(QIcon(log_icon))
        self.log_view_action.triggered.connect(self.open_log_window)


    def create_toolbar(self):
        self.app_toolbar = QtWidgets.QToolBar('Exit', self)
        self.app_toolbar.setIconSize(QtCore.QSize(30, 30))
        self.app_toolbar.layout().setSpacing(20)

        self.app_toolbar.addAction(self.analysis_action)
        self.app_toolbar.addAction(self.backup_action)
        self.app_toolbar.addAction(self.planner_action)
        self.addToolBar(self.app_toolbar)


    def create_menubar(self):
        self.app_menubar = self.menuBar()
        self.file_menu = QtWidgets.QMenu('File', self)
        self.edit_menu = QtWidgets.QMenu('Edit', self)
        self.view_menu = QtWidgets.QMenu('View', self)
        self.help_menu = QtWidgets.QMenu('Help', self)

        # Submenu
        self.backup_menu = QtWidgets.QMenu('Backup')


        self.app_menubar.addMenu(self.file_menu)
        self.app_menubar.addMenu(self.edit_menu)
        self.app_menubar.addMenu(self.view_menu)
        self.app_menubar.addMenu(self.help_menu)
        self.view_menu.addMenu(self.backup_menu)

        self.backup_menu.addAction(self.wakeup_time_backup_action)

        self.file_menu.addAction(self.import_action)
        self.file_menu.addAction(self.export_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.exit_action)
        self.help_menu.addAction(self.about_action)
        self.view_menu.addAction(self.log_view_action) 

        self.app_statusbar = self.statusBar()


    def create_ui(self):
        # Daily tracking frame
        self.daily_tracking_frame = QtWidgets.QFrame(self.main_frame)
        self.daily_tracking_frame.setObjectName('Daily-tracking-frame')

        self.daily_tracking_frame_layout = QtWidgets.QHBoxLayout(self.daily_tracking_frame)
        self.daily_tracking_box = QtWidgets.QFrame(self.daily_tracking_frame)
        self.daily_tracking_box.setObjectName('Daily-tracking-box')
        self.daily_tracking_box_layout = QtWidgets.QVBoxLayout(self.daily_tracking_box)
        self.daily_tracking_box_layout.setSpacing(25)
        self.daily_tracking_box_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.daily_tracking_box_title = QtWidgets.QLabel('Daily tracking')
        self.daily_tracking_box_title.setObjectName('daily-tracking-box-title')
        self.daily_tracking_input_box = QtWidgets.QFrame(self.daily_tracking_box)
        self.daily_tracking_input_box.setObjectName('daily-tracking-input-box')
        self.daily_tracking_input_box_layout = QtWidgets.QFormLayout(self.daily_tracking_input_box)
        self.daily_tracking_date_label = QtWidgets.QLabel('Tracking date')
        self.daily_tracking_date_label.setObjectName('daily-tracking-date-label')
        self.daily_tracking_date_picker = QtWidgets.QDateEdit()
        self.daily_tracking_date_picker.setObjectName('daily-tracking-date-picker')
        self.daily_tracking_date_picker.setCalendarPopup(True)
        self.wakeup_time_label = QtWidgets.QLabel('Wakeup time')
        self.wakeup_time_label.setObjectName('wakeup-time-label')
        self.wakeup_time_input = QtWidgets.QLineEdit()
        self.wakeup_time_input.setObjectName('wakeup-time-input')
        self.sleepy_time_label = QtWidgets.QLabel('Sleepy time')
        self.sleepy_time_label.setObjectName('sleepy-time-label')
        self.sleepy_input_box = QtWidgets.QHBoxLayout()
        self.sleepy_time_input = QtWidgets.QLineEdit()
        self.sleepy_time_input.setObjectName('sleepy-time-input')
        self.sleepy_date_input = QtWidgets.QDateEdit()
        self.sleepy_date_input.setObjectName('sleepy-date-input')
        self.sleepy_date_input.setCalendarPopup(True)
        self.sleepy_input_box.addWidget(self.sleepy_time_input)
        self.sleepy_input_box.addWidget(self.sleepy_date_input)
        self.daily_tracking_button_box = QtWidgets.QFrame(self.daily_tracking_input_box)
        self.daily_tracking_button_box.setObjectName('daily-tracking-button-box')
        self.daily_tracking_button_box_layout = QtWidgets.QHBoxLayout(self.daily_tracking_button_box)
        self.daily_tracking_button_box_layout.setSpacing(8)
        self.daily_tracking_button_box_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.daily_tracking_save_btn = QtWidgets.QPushButton('Save')
        self.daily_tracking_save_btn.setObjectName('daily-tracking-save-btn')
        self.daily_tracking_clear_btn = QtWidgets.QPushButton('Clear')
        self.daily_tracking_clear_btn.setObjectName('daily-tracking-clear-btn')
        self.daily_tracking_button_box_layout.addWidget(self.daily_tracking_clear_btn)
        self.daily_tracking_button_box_layout.addWidget(self.daily_tracking_save_btn)

        self.daily_tracking_input_box_layout.addRow(self.daily_tracking_date_label,
                                                self.daily_tracking_date_picker)
        self.daily_tracking_input_box_layout.addRow(self.wakeup_time_label, self.wakeup_time_input)
        self.daily_tracking_input_box_layout.addRow(self.sleepy_time_label, self.sleepy_input_box)

        # self.daily_tracking_sub_box = QtWidgets.QFrame(self.daily_tracking_box)
        # self.daily_tracking_sub_box_layout = QtWidgets.QVBoxLayout(self.daily_tracking_sub_box)
        # self.current_day_wakeup_time_box = QtWidgets.QFrame(self.daily_tracking_sub_box)
        # self.current_day_wakeup_time_box_layout = QtWidgets.QFormLayout(self.current_day_wakeup_time_box)
        # self.current_day_wakeup_time_label = QtWidgets.QLabel('Latest wakeup time')
        # self.current_day_wakeup_time_input = QtWidgets.QLineEdit()
        # self.current_day_wakeup_time_box_layout.addRow(self.current_day_wakeup_time_label,
        #                                         self.current_day_wakeup_time_input)
        # self.daily_tracking_sub_box_layout.addWidget(self.current_day_wakeup_time_box)
        self.plan_box = QtWidgets.QFrame(self.daily_tracking_box)
        self.plan_box_layout = QtWidgets.QVBoxLayout(self.plan_box)
        self.plan_box_title = QtWidgets.QLabel('Planner area')
        self.plan_view_box = QtWidgets.QFrame(self.plan_box)
        self.plan_box_view_box_layout = QtWidgets.QHBoxLayout(self.plan_view_box)
        self.week_plan_box = QtWidgets.QFrame(self.plan_view_box)
        self.week_plan_box_layout = QtWidgets.QVBoxLayout(self.week_plan_box)
        self.week_plan_box_title = QtWidgets.QLabel('Week')
        self.week_plan_view = QtWidgets.QTableWidget(self.week_plan_box)
        self.week_plan_view.setColumnCount(5)
        self.week_plan_view.setHorizontalHeaderLabels(['Week', 'Start date', 'End data', 'Objective', 'status'])
        self.week_plan_view_header = self.week_plan_view.horizontalHeader()
        self.update_week_plan_table()
        # self.week_plan_view_header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        # self.week_plan_view.resizeColumnsToContents()

        self.week_plan_status_box = QtWidgets.QFrame(self.week_plan_box)
        self.week_plan_status_box_layout = QtWidgets.QHBoxLayout(self.week_plan_status_box)
        # =====
        # self.week_plan_progress_box = QChart()
        # self.week_plan_progress_box.legend().hide()
        # self.week_plan_progress_box.setBackgroundVisible(False)
        # self.week_progrss = QPieSeries()
        # self.week_progrss.setPieSize(1.0)
        
        # self.week_progrss.append('Pending', 1 - (1/4))
        # self.week_progrss.append('Done', (1/4))
        # self.week_progrss.setLabelsVisible(True)
        # self.week_progrss.setLabelsPosition(QPieSlice.LabelPosition.LabelInsideTangential)

        # self.week_plan_progress_box.setMinimumSize(200, 200)
        # self.week_plan_progress_box.addSeries(self.week_progrss)
        # self.week_plan_progress_view = QChartView(self.week_plan_progress_box)
        # self.week_plan_progress_view.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)

        # self.week_plan_status_box_layout.addWidget(self.week_plan_progress_view)
        # ====
        self.week_plan_box_layout.addWidget(self.week_plan_box_title)
        self.week_plan_box_layout.addWidget(self.week_plan_view)
        # self.week_plan_box_layout.addWidget(self.week_plan_status_box)

        self.month_plan_box = QtWidgets.QFrame(self.plan_view_box)
        self.month_plan_box_layout = QtWidgets.QVBoxLayout(self.month_plan_box)
        self.month_plan_box_title = QtWidgets.QLabel('Month')
        self.month_plan_view = QtWidgets.QTableWidget(self.plan_view_box)
        self.month_plan_view.setColumnCount(4)
        self.month_plan_view.setHorizontalHeaderLabels(['Start date', 'End data', 'Objective', 'status'])
        self.month_plan_box_layout.addWidget(self.month_plan_box_title)
        self.month_plan_box_layout.addWidget(self.month_plan_view)

        self.plan_box_view_box_layout.addWidget(self.week_plan_box)
        self.plan_box_view_box_layout.addWidget(self.month_plan_box)
        self.plan_box_layout.addWidget(self.plan_box_title)
        self.plan_box_layout.addWidget(self.plan_view_box)

        self.daily_tracking_box_layout.addWidget(self.daily_tracking_box_title)
        self.daily_tracking_box_layout.addWidget(self.daily_tracking_input_box)
        self.daily_tracking_box_layout.addWidget(self.daily_tracking_button_box)
        self.daily_tracking_box_layout.addWidget(self.plan_box)
        # self.daily_tracking_box_layout.addWidget(self.daily_tracking_sub_box)

        # Daily tracking view
        self.daily_tracking_view_box = QtWidgets.QFrame(self.daily_tracking_frame)
        self.daily_tracking_view_box.setObjectName('Daily-tracking-view-box')
        self.daily_tracking_view_box_layout = QtWidgets.QVBoxLayout(self.daily_tracking_view_box)
        self.daily_tracking_view_box_title = QtWidgets.QLabel('Daily tracking data')
        self.daily_tracking_view_box_title.setObjectName('daily-tracking-view-box-title')
        self.daily_tracking_view_table = QtWidgets.QTableWidget(self.daily_tracking_view_box)
        self.daily_tracking_view_table.setObjectName('daily-tracking-view-table')
        self.daily_tracking_view_table.setColumnCount(3)
        self.daily_tracking_view_table_header = self.daily_tracking_view_table.horizontalHeader()
        self.daily_tracking_view_table_header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.daily_tracking_view_table.setHorizontalHeaderLabels(['Date', 'Wakeup time', 'Sleepy time'])

        for data in self.daily_tracking_controller.show_data(1, 15):
            rows = self.daily_tracking_view_table.rowCount()
            self.daily_tracking_view_table.setRowCount(rows + 1)
            self.daily_tracking_view_table.setItem(rows, 0, QtWidgets.QTableWidgetItem(data[0]))
            self.daily_tracking_view_table.setItem(rows, 1, QtWidgets.QTableWidgetItem(data[1]))
            self.daily_tracking_view_table.setItem(rows, 2, QtWidgets.QTableWidgetItem(data[2]))
        self.daily_tracking_view_table.resizeColumnsToContents()
        self.daily_tracking_view_box_layout.addWidget(self.daily_tracking_view_box_title)
        self.daily_tracking_view_box_layout.addWidget(self.daily_tracking_view_table)
        
        self.daily_tracking_frame_layout.addWidget(self.daily_tracking_box)
        self.daily_tracking_frame_layout.addWidget(self.daily_tracking_view_box)

        # =====

        # Budget tracking frame
        self.budget_tracking_frame = QtWidgets.QFrame(self.main_frame)
        self.budget_tracking_frame.setObjectName('Budget-tracking-frame')
        self.budget_tracking_frame_layout = QtWidgets.QHBoxLayout(self.budget_tracking_frame)

        self.spent_tracking_frame = QtWidgets.QFrame()
        self.spent_tracking_frame.setObjectName('spent-tracking-frame')
        self.spent_tracking_frame_layout = QtWidgets.QHBoxLayout(self.spent_tracking_frame)
        self.spent_tracking_box = QtWidgets.QFrame(self.spent_tracking_frame)
        self.spent_tracking_box.setObjectName('spent-tracking-box')
        self.spent_tracking_box_layout = QtWidgets.QVBoxLayout(self.spent_tracking_box)
        self.spent_tracking_box_layout.setSpacing(25)
        self.spent_tracking_box_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.spent_tracking_box_title = QtWidgets.QLabel('Spent tracking')
        self.spent_tracking_input_box = QtWidgets.QFrame(self.spent_tracking_box)
        self.spent_tracking_input_box_layout = QtWidgets.QFormLayout(self.spent_tracking_input_box)
        self.spent_amount_label = QtWidgets.QLabel('Amount')
        self.spent_amount_label.setObjectName('spent-amount-label')
        self.spent_amount_input = QtWidgets.QLineEdit()
        self.spent_amount_input.setObjectName('spent-amount-input')
        self.spent_amount_remakrs_label = QtWidgets.QLabel('Remarks')
        self.spent_amount_remakrs_label.setObjectName('spent-amount-remakrs-label')
        self.spent_amount_remakrs_input = QtWidgets.QLineEdit()
        self.spent_amount_remakrs_input.setObjectName('spent-amount-remakrs-input')
        self.spent_tracking_input_box_layout.addRow(self.spent_amount_label,
                                                self.spent_amount_input)
        self.spent_tracking_input_box_layout.addRow(self.spent_amount_remakrs_label,
                                                self.spent_amount_remakrs_input)
        self.spent_tracking_button_box = QtWidgets.QFrame(self.spent_tracking_box)
        self.spent_tracking_button_box.setObjectName('spent-tracking-button-box')
        self.spent_tracking_button_box_layout = QtWidgets.QHBoxLayout(self.spent_tracking_button_box)
        self.spent_tracking_button_box_layout.setSpacing(8)
        self.spent_tracking_button_box_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.spent_tracking_save_btn = QtWidgets.QPushButton('Save')
        self.spent_tracking_save_btn.setObjectName('spent-tracking-save-btn')
        self.spent_tracking_save_btn.clicked.connect(self.confirm_save)
        self.spent_tracking_clear_btn = QtWidgets.QPushButton('Clear')
        self.spent_tracking_clear_btn.setObjectName('spent-tracking-clear-btn')
        self.spent_tracking_button_box_layout.addWidget(self.spent_tracking_clear_btn)
        self.spent_tracking_button_box_layout.addWidget(self.spent_tracking_save_btn)

        self.spent_tracking_box_layout.addWidget(self.spent_tracking_box_title)
        self.spent_tracking_box_layout.addWidget(self.spent_tracking_input_box)
        self.spent_tracking_box_layout.addWidget(self.spent_tracking_button_box)

        # Spent view
        self.spent_tracking_view_box = QtWidgets.QFrame(self.spent_tracking_frame)
        self.spent_tracking_view_box.setObjectName('spent-tracking-view-box')
        self.spent_tracking_view_box_layout = QtWidgets.QVBoxLayout(self.spent_tracking_view_box)
        self.spent_tracking_view_box_title = QtWidgets.QLabel('Spent tracking data')
        self.spent_tracking_view_box_title.setObjectName('spent-tracking-view-box-title')
        self.spent_tracking_view_box_filter_box = QtWidgets.QFrame(self.spent_tracking_view_box)
        self.spent_tracking_view_box_filter_box.setObjectName('spent-tracking-view-box-filter-box')
        self.spent_tracking_view_box_filter_box_layout = QtWidgets.QHBoxLayout(self.spent_tracking_view_box_filter_box)
        self.spent_tracking_view_box_month_filter_label = QtWidgets.QLabel('Month')
        self.spent_tracking_view_box_month_filter_label.setObjectName('spent-tracking-view--box-month-filter-label')
        self.spent_tracking_view_box_month_filter_input = QtWidgets.QComboBox(self.spent_tracking_view_box_filter_box)
        self.spent_tracking_view_box_month_filter_input.setObjectName('spent-tracking-view-box-month-filter-input')
        self.spent_tracking_view_box_year_filter_label = QtWidgets.QLabel('Year')
        self.spent_tracking_view_box_year_filter_label.setObjectName('spent-tracking-view--box-year-filter-label')
        self.spent_tracking_view_box_year_filter_input = QtWidgets.QComboBox(self.spent_tracking_view_box_filter_box)
        self.spent_tracking_view_box_year_filter_input.setObjectName('spent-tracking-view-box-year-filter-input')
        self.spent_tracking_view_box_filter_box_layout.addWidget(self.spent_tracking_view_box_month_filter_label)
        self.spent_tracking_view_box_filter_box_layout.addWidget(self.spent_tracking_view_box_month_filter_input)
        self.spent_tracking_view_box_filter_box_layout.addWidget(self.spent_tracking_view_box_year_filter_label)
        self.spent_tracking_view_box_filter_box_layout.addWidget(self.spent_tracking_view_box_year_filter_input)
        self.spent_tracking_view_box_table = QtWidgets.QTableWidget(self.spent_tracking_view_box)
        self.spent_tracking_view_box_table.setObjectName('spent-tracking-view-box-table')
        self.spent_tracking_view_box_table.setColumnCount(2)
        self.spent_tracking_view_box_table_header = self.spent_tracking_view_box_table.horizontalHeader()
        self.spent_tracking_view_box_table_header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.spent_tracking_view_box_table.setHorizontalHeaderLabels(['Amount', 'Remarks'])
        self.spent_tracking_view_box_table.setWordWrap(True)
        for data in self.spent_tracking_controller.show_data(1, 30):
            rows = self.spent_tracking_view_box_table.rowCount()
            self.spent_tracking_view_box_table.setRowCount(rows + 1)
            self.spent_tracking_view_box_table.setItem(rows, 0, QtWidgets.QTableWidgetItem(str(data[0])))
            self.spent_tracking_view_box_table.setItem(rows, 1, QtWidgets.QTableWidgetItem(data[1]))
        self.spent_tracking_view_box_table.resizeColumnsToContents()
        self.spent_tracking_view_box_table.resizeRowsToContents()

        self.spent_tracking_view_box_layout.addWidget(self.spent_tracking_view_box_title)
        self.spent_tracking_view_box_layout.addWidget(self.spent_tracking_view_box_filter_box)
        self.spent_tracking_view_box_layout.addWidget(self.spent_tracking_view_box_table)


        self.spent_tracking_frame_layout.addWidget(self.spent_tracking_box)
        self.spent_tracking_frame_layout.addWidget(self.spent_tracking_view_box)

        self.income_tracking_frame = QtWidgets.QFrame()
        self.income_tracking_frame.setObjectName('income-tracking-frame')
        self.income_tracking_frame_layout = QtWidgets.QHBoxLayout(self.income_tracking_frame)
        self.income_tracking_box = QtWidgets.QFrame(self.income_tracking_frame)
        self.income_tracking_box.setObjectName('income-tracking-box')
        self.income_tracking_box_layout = QtWidgets.QVBoxLayout(self.income_tracking_box)
        self.income_tracking_box_layout.setSpacing(25)
        self.income_tracking_box_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.income_tracking_box_title = QtWidgets.QLabel('Income tracking')
        self.income_tracking_box_title.setObjectName('income-tracking-box-title')
        self.income_tracking_input_box = QtWidgets.QFrame(self.income_tracking_box)
        self.income_tracking_input_box_layout = QtWidgets.QFormLayout(self.income_tracking_input_box)
        self.income_amount_label = QtWidgets.QLabel('Amount')
        self.income_amount_label.setObjectName('income-amount-label')
        self.income_amount_input = QtWidgets.QLineEdit()
        self.income_amount_input.setObjectName('income-amount-input')
        self.income_amount_remarks_label = QtWidgets.QLabel('Remarks')
        self.income_amount_remarks_label.setObjectName('income-amount-remarks-label')
        self.income_amount_remarks_input = QtWidgets.QLineEdit()
        self.income_amount_remarks_input.setObjectName('income-amount-remarks-input')
        self.income_tracking_input_box_layout.addRow(self.income_amount_label,
                                                self.income_amount_input)
        self.income_tracking_input_box_layout.addRow(self.income_amount_remarks_label,
                                                self.income_amount_remarks_input)
        self.income_tracking_button_box = QtWidgets.QFrame(self.income_tracking_box)
        self.income_tracking_button_box.setObjectName('income-tracking-button-box')
        self.income_tracking_button_box_layout = QtWidgets.QHBoxLayout(self.income_tracking_button_box)
        self.income_tracking_button_box_layout.setSpacing(8)
        self.income_tracking_button_box_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.income_tracking_save_btn = QtWidgets.QPushButton('Save')
        self.income_tracking_save_btn.setObjectName('income-tracking-save-btn')
        self.income_tracking_clear_btn = QtWidgets.QPushButton('Clear')
        self.income_tracking_clear_btn.setObjectName('income-tracking-clear-btn')
        self.income_tracking_button_box_layout.addWidget(self.income_tracking_clear_btn)
        self.income_tracking_button_box_layout.addWidget(self.income_tracking_save_btn)

        self.income_tracking_box_layout.addWidget(self.income_tracking_box_title)
        self.income_tracking_box_layout.addWidget(self.income_tracking_input_box)
        self.income_tracking_box_layout.addWidget(self.income_tracking_button_box)

        # Income tracking view box
        self.income_tracking_view_box = QtWidgets.QFrame()
        self.income_tracking_view_box.setObjectName('income-tracking-view-box')
        self.income_tracking_view_box_layout = QtWidgets.QVBoxLayout(self.income_tracking_view_box)
        self.income_tracking_view_box_title = QtWidgets.QLabel('Income tracking data')
        self.income_tracking_view_box_title.setObjectName('income-tracking-view-box-title')
        self.income_tracking_view_box_table = QtWidgets.QTableWidget(self.income_tracking_view_box)
        self.income_tracking_view_box_table.setObjectName('income-tracking-view-box-table')
        self.income_tracking_view_box_table.setColumnCount(2)
        self.income_tracking_view_box_table_hader = self.income_tracking_view_box_table.horizontalHeader()
        self.income_tracking_view_box_table_hader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.income_tracking_view_box_table.setHorizontalHeaderLabels(['Amount', 'Remarks'])
        for data in self.income_tracking_controller.show_data(1, 15):
            rows = self.income_tracking_view_box_table.rowCount()
            self.income_tracking_view_box_table.setRowCount(rows + 1)
            self.income_tracking_view_box_table.setItem(rows, 0, QtWidgets.QTableWidgetItem(str(data[0])))
            self.income_tracking_view_box_table.setItem(rows, 1, QtWidgets.QTableWidgetItem(data[1]))
        self.income_tracking_view_box_table.resizeColumnsToContents()
        self.income_tracking_view_box_layout.addWidget(self.income_tracking_view_box_title)
        self.income_tracking_view_box_layout.addWidget(self.income_tracking_view_box_table)

        self.income_tracking_frame_layout.addWidget(self.income_tracking_box)
        self.income_tracking_frame_layout.addWidget(self.income_tracking_view_box)


        self.budget_tracking_frame_layout.addWidget(self.spent_tracking_frame)
        self.budget_tracking_frame_layout.addWidget(self.income_tracking_frame)

        # =====

        self.central_layout.addWidget(self.daily_tracking_frame)
        self.central_layout.addWidget(self.budget_tracking_frame)


    def close_app(self):
        self.close()


    def confirm_save(self):
        confirm_box = QtWidgets.QMessageBox(self)
        confirm_box.setWindowTitle('Spent tracking')
        confirm_box.setMinimumHeight(1200)
        confirm_box.setInformativeText('Do you want to save the spent tracking')

        confirm_box.show()


    # Should make this as modal
    def open_about_window(self):
        self.about_window = AboutWindow()
        self.about_window.show()

    
    def open_planner_window(self):
        self.planner_window = PlannerWindow()
        self.planner_window.show()

    def open_wakeup_time_backup_window(self):
        wakeup_time_box = QtWidgets.QInputDialog(self, Qt.WindowType.FramelessWindowHint)
        wakeup_time_box.setLabelText('Wakeup time')
        wakeup_time_box.setOkButtonText('Save')
        wakeup_time_box.textValueSelected.connect(lambda: self.backup_wakeup_time(wakeup_time_box.textValue()))
        target = self.rect()
        target_x = target.center().x()
        target_y = target.center().y()
        wakeup_time_box.move(QtCore.QPoint(target_x, target_y))

        wakeup_time_box.exec()


    def backup_wakeup_time(self, time: str):
        status = self.wakeup_time_backup_controller.save_wakeup_time(time)

        if status:
            self.app_statusbar.showMessage('Wakeup time backup successfull')
        else:
            self.app_statusbar.showMessage('Wakeup time backup unsuccessfull')


    def open_log_window(self):
        self.app_statusbar.showMessage('Logfile view open')


    def update_week_plan_table(self):
        month_plan_data = self.week_planner_controller.show_week_plans(QtCore.QDate.currentDate().toPyDate())
        if month_plan_data:
            for data in month_plan_data:
                rows = self.week_plan_view.rowCount()
                self.week_plan_view.setRowCount(rows + 1)
                self.week_plan_view.setItem(rows, 0, QtWidgets.QTableWidgetItem(str(rows + 1)))
                self.week_plan_view.setItem(rows, 1, QtWidgets.QTableWidgetItem(data[0]))
                self.week_plan_view.setItem(rows, 2, QtWidgets.QTableWidgetItem(data[1]))
                self.week_plan_view.setItem(rows, 3, QtWidgets.QTableWidgetItem(data[2]))
                self.week_plan_view.setItem(rows, 4, QtWidgets.QTableWidgetItem(data[3]))        