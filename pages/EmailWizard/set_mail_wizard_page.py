"""
This module contains login_page,
the page object for the xray login page.
"""
import string

import allure

from Utils.Reporting.Reporting import Reporting
from pages.BasePage import BasePage


class set_scanned_mail(BasePage):

    def __init__(self, page):
        self.page = page
        self.granting_us_permissions = page.locator("text=Granting us permissions for gmail integration")
        self.input_email=page.locator("[placeholder=\"Your\\ Email\"]")
        self.next_button = page.locator("text=Next")
        super().__init__(self.page, "")

    @allure.step("Setting scanned email")
    def set_mail(self, email):
        Reporting.report_allure_and_logger("INFO",f"Setting scanned email={email}")
        self.input_email.fill("")
        self.input_email.fill(email)

    @allure.step("Clicking next button on SET SCANNED EMAIL page")
    def click_next_button(self) -> None:
        self.next_button.click()
        Reporting.report_allure_and_logger("INFO","Finished Clicking next button on SET SCANNED EMAIL page")

    @allure.step("Getting text of connect_granting_us_permissions_label_text in SET SCANNED EMAIL page")
    def get_connect_granting_us_permissions_label_text(self) -> string:
        Reporting.report_allure_and_logger("INFO", "Getting text of connect_granting_us_permissions_label_text in SET SCANNED EMAIL page")
        return self.granting_us_permissions.text_content()
