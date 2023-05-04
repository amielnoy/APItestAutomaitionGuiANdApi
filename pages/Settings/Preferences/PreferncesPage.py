import allure

from Utils.Reporting.Reporting import Reporting
from pages.BasePage import BasePage


class preferences_page(BasePage):
    URL = 'https://xray.testing.perception-point.io/settings/preferences'
    def __init__(self, page):
        self.page = page
        self.edit = page.locator("text=Channels Edit >> button")
        super().__init__(self.page, self.env)

    def click_channels_edit(self):
        allure.step("Clicking  channels Edit button on preferences PAGE")
        self.edit.click()
        Reporting.report_allure_and_logger("INFO", "Finished clicking  channels Edit button on preferences PAGE")

