""" Validations for daily tracking activities """


class DailyTrackingValidation:

    @staticmethod
    def wakeup_time(time: str) -> bool:
        return True


    @staticmethod
    def sleepy_time(time: str) -> bool:
        return True