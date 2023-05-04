import string
from datetime import datetime


class Time:
    @staticmethod
    def get_current_time() -> string:
        now = datetime.now()
        current_time = now.strftime("%H_%M_%S")
        # print(f"Current Date Time ={current_time}")
        return current_time

    @staticmethod
    def get_current_date() -> string:
        now = datetime.now().date()
        current_time = now.strftime("%Y_%m_%d")
        # print(f"Current Date Time ={current_time}")
        return current_time

    @staticmethod
    def get_current_date_time() -> string:
        now = datetime.now()
        current_date_time = now.strftime("%Y_%m_%d_%H_%M_%S")
        # print(f"Current Date Time ={current_date_time}")
        return current_date_time
