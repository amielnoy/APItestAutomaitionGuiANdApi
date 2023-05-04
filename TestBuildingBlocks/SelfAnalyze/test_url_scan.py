import os

from playwright.sync_api import expect

from TestBuildingBlocks.SetupTearDownOperations.setup_teardown_api_operations import SetupTearDownApiOperations
from pages.SelfAnalyze.Scans.Urls.url_scans_result_details_page import UrlScanResultsDetailsPage
from pages.SelfAnalyze.Scans.Urls.urls_scans_result_list_page import UrlScanResultsListPage
from tests.SelfAnalyze.File.compare_time_stamp import ComapreTimeStamp
from pages.SelfAnalyze.self_analyze_file_page import SelfAnalyzeFile
from TestBuildingBlocks.SelfAnalyze.ScanBase import ScanBase
from Utils.Assertions.assertions import Assertions
from Utils.Reporting.Reporting import Reporting
from pages.xray_main_page import xrayInsightsMainPage


class TestUrlAnalyzer:
    def __init__(self, page, params_dictionary, is_acronis, urls_data, project_root):
        self.is_acronis = is_acronis
        self.urls_data = urls_data
        self.page = page
        self.params_dictionary = params_dictionary

        if is_acronis:
            self.base_url = params_dictionary.get("ACRONIS_BASE_URL")
            self.user_email_address = os.getenv("ACRONIS_USERNAME1")
            self.organization_id = params_dictionary.get("ACRONIS_ORGANIZATION_ID1")
        else:
            self.base_url = params_dictionary.get("XRAY_BASE_URL")
            self.user_email_address = os.getenv("XRAY_USERNAME1")
            self.organization_id = params_dictionary.get("XRAY_ORGANIZATION_ID")

        self.xray_main_page = xrayInsightsMainPage(page)
        self.root_project = project_root

    def set_url_and_analyze_url(self):
        self_analyze_file_page = SelfAnalyzeFile(self.page, self.base_url)
        self.xray_main_page.click_self_analyze()
        expect(self_analyze_file_page.scan_upload_area).to_be_visible(timeout=ScanBase.FILE_UPLOAD_TIME_OUT - 30)
        self_analyze_file_page.click_url_analysis()
        # page.pause()
        for url in self.urls_data:
            url_to_scan = url[0].strip()
            self_analyze_file_page.set_url_for_analysis(url_to_scan)
            self_analyze_file_page.click_analyze()

            CurrentRunningScanStatus = ''
            while CurrentRunningScanStatus != 'finished running scans':
                CurrentRunningScanStatus = SetupTearDownApiOperations.get_running_scan_id(self.is_acronis
                                                                                       , self.user_email_address
                                                                                       , self.organization_id)
                if CurrentRunningScanStatus == True:
                    CurrentRunningScanStatus = 'finished running scans'
        self.page.wait_for_timeout(ScanBase.SCANS_COMPLETEION_EXTRA_ALL_SCANS_TIME_OUT)
    def scan_all_urls(self):
        for url_to_scan in self.urls_data:
            # goto all scans
            # page.pause()
            self.xray_main_page.click_full_list_link()
            url_scan_results_list_page = UrlScanResultsListPage(self.page, self.base_url)
            url_scan_results_details_page = UrlScanResultsDetailsPage(self.page, self.base_url)
            scanned_url_to_search = url_to_scan[0].strip()
            expect(url_scan_results_list_page.scan_search).to_be_visible(timeout=ScanBase.FILE_UPLOAD_TIME_OUT - 30000)
            url_scan_results_list_page.set_scanned_file_to_search(scanned_url_to_search)
            # url_scan_results_list_page.click_clear_all_filters()
            url_scan_results_list_page.click_search_scans()
            expect(url_scan_results_list_page.open_top_scan_button.nth(0)).to_be_visible(
                timeout=ScanBase.FILE_UPLOAD_TIME_OUT - 30000)
            # time.sleep(3)
            # get top search result time stamp
            top_scan_time_stamp = url_scan_results_list_page.get_top_scan_time_stamp(is_acronis=self.is_acronis)
            Reporting.report_allure_and_logger("INFO", "Current top file scan time stamp=" + top_scan_time_stamp)
            assert ComapreTimeStamp.is_last_scan_series_match(
                top_scan_time_stamp), "failed to find coerrect last URL scan=" + scanned_url_to_search
            expect(url_scan_results_list_page.open_top_scan_button.nth(0)).to_be_visible(
                timeout=ScanBase.FILE_UPLOAD_TIME_OUT - 30000)
            url_scan_results_list_page.click_to_open_top_scan_result()
            #
            Assertions.assert_value("verify correct url of scans",
                                    url_scan_results_list_page.verify_is_url_prefix(self.base_url + "scans"), True)
            url = url_scan_results_details_page.get_url_line_text()
            assert url == "URL\n" + scanned_url_to_search
            self.assert_scan_url_details(url_to_scan, url_scan_results_details_page,
                                         scanned_url_to_search=scanned_url_to_search)

    def assert_scan_url_details(self, url_to_scan, url_scan_results_details_page, scanned_url_to_search):
        # uploading_user = url_scan_results_details_page.get_summary_uploading_user_line_text()
        # assert uploading_user == "Uploading User\n" + url_to_scan[1].strip()

        if url_to_scan[2].strip() == "Malicious":
            assert url_scan_results_details_page.get_verdict_malicious_result() == "Malicious"
            if scanned_url_to_search == 'http://chen.co.il':
                assert url_scan_results_details_page.get_malicious_web_title_text() == "Webpage Title\n" + \
                       url_to_scan[3].strip(), \
                    "Web Title for Malicious URL" + scanned_url_to_search + " wasn't found"
                assert url_scan_results_details_page.get_malicious_responce_url_text() == "Response URL\n" + \
                       url_to_scan[4].strip(), \
                    "Responce url for malicious" + scanned_url_to_search + " wasn't found"
                # assert url_scan_results_details_page.get_malicious_uploading_user_text() == "Uploading User\n" + \
                #        url_to_scan[5].strip(), \
                #     "uploading user for malicious" + scanned_url_to_search + " wasn't found"

        elif url_to_scan[2].strip() == "Clean":
            assert url_scan_results_details_page.get_verdict_clean_result() == "Clean", "Failed to find clean VERDICT result"
        Reporting.report_allure_and_logger("INFO",
                                           "*********\nFINISHED VERIFING SCANED URL=" + scanned_url_to_search + " SUCCESSFULY\n******")
        url_scan_results_details_page.navigate_to_url()
