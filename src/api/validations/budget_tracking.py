""" Validations for budget tracking activities """

from base.datetime_utils import current_date, to_db_date
from database import connector


class BudgetTrackingValidation:
    
    __table = 'budget_tracking'


    def __init__(self) -> None:
        pass

    def is_firsttime_today(self):
        """ Checks if it's using for the, first time today.
        """
        mysql_db = connector.connect(driver='mysql')
        
        day = to_db_date(current_date())
        
        stm = f"SELECT id FROM {BudgetTrackingValidation.__table} WHERE day='{day}';"
        
        # BUG: Not logical
        if not mysql_db.execute(stm):
            return False

        status = mysql_db.first_row()

        return True if status is None else False

    def is_proper_data(self, data: list):
        amount = data[0]
        remarks = data[1]

        try:
            amount = int(amount)
        except ValueError as e:
            return False

        return True