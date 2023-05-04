"""
This module contains login_page,
the page object for the xray login page.
"""
import string

import allure

from Utils.Reporting.Reporting import Reporting
from pages.BasePage import BasePage


class HelpPage(BasePage):

    def __init__(self, page, help_url):
        self.page = page
        self.main_help_center_line1_text_acronis = page.locator("text=Welcome to the Advanced Email Security")
        self.main_help_center_line1_text_xray = page.locator("text=Welcome to the Perception Point")
        self.main_help_center_line2_text = page.locator("text=Documentation Center")
        self.main_middle_search = page.get_by_title("Search now...")
        super().__init__(self.page, help_url)

    @allure.step("Setting help keyword to search for")
    def set_keyword_to_search_help(self, help_keyword):
        Reporting.report_allure_and_logger("INFO", f"Started Setting help keyword to search for={help_keyword}")
        self.page.locator("[placeholder=\"Search\\ the\\ documentation center\"]").nth(1).fill(help_keyword)
        Reporting.report_allure_and_logger("INFO", f"Finished Setting help keyword to search for={help_keyword}")

    @allure.step("Clicking search button on MAIN HELP page")
    def click_search_help_keyword(self) -> None:
        Reporting.report_allure_and_logger("INFO", "Starting CLICKING search button on MAIN HELP page")
        self.page.wait_for_timeout(10000)
        self.main_middle_search.nth(1).click()
        self.page.wait_for_timeout(10000)
        Reporting.report_allure_and_logger("INFO", "Finished  CLICKING search button on MAIN HELP page")

    @allure.step("Getting text of connect_granting_us_permissions_label_text in SET SCANNED EMAIL page")
    def get_connect_granting_us_permissions_label_text(self) -> string:
        Reporting.report_allure_and_logger("INFO",
                                           "Getting text of connect_granting_us_permissions_label_text in SET SCANNED EMAIL page")
        return self.granting_us_permissions.text_content()

    @allure.step("Getting line1 text of  ACRONIS main help page_text in SET SCANNED EMAIL page")
    def get_acronis_main_help_page_line1_text(self, is_acronis) -> string:
        Reporting.report_allure_and_logger("INFO",
                                           "Getting line1 text of ACRONIS main help page_text in SET SCANNED EMAIL page")
        if is_acronis:
            return self.main_help_center_line1_text_acronis.text_content()
        else:
            return self.main_help_center_line1_text_xray.text_content()

    @allure.step("Getting line2 text of  ACRONIS main help page_text in SET SCANNED EMAIL page")
    def get_acronis_main_help_page_line2_text(self) -> string:
        Reporting.report_allure_and_logger("INFO",
                                           "Getting line2 text of ACRONIS main help page_text in SET SCANNED EMAIL page")
        return self.main_help_center_line2_text.text_content()

    def get_page(self):
        return self.page
