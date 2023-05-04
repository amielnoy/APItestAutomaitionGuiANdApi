# TODO
# TODO Tests for all sections(admin user)
# TODO Settings-->Detection
# TODO  DELETE

# TODO git ignore test_output traces & snapshots
# from urllib import request

import allure

from TestBuildingBlocks.SetupTearDownOperations.setup_teardown_gui_operations import SetupTearDownGuiOperations
from TestBuildingBlocks.test_help_pages import TestHelpPages
from test_base import BaseTest
from TestBuildingBlocks.test_setup import TestSetup


class TestsSearchHelpAcronis(BaseTest):
    @allure.testcase('https://perceptionpointtemp.testrail.io/index.php?/cases/view/2343')
    # issue in JIRA direct link(bugs+todo items)
    # issue:
    @allure.issue("https://perception-point.atlassian.net/browse/MS-8798")
    @allure.description('log to chrome and record video of the test')
    def test_search_help_acronis(self, setup_browser_page, read_non_secrets):
        page = setup_browser_page
        params_dictionary = read_non_secrets

        setup_tear_down_gui_operations = SetupTearDownGuiOperations(page, params_dictionary=params_dictionary,
                                                                    is_acronis=True)
        setup_tear_down_gui_operations.login(page)

        my_test_help_pages = TestHelpPages(params_dictionary=params_dictionary, is_acronis=True)
        my_test_help_pages.test_main_help_page(page, is_menu_help=True)
        # validate main help page text
        my_test_help_pages.assert_main_help_page()
        my_test_help_pages.test_main_help_page_search()
        my_test_help_pages.assert_help_search_results()

        my_test_help_pages.test_main_help_page(page, is_menu_help=False)
        my_test_help_pages.assert_main_help_page()
        my_test_help_pages.test_main_help_page_search()
        my_test_help_pages.assert_help_search_results()
