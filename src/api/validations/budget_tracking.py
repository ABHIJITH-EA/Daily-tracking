""" Validations for budget tracking activities """

from base.datetime_utils import current_date, to_db_date
from database import connector


class BudgetTrackingValidation:
    
    table = 'budget_tracking'

    @staticmethod
    def is_firsttime_today():
        """ Checks if it's using for the, first time today.
        """
        mysql_db = connector.connect(driver='mysql')
        
        day = to_db_date(current_date())
        
        stm = f"SELECT id FROM {BudgetTrackingValidation.table} WHERE day='{day}';"
        
        # BUG: Not logical
        if not mysql_db.execute(stm):
            return False

        status = mysql_db.first_row()

        return True if status is None else False