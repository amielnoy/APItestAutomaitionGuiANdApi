import string

import allure
from playwright.sync_api import Page, expect

from Utils.Assertions.expects import Expects
from Utils.Reporting.Reporting import Reporting
from pages.BasePage import BasePage


class xrayInsightsMainPage(BasePage):
    XRAY_URL = 'https://xray.testing.perception-point.io/insights'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.last_day_tab = page.locator('button:has-text("Last Day")')
        self.attack_level_label = page.locator('button:has-text("Attack Level")')

        # self.set_environment = page.locator("id=organizationsSelect input")
        self.email_setup_wizard = page.locator("id=onboardingButton")
        self.self_analyze = page.locator("id=analyzeButton")
        self.settings_menu_item = page.locator("text=Settings")
        self.documentation_center_menu_item = page.locator("#dropdownMenu").get_by_text("Documentation Center")
        self.full_list_link = page.locator("text= Items Scanned")
        # page.locator("header:has-text(\"Last IncidentsFull List\")").get_by_role("link",name="Full List")
        self.bottom_help_link = page.locator("#app-root").get_by_text("Documentation Center")
        super().__init__(self.page, self.XRAY_URL)

    @allure.step
    def get_result_last_day(self) -> str:
        self.last_day_tab.wait_for()
        return self.last_day_tab.inner_text()

    @allure.step
    def get_result_attack_level(self) -> str:
        self.attack_level_label.wait_for()
        return self.attack_level_label.inner_text()

    @allure.step
    def get_title(self) -> string:
        return self.page.title()

    @allure.step("Clicking  SETTINGS menu item button on  main PAGE main menu")
    def click_setting_menu_item(self):
        Reporting.report_allure_and_logger("INFO", "Clicking  SETTINGS menu item button on  main PAGE main menu")
        #self.page.locator(
        #    ".Icon__icon--2LSDd.Icon__icon-direction-row--3X3WP.Icon__icon-size-regular--2jW3B.Icon__is-inherits-color--3uQQz .isvg svg").first.click()
        self.settings_menu_item.click()
        self.page.wait_for_selector("id=recipient-whitelist-create")
        self.page.get_by_role("link", name="Detection Detection").click()
        Reporting.report_allure_and_logger("INFO",
                                           "Finished Clicking  SETTINGS menu item button on  main PAGE main menu")

    @allure.step("Clicking  SELF ANALYZE menu item button SELF ANALYZE on  main PAGE")
    def click_self_analyze(self):
        Reporting.report_allure_and_logger("INFO", "Start clicking  SELF ANALYZE on  main PAGE")
        self.self_analyze.click()
        Reporting.report_allure_and_logger("INFO", "Finished Clicking  SELF ANALYZE menu item button on  main PAGE")

    @allure.step("Clicking **Email Setup Wizard** button")
    def click_email_wizard(self):
        Reporting.report_allure_and_logger("INFO", "Start Clicking **Email Setup Wizard** button on MAIN PAGE")
        self.email_setup_wizard.click()
        Reporting.report_allure_and_logger("INFO", "Finish Clicking **Email Setup Wizard** button on MAIN PAGE")

    @allure.step
    def set_environment(self, enviornment):
        set_environment = self.page.query_selector("#organizationsSelect input")
        set_environment.click()
        set_environment.fill(enviornment)

    @allure.step("clicking settings on main page")
    def click_settings(self):
        Reporting.report_allure_and_logger("INFO", "Start clicking setting menu item button on MainPage main menu")
        self.settings.click()
        Reporting.report_allure_and_logger("INFO", "Finished clicking setting menu item button on MainPage main menu")

    @allure.step("Clicking **documentation_center_menu_item** button")
    def click_documentation_center_menu_item(self, is_acronis):
        Reporting.report_allure_and_logger("INFO",
                                           "Before Clicking **documentation_center_menu_item** button on MAIN PAGE")

        Expects.expect_conditions_visible_and_enabled(self.page.locator("span:nth-child(2) > .isvg > svg").first
                                                      , 10000
                                                      , "Setting menu item  not visible"
                                                      , "Settings menu item not enabled")
        self.page.locator("span:nth-child(2) > .isvg > svg").first.click()
        expect(self.documentation_center_menu_item).to_be_visible()
        expect(self.documentation_center_menu_item).to_be_enabled()
        with self.page.context.expect_page() as new_help_tab:
            self.documentation_center_menu_item.click()
        if is_acronis:
            new_help_tab.value.wait_for_selector("text=Welcome to the Advanced Email Security")

        else:
            new_help_tab.value.wait_for_selector("text=Welcome to the Perception Point")
        return new_help_tab.value
        # Reporting.report_allure_and_logger("INFO", "Finish Clicking **documentation_center_menu_item** button on MAIN PAGE")

    @allure.step("Clicking **documentation_center_menu_item** button")
    def click_documentation_center_on_bottom_of_main_xray(self, is_acronis):
        Reporting.report_allure_and_logger("INFO",
                                           "Start Clicking **documentation_center_bottom link** button on MAIN PAGE")

        with self.page.context.expect_page() as new_help_tab:
            self.bottom_help_link.click()
        if is_acronis:
            new_help_tab.value.wait_for_selector("text=Welcome to the Advanced Email Security")
        else:
            new_help_tab.value.wait_for_selector("text=Welcome to the Perception Point")
        return new_help_tab.value

    @allure.step("clicking Full List on main page")
    def click_full_list_link(self):
        Reporting.report_allure_and_logger("INFO", "Start clicking Full List link on MainPage main menu")
        self.full_list_link.first.click()
        Reporting.report_allure_and_logger("INFO", "Finished clicking Full List link on MainPage main menu")
