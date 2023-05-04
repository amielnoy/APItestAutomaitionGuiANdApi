"""
This module contains login_page,
the page object for the xray login page.
"""
import string

import allure

from Utils import Reporting
from Utils.Reporting.Reporting import Reporting
from pages.BasePage import BasePage


class NewServiceWizardAddDomain(BasePage):

    def __init__(self, page):
        self.page = page
        self.domains = page.locator("label:has-text(\"Domains\")")

        self.host = page.locator("[placeholder=\"Host\"]")
        self.find_domain_smtp_server = page.locator("text=Domains Add Domain >> svg >> nth=1")
        self.user_licenses_per_domain = page.locator("input[type=\"number\"]>>nth=0")
        self.accounts = page.locator("text=Number of Accounts (recommended for best protection)")
        self.next_button = page.locator("text=Next")

        super().__init__(self.page, "")

    @allure.step("Setting host name on CONNECTION SERVICE ADD DOMAIN PAGE")
    def set_host(self, host):
        allure.step("Setting host name=" + host)
        self.host.fill("")
        self.host.fill(host)
        self.logger.info("Finished Setting " + host + " edit on CONNECTION SERVICE ADD DOMAIN PAGE")

    @allure.step
    def click_find_domain_smtp_server(self):
        Reporting.report_allure_and_logger("INFO", "clicking find_domain_smtp_server from ADD DOMAIN page(ACRONIS)")
        self.find_domain_smtp_server.click()

    @allure.step("clicking accounts radio button from ADD DOMAIN page(ACR)")
    def click_accounts(self):
        Reporting.report_allure_and_logger("INFO", "Start clicking accounts radio button from ADD DOMAIN page(ACR)")
        self.accounts.click()
        Reporting.report_allure_and_logger("INFO", "Finish clicking accounts radio button from ADD DOMAIN page(ACR)")

    @allure.step("set user licenses per domain{1}")
    def set_user_licenses_per_domain(self, user_licenses_per_domain):
        Reporting.report_allure_and_logger("INFO", f'set user licenses per domain=={user_licenses_per_domain}')
        self.user_licenses_per_domain.fill("")
        self.user_licenses_per_domain.fill(user_licenses_per_domain)
        return self.user_licenses_per_domain.input_value()

    @allure.step("Clicking next button on ADD DOMAIN page")
    def click_next_button(self) -> None:
        self.next_button.click()
        Reporting.report_allure_and_logger("INFO", "Finished Clicking next button on ADD DOMAIN page")

    @allure.step("Clicking next button on ADD DOMAIN page")
    def click_next_button_enable(self, service) -> None:
        Reporting.report_allure_and_logger("INFO",
                                           f"Starting Clicking next button on ADD DOMAIN page text on button{service}")
        next_button = self.page.locator("text=Enable " + service + " app")
        next_button.click()
        Reporting.report_allure_and_logger("INFO",
                                           f"Finished Clicking next button on ADD DOMAIN page text on button{service}")

    @allure.step("Getting text of highest control\n in ADD DOMAIN page")
    def get_add_domain_label_text(self) -> string:
        Reporting.report_allure_and_logger("INFO", "Finished Getting text of domains control  in ADD DOMAIN page")
        return self.domains.text_content()
