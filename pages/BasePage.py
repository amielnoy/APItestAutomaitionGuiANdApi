# import logging
from tokenize import String

import allure

from Utils.Reporting.Reporting import Reporting
from logManager import logManager


class BasePage:
    def __init__(self, page, url):
        self.url = url
        self.page = page
        self.logger = logManager().get_logger_instance()

    def navigate_to_url(self):
        Reporting.report_allure_and_logger("INFO", "Starting   navigating to url %s" % self.url)
        self.page.goto(self.url)
        Reporting.report_allure_and_logger("INFO", "Finished  navigating to url %s" % self.url)

    def get_page_url(self):
        Reporting.report_allure_and_logger("INFO", "returning page url")
        return self.page.url

    def verify_page_title(self, page, expected_web_page_title):
        allure.step("verifying current web page title")
        actual_page_title = page.title()
        self.logger.info("trying to verify current web page title == " + actual_page_title)
        assert actual_page_title == expected_web_page_title
        self.logger.info("verified current web page title == " + actual_page_title)

    @allure.step("verifying current web page url {1}")
    def verify_url(self, expected_url):
        allure.step("verifying current web page url")
        self.logger.info("trying to verify current web page url == " + str(self.get_page_url()))
        assert self.get_page_url() == expected_url
        self.logger.info("verified current web page url == " + str(self.get_page_url()))

    @allure.step("verifying current web page url {1}")
    def verify_is_url_prefix(self, expected_url_prefix):
        allure.step("verifying current web page url")
        self.logger.info("trying to verify current web page url == " + str(self.get_page_url()))
        try:
            assert self.get_page_url().startswith(expected_url_prefix)
            self.logger.info("verified current web page url == " + str(self.get_page_url()))
            return True
        except:
            return False

    def build_locator_string(self, gui_item_position, locator_prefix_string, locator_suffix_string) -> String:
        if gui_item_position != -1:
            return locator_prefix_string + str(gui_item_position) + locator_suffix_string
        else:
            return locator_prefix_string + locator_suffix_string
