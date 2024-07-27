from Utils.Time.Time import Time

import allure
from allure_commons.types import AttachmentType

from LogManager import LogManager


class Reporting:
    logger = LogManager().get_logger_instance()

    @staticmethod
    def take_screenshot_and_add_to_report(page, testname):
        # TODO create date folder at screenshots/curr_date
        # TODO create screan shot under the new folder
        time_stamp = Time.get_current_time().replace(":", "_")
        test_screenshot_path = "test_output/screenshots/screenshot_" + testname + "_" + time_stamp + ".png"
        allure.attach(page.screenshot(path=test_screenshot_path, full_page=True), name="regular screenshot/Failure "
                                                                                       "screenshot if FAILED)",
                      attachment_type=AttachmentType.PNG)


    @staticmethod
    @allure.step("{0},{1}")
    def report_allure_and_logger(log_type, log_message):
        if log_type == "INFO":
            Reporting.logger.info(log_message)
            allure.step("INFO: "+log_message)
        elif log_type == "WARNING":
            Reporting.logger.warning(log_message)
            allure.step("WARNING: " + log_message)
        elif log_type == "ERROR":
            Reporting.logger.error(log_message)
            allure.step("ERROR: " + log_message)
        elif log_type == "CRITICAL":
            Reporting.logger.critical(log_message)
            allure.step("CRITICAL: " + log_message)