# # TODO
# # TODO Tests for all sections(admin user)
# # TODO Settings-->Detection
# # TODO  DELETE
#
# # TODO git ignore test_output traces & snapshots
# from urllib import request

import allure

from pages.Google.google_page import GooglePage
from TestBuildingBlocks.SetupTearDownOperations.setup_teardown_gui_operations import SetupTearDownGuiOperations
from TestBuildingBlocks.test_help_pages import TestHelpPages
from test_base import BaseTest
from TestBuildingBlocks.test_setup import TestSetup


class TestsSearchGoogle(BaseTest):
    @allure.testcase('https://amiel.testrail.io/index.php?/suites/view/1&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=11')
    # issue in JIRA direct link(bugs+todo items)
    # issue:
    @allure.issue("https://perception-point.atlassian.net/browse/MS-8798")
    @allure.description('log to chrome and record video of the test')
    def test_search_google(self, setup_page2, read_non_secrets):
        page = setup_page2
        #page.pause()
        params_dictionary = read_non_secrets

        #setup_tear_down_gui_operations = SetupTearDownGuiOperations(page, params_dictionary=params_dictionary,
        #                                                             is_acronis=True)
        google_url_value=params_dictionary['GOOGLE_URL']
        google_search_string=params_dictionary['GOOGLE_SEARCH_STRING']

        google= GooglePage(page , base_url=google_url_value)
        google.load()
        google.set_search(google_search_string)
        #page.pause()
        google.click_google_image()
        google.click_enter_on_google_search()

        assert False
        #assert google.url,params_dictionary['GOOGLE_SEARCH_RESULT_URL']+"error"
        print("hello")
        #
        # my_test_help_pages = TestHelpPages(params_dictionary=params_dictionary, is_acronis=True)
        # my_test_help_pages.test_main_help_page(page, is_menu_help=True)
        # # validate main help page text
        # my_test_help_pages.assert_main_help_page()
        # my_test_help_pages.test_main_help_page_search()
        # my_test_help_pages.assert_help_search_results()
        #
        # my_test_help_pages.test_main_help_page(page, is_menu_help=False)
        # my_test_help_pages.assert_main_help_page()
        # my_test_help_pages.test_main_help_page_search()
        # my_test_help_pages.assert_help_search_results()
