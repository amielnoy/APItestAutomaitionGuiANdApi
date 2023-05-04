# TODO

# TODO Tests for all sections(admin user)
# TODO Settings-->Detection
# TODO  ADD+EDIT+DELETE

# TODO git ignore LogFiles and reports
# from urllib import request

import allure

from TestBuildingBlocks.SetupTearDownOperations.setup_teardown_gui_operations import SetupTearDownGuiOperations
from TestBuildingBlocks.SelfAnalyze.ScanBase import ScanBase
from TestBuildingBlocks.SelfAnalyze.test_url_scan import TestUrlAnalyzer
from Utils.DataDrriven import DataDrriven
from TestBuildingBlocks.test_setup import TestSetup


# Test Flow:

# 1.click from main page manually scan
# 2.for 13 files
#   add file and wait for upload area to be visible again
# 3.verify all scans have correct results


class TestAcronisSelfAnlyzeUrl:
    # Test Case in TestTrail direct link
    project_root = ScanBase.get_project_root()
    csv_path = ScanBase.get_csv_path_for_urls("urls_to_scan_acronis.csv")
    urls_data = DataDrriven.read_test_data_from_csv_to_list(csv_path)

    # issue: can't find scan result
    @allure.issue("https://perception-point.atlassian.net/browse/QA-538")
    @allure.description('log to chrome and record video of the test')
    # @pytest.mark.parametrize("file_full_path", files_data)
    def test_acronis_self_anlyze_url(self, setup_browser_page, read_non_secrets):
        page = setup_browser_page
        dictionary_env_params = read_non_secrets

        setup_tear_down_gui_operations = SetupTearDownGuiOperations(page, params_dictionary=dictionary_env_params
                                                                    , is_acronis=True)
        setup_tear_down_gui_operations.login(page)

        test_url_scan = TestUrlAnalyzer(page, dictionary_env_params
                                        , is_acronis=True
                                        , urls_data=self.urls_data
                                        , project_root=self.project_root)
        test_url_scan.set_url_and_analyze_url()
        test_url_scan.scan_all_urls()
