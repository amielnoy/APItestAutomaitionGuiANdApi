from datetime import datetime


class ComapreTimeStamp:
    @staticmethod
    def is_last_scan_series_match(top_scan_time_stamp):
        top_scan_date = top_scan_time_stamp.split("|")[0]
        top_scan_time = top_scan_time_stamp.split("|")[1]
        month_name = datetime.strptime(top_scan_date.split(" ")[0], '%b').month

        current_date_time = datetime.now()
        if current_date_time.month == month_name \
                and current_date_time.day == int(top_scan_date.split(" ")[1]) \
                and str(current_date_time.hour) == top_scan_time.split(":")[0] \
                and ((current_date_time.minute)) >= int(top_scan_time.split(":")[1]) \
                or current_date_time.minute - 5 <= int(top_scan_time.split(":")[1]):
            return True
        else:
            return False
