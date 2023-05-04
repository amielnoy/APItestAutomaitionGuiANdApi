import allure
from playwright.sync_api import Page

from Utils.Reporting.Reporting import Reporting
from pages.BasePage import BasePage


class SelfAnalyzeFile(BasePage):

    def __init__(self, page: Page, base_url) -> None:
        self.page = page
        self.upload_file_to_scan = page.locator("//*[@id='react-tabs-1']/form/div[1]/div/div[1]/input")
        self.scan_upload_area = page.locator("(//div/div/span/span[2])[1]")
        self.scan_search = page.locator("//input[@placeholder='Search']")
        self.search_scans_button = page.locator("id=circle")
        self.top1_uploaded_file = page.locator("//div/div/div[2]/ul/li[1]/a/div/div/div[2]/div[1]/span/span[2]")
        self.top2_uploaded_file = page.locator("//div/div/div[2]/ul/li[2]/a/div/div/div[2]/div[1]/span/span[2]")
        self.top3_uploaded_file = page.locator("//div/div/div[2]/ul/li[3]/a/div/div/div[2]/div[1]/span/span[2]")
        self.top4_uploaded_file = page.locator("//div/div/div[2]/ul/li[4]/a/div/div/div[2]/div[1]/span/span[2]")

        self.title_malicious = page.get_by_title("Malicious")
        self.title_clean = page.get_by_title("Clean")

        self.url_analysis_tab = page.locator("text='URL Analysis'")
        self.url_for_analysis = page.get_by_placeholder("Enter Url...")
        self.manuall_analysys_button = page.locator("text='Analyze'")
        self.url_scanned_now1 = page.get_by_text("Malicious")
        self.url_scanned_now2 = page.get_by_text("Clean")
        self.upload_password_file_to_scan = page.locator("text=upload")
        self.password_for_file_to_scan = page.get_by_placeholder("Password")
        super().__init__(self.page, base_url)

    @allure.step("Click upload password protected file to scan")
    def click_upload_password_file_to_scan(self):
        Reporting.report_allure_and_logger("INFO",
                                           "Started upload password protected file to scan")
        self.upload_password_file_to_scan.click()
        Reporting.report_allure_and_logger("INFO",
                                           "finished upload password protected file to scan")

    @allure.step("Set file to manually scan")
    def set_password_for_file_to_scan(self, password):
        Reporting.report_allure_and_logger("INFO",
                                           "Started Setting file to manually scan!")
        self.password_for_file_to_scan.fill(password)
        Reporting.report_allure_and_logger("INFO",
                                           "finished Setting file to manually scan!")

    @allure.step("Set file to manually scan")
    def set_file_to_scan(self, file_full_path):
        Reporting.report_allure_and_logger("INFO",
                                           "Started Setting file to manually scan!")
        self.upload_file_to_scan.set_input_files(file_full_path)
        Reporting.report_allure_and_logger("INFO",
                                           "finished Setting file to manually scan!")
    @allure.step("get top upload_file_to_scan verdict text")
    def get_upload_file_to_scan_verdict_text(self):
        Reporting.report_allure_and_logger("INFO",
                                           "Before getting upload_file_to_scan verdict text")
        return self.top_uploaded_file.inner_text()

    @allure.step("Click url analysys tab")
    def click_url_analysis(self):
        Reporting.report_allure_and_logger("INFO",
                                           "Started Clicking url analysys tab")
        self.url_analysis_tab.click()
        Reporting.report_allure_and_logger("INFO",
                                           "finished Clicking url analysys tab")

    @allure.step("Set url to analysys")
    def set_url_for_analysis(self, url_to_analyze):
        Reporting.report_allure_and_logger("INFO",
                                           "Started Setting url to analyze")
        self.url_for_analysis.fill(url_to_analyze)
        Reporting.report_allure_and_logger("INFO", "finished Setting url to analyze")

    @allure.step("Click analyze file")
    def click_analyze(self):
        Reporting.report_allure_and_logger("INFO",
                                           "Started clicking analyze url")
        self.manuall_analysys_button.click()
        Reporting.report_allure_and_logger("INFO", "finished clicking analyze url")
