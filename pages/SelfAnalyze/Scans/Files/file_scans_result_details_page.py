import string

import allure
from playwright.sync_api import Page

from Utils.Reporting.Reporting import Reporting
from pages.BasePage import BasePage


class ScanResultsDetailsPage(BasePage):

    def __init__(self, page: Page, base_url) -> None:
        self.page = page
        self.verdict_clean_label = page.locator("#app-root header >> text=Clean")
        self.verdict_malicious_label = page.locator("#app-root header >> text=Malicious")
        self.summary_file_name_line = page.locator("(//div[@class='ScanSummary__group--3O_eM']/ul/li[1])[1]")
        self.summary_uploading_user_line = page.locator("(//div[@class='ScanSummary__group--3O_eM']/ul/li[5])[1]")
        self.summary_subject_line = page.locator("//div[@class='ScanSummary__group--3O_eM'][1]/ul/li[6]")
        self.summary_from_line = page.locator("//div[@class='ScanSummary__group--3O_eM'][1]/ul/li[8]")
        self.summary_to_line = page.locator("//div[@class='ScanSummary__group--3O_eM'][1]/ul/li[7]")
        self.summary_webpage_title = page.locator("//div[@class='ScanSummary__group--3O_eM'][1]/ul/li[2]")
        self.summary_responce_url = page.locator("//div[@class='ScanSummary__group--3O_eM'][1]/ul/li[3]")

        self.summary_sha256 = page.locator("(//div[@class='ScanSummary__group--3O_eM'][2]/ul/li[2])[1]")
        self.summary_md5_line = page.locator("(//div[@class='ScanSummary__group--3O_eM'][2]/ul/li[3])[1]")
        self.summary_sha1 = page.locator("((//div[@class='ScanSummary__group--3O_eM'][2]/ul/li[4])[1]")

        self.summary_file_extension = page.locator("//div[@class='ScanSummary__group--3O_eM'][3]/ul/li[1]")
        self.summary_mime_type = page.locator("//div[@class='ScanSummary__group--3O_eM'][3]/ul/li[2]")
        self.summary_size = page.locator("//div[@class='ScanSummary__group--3O_eM'][3]/ul/li[3]")

        self.word_malicious_type_2010 = page.locator("text=Microsoft Word 2010")
        self.word_malicious_type_2016 = page.locator("text=Microsoft Word 2016")
        self.word_malicious_type_2019 = page.locator("text=Microsoft Word 2019")

        super().__init__(self.page, base_url)

    @allure.step("Getting **file scan malicious verdict**")
    def get_verdict_malicious_result(self) -> string:
        Reporting.report_allure_and_logger("INFO", "Before **file scan malicious verdict** text")
        return self.verdict_malicious_label.nth(0).inner_text()

    @allure.step("Getting **file scan clean verdict**")
    def get_verdict_clean_result(self) -> string:
        Reporting.report_allure_and_logger("INFO", "Before **file scan malicious verdict** text")
        return self.verdict_clean_label.nth(0).inner_text()

    @allure.step("getting file name")
    def get_summary_file_name_line_text(self) -> string:
        Reporting.report_allure_and_logger("INFO", "Before getting file name")
        return self.summary_file_name_line.inner_text()

    @allure.step("Getting uploading user")
    def get_summary_uploading_user_line_text(self) -> string:
        Reporting.report_allure_and_logger("INFO", "Before getting uploading user")
        return self.summary_uploading_user_line.inner_text()

    @allure.step("Getting getting sha256!")
    def get_summary_sha256_line_text(self) -> string:
        Reporting.report_allure_and_logger("INFO", "Before getting sha256")
        return self.summary_sha256.inner_text()

    @allure.step("Getting md5 text")
    def get_summary_md5_line_text(self) -> string:
        Reporting.report_allure_and_logger("INFO", "Before getting md5 text")
        return self.summary_md5_line.inner_text()

    @allure.step("Getting sha1 text")
    def get_summary_sha1_line_text(self) -> string:
        Reporting.report_allure_and_logger("INFO", "Before getting sha1 text")
        return self.summary_sha1.inner_text()

    @allure.step("Getting **File Extension** text")
    def get_summary_file_extension_line_text(self) -> string:
        Reporting.report_allure_and_logger("INFO", "Before **File Extension** text")
        return self.summary_file_extension.inner_text()

    @allure.step("Getting **Sha1** text")
    def get_summary_sha1_line_text(self) -> string:
        Reporting.report_allure_and_logger("INFO", "Before **sha1* text")
        return self.summary_file_extension.inner_text()

    @allure.step("Getting **Mime type** text")
    def get_summary_mime_type_line_text(self) -> string:
        Reporting.report_allure_and_logger("INFO", "Before **Mime type** text")
        return self.summary_mime_type.inner_text()

    @allure.step("Getting **File Size** text")
    def get_summary_file_size_line_text(self) -> string:
        Reporting.report_allure_and_logger("INFO", "Before **File Size** text")
        return self.summary_size.inner_text()

    @allure.step("Getting **web_page title** text")
    def get_summary_web_page_title_line_text(self) -> string:
        Reporting.report_allure_and_logger("INFO", "Before *Web_page Title** text")
        return self.summary_webpage_title.inner_text()

    @allure.step("Getting **responce url** text")
    def get_summary_responce_url_line_text(self) -> string:
        Reporting.report_allure_and_logger("INFO", "Before **responce_url** text")
        return self.summary_responce_url.inner_text()

    @allure.step("Getting **from** text")
    def get_summary_subject_line_text(self) -> string:
        Reporting.report_allure_and_logger("INFO", "Before **from** text")
        return self.summary_from_line.inner_text()

    @allure.step("Getting **To** text")
    def get_summary_to_line_text(self) -> string:
        Reporting.report_allure_and_logger("INFO", "Before **To** text")
        return self.summary_from_line.inner_text()

    @allure.step("Getting **Hap word2010** text")
    def get_hap_word2010_text(self) -> string:
        Reporting.report_allure_and_logger("INFO", "Before **Hap word2010** text")
        return self.word_malicious_type_2010.inner_text()

    @allure.step("Getting **Hap word2016** text")
    def get_hap_word2016_text(self) -> string:
        Reporting.report_allure_and_logger("INFO", "Before **Hap word2016** text")
        return self.word_malicious_type_2016.inner_text()

    @allure.step("Getting **Hap word2019** text")
    def get_hap_word2019_text(self) -> string:
        Reporting.report_allure_and_logger("INFO", "Before **word2019** text")
        return self.word_malicious_type_2019.inner_text()
