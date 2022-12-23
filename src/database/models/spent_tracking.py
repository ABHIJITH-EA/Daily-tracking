
from database.models.budget_tracking import BudgetTrackingModel

class SpentTrackingModel(BudgetTrackingModel):
    table = 'spent'

    id = 'id'
    budgeting_id = 'budgeting_id'
    amount = 'amount'
    remarks = 'remarks'
    created_at = 'created_at'
    updated_at = 'updated_at'
    deleted_at = 'deleted_at'
    created_by = 'created_by'
    updated_by = 'updated_by'
    deleated_by = 'deleated_by'

    def __init__(self) -> None:
        super().__init__()