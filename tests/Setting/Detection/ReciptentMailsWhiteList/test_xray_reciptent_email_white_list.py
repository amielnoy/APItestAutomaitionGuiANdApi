# TODO

# TODO Tests for all sections(admin user)

import allure

from TestBuildingBlocks.SettingsDetection.test_setting_detection_items_list import TestSettingDetectionItemList
from pages.Settings.Detection.SettingsDetectionWhiteListReciptentPage import \
    SettingsDetectionReciptentWhiteListPage
from test_base import BaseTest


# 1.add two mails
# 2.verify 2 mails added
# 3.search for one
# 4.verify one
# 5.edit it
# 6.delete 2 mails
# 7.verify no bad request
# 8.verify correct url

# BUG:
# ON Recipient Email Address Whitelist
# only one mail exists but 3 reported
class TestsSettingDetectionWhiteListReciptentXray(BaseTest):
    # Test Case in TestTrail direct link
    @allure.testcase('https://perceptionpointtemp.testrail.io/index.php?/cases/view/2343')
    # issuekipa in JIRA direct link(bugs+todo items)
    # issue:
    @allure.issue("https://perception-point.atlassian.net/browse/MS-8798")
    @allure.description('log to chrome and record video of the test')
    def test_reciptent_white_list_xray(self, setup_browser_page, read_non_secrets):
        page = setup_browser_page
        params_dictionary = read_non_secrets

        settings_detection_reciptent_white_list_page = SettingsDetectionReciptentWhiteListPage(page, is_acronis=False)
        test_setting_detection_black_list_ip = TestSettingDetectionItemList(
            page
            , settings_detection_reciptent_white_list_page
            , params_dictionary=params_dictionary
            , is_acronis=False
        )
        test_setting_detection_black_list_ip.setup_tear_down_gui_operations.login(page)
        test_setting_detection_black_list_ip.click_setting_menu_item_and_verify_url(page)

        test_setting_detection_black_list_ip.add_two_items_to_list(is_reciptent_white_list=True)

        test_setting_detection_black_list_ip.get_number_of_added_items_and_assert(2)

        test_setting_detection_black_list_ip.search_for_items_and_assert_search_results_number(
            test_setting_detection_black_list_ip.ip_address1, 1)

        test_setting_detection_black_list_ip.edit_and_save_changes(test_setting_detection_black_list_ip.ip_address1)
        # setting_detection_page.click_cancel_search()
        test_setting_detection_black_list_ip.cancel_search()
        # Delete added mails
        test_setting_detection_black_list_ip.delete_two_list_items()
