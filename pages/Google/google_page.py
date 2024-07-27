"""
This module contains login_page,
the page object for the xray login page.
"""
import allure

from Utils.Reporting.Reporting import Reporting
from pages.BasePage import BasePage


class GooglePage(BasePage):
    url = ""

    def __init__(self, page, base_url):
        self.page = page
        self.search = page.locator("id=APjFqb")
        self.search_button = page.locator(".QCzoEc > svg")
        self.google_image = page.get_by_role("img", name="Google")
        self.url = base_url
        super().__init__(self.page, self.url)

    @allure.step("Navigating to login page!")
    def load(self) -> None:
        Reporting.report_allure_and_logger("INFO", "Navigating to login page=" + self.url)
        self.navigate_to_url()

    @allure.step("Setting value search google")
    def set_search(self, search_string):
        self.search.fill(search_string)

        Reporting.report_allure_and_logger("INFO", f"finished setting Search String to google search={search_string}")
    @allure.step("click google search")
    def click_enter_on_google_search(self):
        self.search.click()
        self.page.keyboard.press("Enter")
        Reporting.report_allure_and_logger("INFO", "finished clicking enter on google search")

    @allure.step("click google image")
    def click_google_image(self):
        self.google_image.click()
        Reporting.report_allure_and_logger("INFO", "finished clicking google image")

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
