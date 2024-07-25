"""
This module contains login_page,
the page object for the xray login page.
"""
import allure

from Utils.Reporting.Reporting import Reporting
from pages.BasePage import BasePage


class login(BasePage):
    url = ""

    def __init__(self, page, base_url):
        self.page = page
        self.login_user = page.locator("[placeholder=\"yours\\@example\\.com\"]")
        self.login_password = page.locator("[placeholder=\"your\\ password\"]")
        self.login_button = page.locator("[aria-label=\"Log\\ In\"]")
        self.url = base_url
        super().__init__(self.page, self.url)

    @allure.step("Navigating to login page!")
    def load(self) -> None:
        Reporting.report_allure_and_logger("INFO", "Navigating to login page=" + self.url)
        self.navigate_to_url()

    @allure.step("user logged in with USERNAME={1}")
    def set_user(self, username):
        self.login_user.fill("")
        self.login_user.fill(username)
        Reporting.report_allure_and_logger("INFO", f"finished setting USERNAME={username}")

    @allure.step("user logged in with PASSWORD={1}")
    def set_pass(self, password):
        self.login_password.fill("")
        self.login_password.fill(password)
        Reporting.report_allure_and_logger("INFO", "finished setting PASSWORD=" + password)

    @allure.step("click login action(after setting user+pass)")
    def click_login_button(self):
        Reporting.report_allure_and_logger("INFO", "Started Clicking login button")
        self.login_button.click()
        Reporting.report_allure_and_logger("INFO", "finished Clicking login button")

    @allure.step("preforming login action!")
    def login(self, username, password):
        Reporting.report_allure_and_logger("INFO", "Started  login process user=" + username + " password=" + password)
        self.set_user(username)
        self.set_pass(password)
        self.click_login_button()
        Reporting.report_allure_and_logger("INFO", "Finished login process(user+pass) Navigating to main page")
