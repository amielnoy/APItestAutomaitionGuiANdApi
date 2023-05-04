"""
This module contains login_page,
the page object for the xray login page.
"""
import string

import allure

from Utils.Reporting.Reporting import Reporting
from pages.BasePage import BasePage


class CompleteGmailConfigurationPage(BasePage):

    def __init__(self, page):
        self.page = page
        self.complete_gmail_configuration_label = page.locator(
            "text=Please follow these steps to complete your Gmail configuration:")
        self.gmail_configuration_mail_input = page.get_by_placeholder("Your Email")

        super().__init__(self.page, "")

    @allure.step("Clicking next button on first connection page,no parameters")
    def set_gmail_configuration_mail(self, gmail_configuration_mail) -> None:
        Reporting.report_allure_and_logger("INFO", "Started SETTING GMAIL CONFIGURATION MAIL on CONNECTION WIZARD PAGE")
        # self.gmail_configuration_mail_input.fill('')
        # self.page.pause()
        self.gmail_configuration_mail_input.fill(gmail_configuration_mail)
        Reporting.report_allure_and_logger("INFO",
                                           "Finished SETTING GMAIL CONFIGURATION MAIL on CONNECTION WIZARD PAGE")
    @allure.step("Clicking next button on first connection page,no parameters")
    def click_next_button(self) -> None:
        Reporting.report_allure_and_logger("INFO", "Started clicking NEXT BUTTON on CONNECTION WIZARD PAGE")
        next_button = self.page.locator("text=Next")
        next_button.click()
        Reporting.report_allure_and_logger("INFO", "Finished clicking NEXT BUTTON on CONNECTION WIZARD PAGE")

    @allure.step("Clicking next button on first connection page")
    def click_next_button_enable(self, service) -> None:
        Reporting.report_allure_and_logger("INFO", f'Started clicking Enable {service} app BUTTON on CONNECTION WIZARD PAGE')
        next_button = self.page.locator("text=Enable " + service + " APP")
        next_button.click()
        Reporting.report_allure_and_logger("INFO",
                                           f'Finished clicking Enable {service} app BUTTON on CONNECTION WIZARD PAGE')

    @allure.step("Getting text of highest control\n in first connection wizard page")
    def get_complete_gmail_configuration_label_text(self) -> string:
        Reporting.report_allure_and_logger("INFO", "getting complete gmail configuration text_content")
        return self.complete_gmail_configuration_label.text_content()
