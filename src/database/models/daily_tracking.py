
class DailyTrackingModel:
    __table = 'daily_tracking'

    __id = 'id'
    __day = 'day'
    __wakeup_time = 'wakeup_time'
    __sleepy_time = 'sleepy_time'
    __created_at = 'created_at'
    __updated_at = 'updated_at'
    __deleted_at = 'deleted_at'
    __created_by = 'created_by'
    __updated_by = 'updated_by'
    __deleated_by = 'deleated_by'

    
    def __init__(self):
        pass