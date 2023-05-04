import allure

from Utils.Reporting.Reporting import Reporting
from pages.BasePage import BasePage


class channels_page(BasePage):
    URL='https://xray.testing.perception-point.io/settings/preferences'
    def __init__(self, page):
        self.page = page
        self.gmail_checkbox = page.locator("input[type=\"checkbox\"]")
        self.office365_checkbox = page.locator("input[type=\"checkbox\"]")
        self.save_button=page.locator("button:has-text(\"Save\")")
        super().__init__(self.page, self.URL)

    def check_gmail(self):
        self.gmail_checkbox.nth(1).check()
        self.page.wait_for_load_state("networkidle");
        Reporting.report_allure_and_logger("INFO", "Finished checking gmail channels checkbox on CHANNELS PAGE")

    def check_office(self):
        self.office365_checkbox.first.check()
        self.page.wait_for_load_state("networkidle")
        Reporting.report_allure_and_logger("INFO", "Finished checking OFFICE365 channels checkbox on CHANNELS PAGE")

    def click_save(self):
        allure.step("clicking SAVE BUTTON  on CHANNELS PAGE")
        self.save_button.click()
        self.page.wait_for_load_state("networkidle");
        Reporting.report_allure_and_logger("INFO", "Finished clicking SAVE BUTTON  on CHANNELS PAGE")