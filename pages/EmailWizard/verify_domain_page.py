from tokenize import String

import allure

from Utils.Reporting.Reporting import Reporting
from pages.BasePage import BasePage


class verify_domain(BasePage):
    def __init__(self, page):
        self.page = page
        self.add_text_records = page.locator("text=Add TXT Records")
        self.next_button = page.locator("text=Next")
        super().__init__(self.page, "")

    @allure.step("Setting scanned email")
    def get_add_text_records_text(self) -> String:
        Reporting.report_allure_and_logger("INFO","getting text on verify domain added")
        self.logger.info("returning text on verify domain added")
        return self.add_text_records.inner_text()

    @allure.step("Clicking next button on SET SCANNED EMAIL page")
    def click_next_button(self) -> None:
        self.next_button.click()
        Reporting.report_allure_and_logger("INFO", "Finished Clicking next button on SET SCANNED EMAIL page")
