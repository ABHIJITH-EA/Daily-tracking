""" API for budget tracking activities """

from database import connector
from database.models.budget_tracking import BudgetTrackingModel
from database.driver.mysql import MysqlDb

class BudgetTracking:

    def __init__(self) -> None:
        self.mysql_db:MysqlDb = connector.connect(driver='mysql')
        self.model = BudgetTrackingModel()

    
    def get_id(self, day:str) -> int:
        """ Find id of a specific day
            :returns int
        """
        colums = [self.model.id]
        where_column = self.model.day

        id = self.mysql_db.select(self.model.table,
                        colums)

        return id