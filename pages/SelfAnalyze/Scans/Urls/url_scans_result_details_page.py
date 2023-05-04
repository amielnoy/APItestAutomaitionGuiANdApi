import string

import allure
from playwright.sync_api import Page

from Utils.Reporting.Reporting import Reporting
from pages.BasePage import BasePage


class UrlScanResultsDetailsPage(BasePage):

    def __init__(self, page: Page, base_url) -> None:
        self.page = page
        self.verdict_clean_label = page.locator("#app-root header >> text=Clean")
        self.verdict_malicious_label = page.locator("#app-root header >> text=Malicious")
        self.web_title = page.locator("//div/div[3]/div[2]/div/div/div/ul/li[2]")
        self.responce_url = page.locator("//div[3]/div[2]/div/div/div/ul/li[3]")
        self.uploading_user = page.locator("//div[3]/div[2]/div/div/div/ul/li[5]")
        self.summary_url_line = page.locator("//div[3]/div[2]/div/div/div/ul/li[1]/div/div")
        self.summary_from_line = page.locator("//div[@class='ScanSummary__group--3O_eM'][1]/ul/li[8]")
        self.summary_to_line = page.locator("//div[@class='ScanSummary__group--3O_eM'][1]/ul/li[7]")
        self.summary_uploading_user_line = page.locator("//div[3]/div[2]/div/div/div/ul/li[5]/div/div")

        super().__init__(self.page, base_url)
    @allure.step("Getting **file scan malicious verdict**")
    def get_verdict_malicious_result(self) -> string:
        Reporting.report_allure_and_logger("INFO", "Before **file scan malicious verdict** text")
        return self.verdict_malicious_label.inner_text()

    @allure.step("Getting **file scan clean verdict**")
    def get_verdict_clean_result(self) -> string:
        Reporting.report_allure_and_logger("INFO", "Before **file scan malicious verdict** text")
        return self.verdict_clean_label.inner_text()

    @allure.step("Getting **To** text")
    def get_summary_to_line_text(self) -> string:
        Reporting.report_allure_and_logger("INFO", "Before **To** text")
        return self.summary_from_line.inner_text()

    @allure.step("Getting **Uploading user** text")
    def get_summary_uploading_user_line_text(self) -> string:
        Reporting.report_allure_and_logger("INFO", "Before **Uploading user*** text")
        return self.summary_uploading_user_line.inner_text()

    @allure.step("Getting **URL LINE** text")
    def get_url_line_text(self) -> string:
        Reporting.report_allure_and_logger("INFO", "Before **getting URL LINE** text")
        return self.summary_url_line.inner_text()

    @allure.step("Getting **Web Title** text")
    def get_malicious_web_title_text(self) -> string:
        Reporting.report_allure_and_logger("INFO", "Before **getting Web Title** text")
        return self.web_title.inner_text()

    @allure.step("Getting **Responce Url** text")
    def get_malicious_responce_url_text(self) -> string:
        Reporting.report_allure_and_logger("INFO", "Before **getting Responce Url** text")
        return self.responce_url.inner_text()

    @allure.step("Getting **Uploading User** text")
    def get_malicious_uploading_user_text(self) -> string:
        Reporting.report_allure_and_logger("INFO", "Before **getting Uploading User** text")
        return self.uploading_user.inner_text()
