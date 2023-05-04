from tokenize import String

import allure

from Utils.Reporting.Reporting import Reporting
from pages.BasePage import BasePage

class view_status(BasePage):
    def __init__(self, page):
        self.page = page
        self.allmost_done=page.locator("text=Almost Done!")
        self.view_status_button = page.locator("text=VIEW STATUS")
        super().__init__(self.page, "")

    @allure.step("Setting scanned email")
    def get_allmost_done_text(self) -> String:
        Reporting.report_allure_and_logger("INFO", "getting text on VIEW STATUS page")
        self.logger.info("returning text on VIEW STATUS page")
        return self.allmost_done.inner_text()

    @allure.step("Clicking next button on VIEW STATUS page")
    def click_view_status_button(self) -> None:
        self.view_status_button.click()
        Reporting.report_allure_and_logger("INFO", "Finished Clicking VIEW STATUS button on VIEW STATUS page")


