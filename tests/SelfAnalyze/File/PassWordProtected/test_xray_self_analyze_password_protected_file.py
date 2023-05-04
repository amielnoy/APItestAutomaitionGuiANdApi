import allure

from TestBuildingBlocks.SetupTearDownOperations.setup_teardown_gui_operations import SetupTearDownGuiOperations
from TestBuildingBlocks.SelfAnalyze.ScanBase import ScanBase
from TestBuildingBlocks.SelfAnalyze.test_password_protected_file_scan import TestPasswordProtectedFileAnalyzer

from Utils.DataDrriven import DataDrriven
from TestBuildingBlocks.test_setup import TestSetup


# Test Flow:

# 1.click from main page manually scan
# 2.for 13 files
#   add file and wait for upload area to be visible again
# 3.verify all scans have correct results

class TestXraySelfAnlyzePassWordProtectedFile:
    project_root = ScanBase.get_project_root()
    csv_path = ScanBase.get_csv_path_for_files("files_to_scan_xray_password_protected.csv")
    files_data = DataDrriven.read_test_data_from_csv_to_list(csv_path)

    @allure.testcase('https://perceptionpointtemp.testrail.io/index.php?/cases/view/2343')
    # issue in JIRA direct link(bugs+todo items)
    # issue:
    @allure.issue("https://perception-point.atlassian.net/browse/MS-8798")
    @allure.description('log to chrome and record video of the test')
    # @pytest.mark.parametrize("file_full_path", files_data)
    def test_xray_self_anlyze_file_password_protected(self, setup_browser_page, read_non_secrets):  # page.pause()

        dictionary_env_params = read_non_secrets
        page = setup_browser_page
        setup_tear_down_gui_operations = SetupTearDownGuiOperations(page, params_dictionary=dictionary_env_params
                                                                    , is_acronis=True)
        setup_tear_down_gui_operations.login(page)

        test_password_protected_file_analyzer = TestPasswordProtectedFileAnalyzer(page, dictionary_env_params
                                                                                  , is_acronis=False
                                                                                  ,
                                                                                  files_data=TestXraySelfAnlyzePassWordProtectedFile.files_data
                                                                                  , project_root=self.project_root)
        test_password_protected_file_analyzer.password_protected_file_upload_and_analyze()
        # verify scan results
        test_password_protected_file_analyzer.password_protected_file_scan_all_files()
