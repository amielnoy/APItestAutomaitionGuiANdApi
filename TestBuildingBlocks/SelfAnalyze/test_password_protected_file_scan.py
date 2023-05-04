import os

from playwright.sync_api import expect

from TestBuildingBlocks.SetupTearDownOperations.setup_teardown_api_operations import SetupTearDownApiOperations
from Utils.Assertions.expects import Expects
from tests.SelfAnalyze.File.compare_time_stamp import ComapreTimeStamp
from pages.SelfAnalyze.Scans.Files.file_scans_result_details_page import ScanResultsDetailsPage
from pages.SelfAnalyze.Scans.Files.file_scans_result_list_page import ScanResultsListPage
from pages.SelfAnalyze.self_analyze_file_page import SelfAnalyzeFile
from TestBuildingBlocks.SelfAnalyze.ScanBase import ScanBase
from Utils.Assertions.assertions import Assertions
from Utils.Reporting.Reporting import Reporting
from pages.xray_main_page import xrayInsightsMainPage


class TestPasswordProtectedFileAnalyzer:
    def __init__(self, page, params_dictionary, is_acronis, files_data, project_root):
        self.is_acronis = is_acronis
        self.files_data = files_data
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

    def password_protected_file_upload_and_analyze(self):
        xray_main_page = xrayInsightsMainPage(self.page)
        self_analyze_file_page = SelfAnalyzeFile(self.page, self.base_url)

        xray_main_page.click_self_analyze()
        expect(self_analyze_file_page.scan_upload_area).to_be_visible(timeout=ScanBase.FILE_UPLOAD_TIME_OUT - 30000)

        for file_detals in self.files_data:
            file_full_path = str(self.root_project.parent) + "/TestData/TestScanInputFiles/password_protected/" + \
                             file_detals[0].strip()
            if os.path.isfile(file_full_path):
                self_analyze_file_page.click_upload_password_file_to_scan()
                self_analyze_file_page.set_file_to_scan(file_full_path)
                # Set  ***password for password protected file to scan***
                self_analyze_file_page.set_password_for_file_to_scan(file_detals[6].strip())
                self_analyze_file_page.click_analyze()
                expect(self_analyze_file_page.scan_upload_area).to_be_visible(timeout=ScanBase.FILE_UPLOAD_TIME_OUT)

        CurrentRunningScanStatus = ''
        while CurrentRunningScanStatus != 'finished running scans':
            CurrentRunningScanStatus = SetupTearDownApiOperations.get_running_scan_id(self.is_acronis
                                                                                      , self.user_email_address
                                                                                      , self.organization_id)
            if CurrentRunningScanStatus == True:
                CurrentRunningScanStatus = 'finished running scans'
        self.page.wait_for_timeout(ScanBase.SCANS_COMPLETEION_EXTRA_ALL_SCANS_TIME_OUT)

    def password_protected_file_scan_all_files(self):
        for file_details in self.files_data:
            # goto all scans
            self.xray_main_page.click_full_list_link()
            scan_results_list_page = ScanResultsListPage(self.page, self.base_url)
            scan_results_details_page = ScanResultsDetailsPage(self.page, self.base_url)
            scanned_file_to_search = file_details[0].strip()
            # scan_results_list_page.click_clear_all_filters()
            scan_results_list_page.set_scanned_file_to_search(scanned_file_to_search)
            Expects.expect_condition_visible(scan_results_list_page.search_scans_button
                                             , timeout=ScanBase.SEARCH_SCAN_BUTTON_MAX_TIME,
                                             error_message="search scans button failed to appear after"
                                                           + str(ScanBase.SEARCH_SCAN_BUTTON_MAX_TIME))
            expect(scan_results_list_page.search_scans_button).to_be_enabled(
                timeout=ScanBase.SEARCH_SCAN_BUTTON_MAX_TIME)

            scan_results_list_page.click_search_scans()
            expect(scan_results_list_page.open_top_scan_button.nth(0)).to_be_visible()
            # get top search result time stamp
            top_scan_time_stamp = scan_results_list_page.get_top_scan_time_stamp(self.is_acronis)
            Reporting.report_allure_and_logger("INFO", "Current top file scan time stamp=" + top_scan_time_stamp)
            Assertions.assert_value_with_err_message("Assert is last scan has correct time stamp"
                                                     , ComapreTimeStamp.is_last_scan_series_match(top_scan_time_stamp)
                                                     , True
                                                     , "failed to find coerrect last file scan")
            # time.sleep(3)
            scan_results_list_page.click_to_open_top_scan_result()

            Assertions.assert_boolean_value("verify correct url of scans"
                                            , True
                                            , scan_results_list_page.verify_is_url_prefix(self.base_url + "scans"))
            Assertions.assert_value_with_err_message("Asserting file name"
                                                     , scan_results_details_page.get_summary_file_name_line_text()
                                                     , "File Name\n" + scanned_file_to_search.strip()
                                                     , "file name is not=" + scanned_file_to_search)
            self.assert_scan_file_details(file_details, scan_results_details_page, scanned_file_to_search)

    def assert_scan_file_details(self, file_details, scan_results_details_page, scanned_file_to_search):
        # TODO web_page_title & from fields not always appear in scan details page!!!
        # if scanned_file_to_search == 'CSS.amir':
        # web_page_title=scan_results_details_page.get_summary_web_page_title_line_text()
        # from_address = page.locator("//div[@class='ScanSummary__group--3O_eM'][1]/ul/li[7]").inner_text()
        # assert web_page_title == "Webpage Title\n"+file_detals[6]
        # assert from_address == "From\n" + file_detals[7]
        # TODO subject & to fields not always appear in scan details page!!!
        # if scanned_file_to_search == 'organización española escanea.eml':
        # subject=scan_results_details_page.get_summary_subject_line_text()
        # to_email_address = scan_results_details_page.get_summary_to_line_text()
        # assert subject == "Subject\n"+file_detals[7]
        # assert to_email_address == "To\n" + file_detals[8]

        uploading_user = scan_results_details_page.get_summary_uploading_user_line_text()
        # print("\n" + uploading_user)
        # print("Uploading User\n" + file_details[1])
        # if len(uploading_user) > 0:
        #    Assertions.assert_value("Assert uploading user", "Uploading User\n" + file_details[1].strip(),
        #                            uploading_user)

        file_extension = scan_results_details_page.get_summary_file_extension_line_text()
        Assertions.assert_value("Assert file extension", "File Extension\n" + file_details[2].strip(),
                                file_extension)

        mime_type = scan_results_details_page.get_summary_mime_type_line_text()
        Assertions.assert_value("Assert file mime type", "Mime Type\n" + file_details[3].strip(), mime_type)
        file_size = scan_results_details_page.get_summary_file_size_line_text()
        Assertions.assert_value("Asserting file size", file_size, "Size\n" + file_details[4].strip())
        # page.pause()
        if (file_details[5].strip() == "Malicious"):
            assert scan_results_details_page.get_verdict_malicious_result() == (file_details[5].strip())
            if scanned_file_to_search == 'mal.docx':
                Assertions.assert_value_with_err_message("Assert word2010 hap"
                                                         , scan_results_details_page.get_hap_word2010_text()
                                                         , "Microsoft Word 2010"
                                                         , "Malware Microsoft Word 2010 wasn't found")
                Assertions.assert_value_with_err_message("Assert word2016 hap"
                                                         , scan_results_details_page.get_hap_word2016_text()
                                                         , "Microsoft Word 2016"
                                                         , "Malware Microsoft Word 2010 wasn't found")
                Assertions.assert_value_with_err_message("Assert word2016 hap"
                                                         , scan_results_details_page.get_hap_word2019_text()
                                                         , "Microsoft Word 2019"
                                                         , "Malware Microsoft Word 2010 wasn't found")

        elif file_details[5].strip() == "Clean":
            assert scan_results_details_page.get_verdict_clean_result() == (file_details[5].strip())
        Reporting.report_allure_and_logger("INFO",
                                           "*********\nFINISHED VERIFING FILE SCAN of file=" + scanned_file_to_search + " SUCCESSFULLY\n******")
        scan_results_details_page.navigate_to_url()
