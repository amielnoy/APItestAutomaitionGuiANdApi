import allure
from playwright.sync_api import Page

from Utils.Reporting.Reporting import Reporting
from pages.BasePage import BasePage


class SelfAnalyzeUrl(BasePage):

    def __init__(self, page: Page, base_url) -> None:
        self.page = page
        self.last_day_tab = page.locator('button:has-text("Last Day")')

        super().__init__(self.page, base_url)

    @allure.step
    def click_setting_menu_item(self):
        self.page.locator(
            ".Icon__icon--2LSDd.Icon__icon-direction-row--3X3WP.Icon__icon-size-regular--2jW3B.Icon__is-inherits-color--3uQQz .isvg svg").first.click()
        self.settings_menu_item.click()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_selector("id=recipient-whitelist-create")
        self.page.get_by_role("link", name="Detection Detection").click()
        Reporting.report_allure_and_logger("INFO", "Finished Clicking  Setting button on main menu on main PAGE")

    @allure.step
    def click_email_wizard(self):
        self.email_setup_wizard.click()
