"""
This module contains login_page,
the page object for the xray login page.
"""

import allure

from Utils.Reporting.Reporting import Reporting
from pages.BasePage import BasePage


class HelpSearchResultsPage(BasePage):

    def __init__(self, page, help_url):
        self.page = page
        self.resultHeading = page.locator("text=Your search for ")
        # self.acronis_logo = page.locator("text=")
        # self.search_help_keyword=page.locator("[placeholder=\"Search\\ the\\ documentation center\"]")

        # self.search_button= page.get_by_title("Search now...")
        super().__init__(self.page, help_url)

    @allure.step("Setting help keyword to search for")
    def set_keyword_to_search_help(self, help_keyword):
        Reporting.report_allure_and_logger("INFO", f"Setting help keyword to search for={help_keyword}")
        # self.search_help_keyword.nth(0).fill("")
        # self.search_help_keyword.nth(0).fill(help_keyword)

    @allure.step("Clicking search button on MAIN HELP page")
    def click_search_help_keyword(self) -> None:
        Reporting.report_allure_and_logger("INFO", "Starting search button on MAIN HELP page")
        # self.search_button.nth(0).click()
        Reporting.report_allure_and_logger("INFO", "Finished search button on MAIN HELP page")
