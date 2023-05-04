import string
from pathlib import Path

from Utils import DataDrriven
from test_base import BaseTest


class ScanBase:
    PASSWORD_PROTECTED_SCANS_COMPLETEION_TIME_OUT = 120000
    PASSWORD_LESS_SCANS_COMPLETEION_TIME_OUT = 200000
    SCANS_COMPLETEION_EXTRA_ALL_SCANS_TIME_OUT = 30000
    FILE_UPLOAD_TIME_OUT = 60000
    WAIT_FOR_SET_SCAN_FILE_SEARCH_TIMEOUT = 30000
    SEARCH_SCAN_BUTTON_MAX_TIME = 10000

    @staticmethod
    def get_project_root() -> Path:
        return Path(__file__).parent.parent

    @classmethod
    def get_csv_path_for_files(cls, csv_file_name) -> string:
        return str(
            cls.get_project_root().parent) + "/tests/SelfAnalyze/File/Data/" + csv_file_name  # files_to_scan_acronis_password_less.csv"

    @classmethod
    def get_csv_path_for_urls(cls, csv_file_name) -> string:
        if csv_file_name == "urls_to_scan_acronis.csv" or csv_file_name == "urls_to_scan_xray.csv":
            return str(
                cls.get_project_root().parent) + "/tests/SelfAnalyze/Url/Data/" + csv_file_name  # files_to_scan_acronis_password_less.csv"
        else:
            return str(
                cls.get_project_root()) + "/SelfAnalyze/Url/Data/" + csv_file_name  # files_to_scan_acronis_password_less.csv"
