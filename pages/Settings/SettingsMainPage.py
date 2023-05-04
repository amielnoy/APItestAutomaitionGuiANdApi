import allure

from Utils.Reporting.Reporting import Reporting
from pages.BasePage import BasePage


class SettingsMainPage(BasePage):
    URL = 'https://xray.testing.perception-point.io/settings/detection'

    def __init__(self, page):
        self.page = page
        self.preferences = page.locator("text=Preferences")
        self.channels = page.locator("a.AppNavigationMenu__nav-link--1a7pe.active")

        super().__init__(self.page, self.URL)

    @allure.step("Clicking  PREFERNCES menu item button on Settings main PAGE")
    def click_preferences(self):
        Reporting.report_allure_and_logger("INFO", "Clicking  PREFERNCES menu item button on Settings main PAGE")
        self.preferences.click()
        Reporting.report_allure_and_logger("INFO",
                                           "Finished Clicking  Preferences menu item button on Settings main PAGE")

    @allure.step("Clicking  COLLABORATION menu item button on Settings main PAGE")
    def click_channels(self):
        Reporting.report_allure_and_logger("INFO", "Clicking  COLLABORATION menu item button on Settings main PAGE")
        self.channels.click()
        Reporting.report_allure_and_logger("INFO",
                                           "Finished Clicking  COLLABORATION menu item button on Settings main PAGE")
