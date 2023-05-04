# TODO

# TODO Tests for all sections(admin user)
# TODO Settings-->Detection
# TODO  ADD+EDIT+DELETE

# TODO git ignore LogFiles and reports
# from urllib import request

import allure

from TestBuildingBlocks.SettingsDetection.test_setting_detection_items_list import TestSettingDetectionItemList
from pages.Settings.Detection.SettingsDetectionBlackListUrl_Page import SettingsDetectionUrlBlackListPage
from test_base import BaseTest


# Test Flow:

# 1.add two mails
# 2.verify 2 mails added
# 3.search for one
# 4.verify one
# 5.edit it
# 6.delete 2 mails
# 7.verify no bad request
# 8.verify correct url
class TestsSettingDetectionUrlBlackListAcronis(BaseTest):

    # Test Case in TestTrail direct link
    @allure.testcase('https://perceptionpointtemp.testrail.io/index.php?/cases/view/2343')
    # issue in JIRA direct link(bugs+todo items)
    # issue:
    @allure.issue("https://perception-point.atlassian.net/browse/MS-8798")
    @allure.description('log to chrome and record video of the test')
    def test_url_address_blacklist_acronis(self, setup_browser_page, read_non_secrets):
        page = setup_browser_page
        params_dictionary = read_non_secrets

        settings_detection_url_blackList_page = SettingsDetectionUrlBlackListPage(page
                                                                                  , params_dictionary
                                                                                  , is_acronis=True)
        test_setting_detection_url_blacklist = TestSettingDetectionItemList(
            page
            , settings_detection_url_blackList_page

            , params_dictionary=params_dictionary
            , is_acronis=True)

        test_setting_detection_url_blacklist.setup_tear_down_gui_operations.login(page)

        test_setting_detection_url_blacklist.click_setting_menu_item_and_verify_url(page)

        test_setting_detection_url_blacklist.add_two_items_to_list(is_url_blacklist_address=True)
        # add second mail

        test_setting_detection_url_blacklist.get_number_of_added_items_and_assert(2)

        test_setting_detection_url_blacklist.search_for_items_and_assert_search_results_number(
            test_setting_detection_url_blacklist.ip_address1, 1)

        test_setting_detection_url_blacklist.edit_and_save_changes(
            test_setting_detection_url_blacklist.ip_address1)
        # setting_detection_page.click_cancel_search()
        test_setting_detection_url_blacklist.cancel_search()
        # Delete added mails
        test_setting_detection_url_blacklist.delete_two_list_items()
