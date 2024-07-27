"""
This module contains login_page,
the page object for the xray login page.
"""
import string

import allure

from Utils.Reporting.Reporting import Reporting
from pages.BasePage import BasePage


class NewMailServiceWizardPage(BasePage):

    def __init__(self, page):
        self.page = page
        self.connect_new_service = page.locator("text=Add a New Service")

        self.organization = page.locator("text=Organizationamiel.noyfeld >> select")

        self.check_office365_service = page.locator("label").filter(has_text="Office365")
        self.check_gmail_service = page.locator("label").filter(has_text="Gmail")
        super().__init__(self.page, "")

    @allure.step("Setting organization name")
    def set_organisation(self, organization):
        Reporting.report_allure_and_logger("INFO", f'Setting organization name={organization}')
        self.organization.select_option(organization)

    @allure.step
    def click_gmail_service(self):
        Reporting.report_allure_and_logger("INFO", "Checking radio button gmail on CONNECTION WIZARD PAGE")
        self.check_gmail_service.click()

    @allure.step
    def click_office365_service(self) -> None:
        Reporting.report_allure_and_logger("INFO", "checking radio button office 365 on CONNECTION WIZARD PAGE")
        self.check_office365_service.click()

    @allure.step("Clicking next button on first connection page,no parameters")
    def click_next_button(self) -> None:
        next_button = self.page.locator("text=Next")
        next_button.click()
        Reporting.report_allure_and_logger("INFO", "Finished clicking NEXT BUTTON on CONNECTION WIZARD PAGE")

    @allure.step("Clicking next button on first connection page")
    def click_next_button_enable(self, service) -> None:
        next_enable_button = self.page.get_by_role("button", name="ENABLE " + service + " APP")
        # self.page.pause()
        next_enable_button.click()
        Reporting.report_allure_and_logger("INFO",
                                           f'Finished clicking Enable {service} app BUTTON on CONNECTION WIZARD PAGE')

    @allure.step("Getting text of highest control\n in first connection wizard page")
    def get_connect_new_service_label_text(self) -> string:
        Reporting.report_allure_and_logger("INFO", "getting connect_new_service control text_content")
        return self.connect_new_service.text_content()
