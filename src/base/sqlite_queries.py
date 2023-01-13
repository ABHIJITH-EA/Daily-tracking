""" SQLITE helper Queries"""

TABLE_NAME = 'app_database_status'
WAKEUP_BACKUP_TIME_TABLE_NAME = 'wakeup_time_backup'

# TODO: Fix redundancy
APP_DB_TABLE_ACTIVATE = f"UPDATE {TABLE_NAME} SET \
         status = 'ACTIVE' WHERE component_name='database_tables';"

APP_DB_TABLE_DEACTIVATE = f"UPDATE {TABLE_NAME} SET \
         status = 'INACTIVE' WHERE component_name='database_tables';"

APP_DB_TABLE_STATUS_SELECT = f"SELECT status FROM {TABLE_NAME} LIMIT 1;"


# Wakeup backup queries
INSERT_WAKEUP_TIME = f"INSERT INTO {WAKEUP_BACKUP_TIME_TABLE_NAME}"