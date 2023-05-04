import allure
from playwright.sync_api import Page

from Utils.Reporting.Reporting import Reporting
from pages.BasePage import BasePage


class ScanResultsListPage(BasePage):

    def __init__(self, page: Page, base_url) -> None:
        self.page = page
        self.scan_search = page.locator("//input[@placeholder='Search']")
        self.full_list_link = page.locator("text=Full List")
        self.search_scans_button = page.locator("id=circle")
        self.open_top_scan_button = page.get_by_title("Open Scan")
        self.top_scan_time_stamp_acronis = page.locator("//li[1]/div/div/div[9]")
        self.top_scan_time_stamp_xray = page.locator("//li[1]/div/div/div[10]")
        self.clear_all_filters = page.locator("text=Clear All")

        super().__init__(self.page, base_url)

    @allure.step("set scanned file to search={1}")
    def set_scanned_file_to_search(self, scaned_file_to_search):
        Reporting.report_allure_and_logger("INFO",
                                           "Started set file scan to search=" + scaned_file_to_search)
        self.scan_search.fill(scaned_file_to_search)
        Reporting.report_allure_and_logger("INFO",
                                           "finished set file scan to search=" + scaned_file_to_search)

    @allure.step("click search scans")
    def click_search_scans(self):
        Reporting.report_allure_and_logger("INFO",
                                           "Started clicking search scans!")
        self.search_scans_button.click()
        Reporting.report_allure_and_logger("INFO",
                                           "finished clicking search scans!")

    @allure.step("click opening top file scan!")
    def click_to_open_top_scan_result(self):
        Reporting.report_allure_and_logger("INFO",
                                           "Started opening top file scan!")
        self.open_top_scan_button.nth(0).click()
        Reporting.report_allure_and_logger("INFO",
                                           "finished opening top file scan!")

    @allure.step("getting top scan time stamp")
    def get_top_scan_time_stamp(self, is_acronis):
        Reporting.report_allure_and_logger("INFO",
                                           "Getting top scan time stamp on scan results list")
        if is_acronis:
            return self.top_scan_time_stamp_acronis.inner_text()
        else:
            return self.top_scan_time_stamp_xray.inner_text()

    @allure.step("click all filters!")
    def click_clear_all_filters(self):
        Reporting.report_allure_and_logger("INFO",
                                           "Started clicking clear all filters link!")
        self.clear_all_filters.click()
        self.page.wait_for_load_state("networkidle")
        Reporting.report_allure_and_logger("INFO",
                                           "finished clicking clear all filters link!")
