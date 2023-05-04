"""
This module contains login_page,
the page object for the xray login page.
"""
import string

import allure

from Utils.Reporting.Reporting import Reporting
from pages.BasePage import BasePage


class CompleteOffice365ConfigurationPage(BasePage):

    def __init__(self, page):
        self.page = page
        self.complete_gmail_configuration_label = page.locator(
            "text=Please follow these steps to complete your Gmail configuration:")
        self.label_user_microsoft_login = page.locator("text=atp@office365.ecknhhk.xyz")
        self.input_office_user_microsoft_login = page.locator("id=i0116")
        self.input_microsoft_password = page.get_by_placeholder("Password")
        self.sign_in_button = page.get_by_placeholder("text=Sign in")
        self.gmail_configuration_mail_input = page.locator("[placeholder=\"Your Email\"]")
        self.office_next_button = page.locator('text=next')

        super().__init__(self.page, "")

    @allure.step("Clicking next button on first connection page,no parameters")
    def click_office365_user(self) -> None:
        Reporting.report_allure_and_logger("INFO",
                                           "Started clicking OFFICE365 username on office365 complete integration wizard PAGE")
        self.label_user_microsoft_login.click()
        Reporting.report_allure_and_logger("INFO",
                                           "Finished SETTING GMAIL CONFIGURATION MAIL on CONNECTION WIZARD PAGE")

    @allure.step("Clicking next button on first connection page,no parameters")
    def set_office365_configuration_mail(self, office_user_configuration_mail) -> None:
        Reporting.report_allure_and_logger("INFO", "Started SETTING GMAIL CONFIGURATION MAIL on CONNECTION WIZARD PAGE")
        self.page.pause()

        self.input_office_user_microsoft_login.fill('')
        self.input_office_user_microsoft_login.fill(office_user_configuration_mail)
        Reporting.report_allure_and_logger("INFO",
                                           "Finished SETTING GMAIL CONFIGURATION MAIL on CONNECTION WIZARD PAGE")

    @allure.step("Clicking next button on first connection page,no parameters")
    def set_office365_configuration_password(self, office365_configuration_password) -> None:
        Reporting.report_allure_and_logger("INFO", "Started SETTING GMAIL CONFIGURATION MAIL on CONNECTION WIZARD PAGE")
        self.off.fill('')
        self.gmail_configuration_mail_input.fill(office365_configuration_password)
        Reporting.report_allure_and_logger("INFO",
                                           "Finished SETTING GMAIL CONFIGURATION MAIL on CONNECTION WIZARD PAGE")

    @allure.step("Clicking next button on first connection page,no parameters")
    def click_next_button(self) -> None:
        Reporting.report_allure_and_logger("INFO", "Started clicking NEXT BUTTON on CONNECTION WIZARD PAGE")
        self.input_office_user_microsoft_login.click()
        Reporting.report_allure_and_logger("INFO", "Finished clicking NEXT BUTTON on CONNECTION WIZARD PAGE")

    @allure.step("Clicking next button on first connection page")
    def click_next_button_enable(self, service) -> None:
        Reporting.report_allure_and_logger("INFO",
                                           f'Started clicking Enable {service} app BUTTON on CONNECTION WIZARD PAGE')
        next_button = self.page.locator("text=Enable " + service + " APP")
        next_button.click()
        Reporting.report_allure_and_logger("INFO",
                                           f'Finished clicking Enable {service} app BUTTON on CONNECTION WIZARD PAGE')

    def click_sign_in_button(self) -> None:
        Reporting.report_allure_and_logger("INFO", "Started clicking ***SIGN IN** BUTTON on CONNECTION WIZARD PAGE")
        self.sign_in_button.click()
        Reporting.report_allure_and_logger("INFO", "Finished clicking ***SIGN IN** BUTTON on CONNECTION WIZARD PAGE")

    @allure.step("Getting text of highest control\n in first connection wizard page")
    def get_complete_gmail_configuration_label_text(self) -> string:
        Reporting.report_allure_and_logger("INFO", "getting complete gmail configuration text_content")
        return self.complete_gmail_configuration_label.text_content()
