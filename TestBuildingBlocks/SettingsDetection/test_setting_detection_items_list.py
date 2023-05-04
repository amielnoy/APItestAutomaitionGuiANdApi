import os
import string

from playwright.sync_api import expect

from pages.Settings.SettingsDetectionBasePage import SettingsDetectionBasePage
from TestBuildingBlocks.SettingsDetection.test_setting_detection_pages_base import BaseSettingDetectionTestPages
from Utils.Reporting.Reporting import Reporting
from pages.xray_main_page import xrayInsightsMainPage


class TestSettingDetectionItemList(BaseSettingDetectionTestPages):

    def __init__(self, page, setting_detection_base_page: SettingsDetectionBasePage = None, params_dictionary=None,
                 is_acronis=None):
        self.TIME_FOR_ITEM_CREATION_SUCCESS_MESSAGE_TO_APPEAR = 10000

        self.settings_detection_base_page = setting_detection_base_page
        self.params_dictionary = params_dictionary
        self.is_acronis = is_acronis
        if is_acronis:
            self.organization_id = params_dictionary.get('ORGANIZATION_ID1')
            self.token_value = os.getenv('XRAY_USER_TOKEN1')
        else:
            self.organization_id = params_dictionary.get('ORGANIZATION_ID')
            self.token_value = os.getenv('XRAY_USER_TOKEN1')

        super().__init__(page, params_dictionary, is_acronis)

    def click_setting_menu_item_and_verify_url(self, page):
        xray_main_page = xrayInsightsMainPage(page)
        xray_main_page.click_setting_menu_item()
        xray_main_page.verify_url(self.base_url + "settings/detection")

    def add_item_to_list(self, is_first
                         , is_reciptent_white_list=False
                         , is_black_list_mail_sender=False
                         , is_white_list_mail_sender=False
                         , is_ip_whitelist_address=False
                         , is_ip_blacklist_address=False
                         , is_url_blacklist_address=False
                         , is_url_whitelist_address=False):
        if is_first:
            ip_addrress = self.settings_detection_base_page.get_list_item(self.params_dictionary
                                                                          , True
                                                                          , self.is_acronis)
            self.ip_address1 = ip_addrress
        else:
            ip_addrress = self.settings_detection_base_page.get_list_item(self.params_dictionary
                                                                          , False
                                                                          , self.is_acronis)
            self.ip_address2 = ip_addrress

        # add first mail
        self.settings_detection_base_page.click_add_to_list()
        self.settings_detection_base_page.set_filled_item_name_to_add_list(ip_addrress)
        self.settings_detection_base_page.click_add_item_button_to_add_list()
        if is_reciptent_white_list:
            expect(self.settings_detection_base_page.succesfull_Recipient_mail_adding_message) \
                .to_be_visible(timeout=self.TIME_FOR_ITEM_CREATION_SUCCESS_MESSAGE_TO_APPEAR)
        elif is_black_list_mail_sender:
            expect(self.settings_detection_base_page.succesfull_sender_blacklist_adding_message) \
                .to_be_visible(timeout=self.TIME_FOR_ITEM_CREATION_SUCCESS_MESSAGE_TO_APPEAR)
        elif is_white_list_mail_sender:
            expect(self.settings_detection_base_page.succesfull_sender_whitelist_adding_message) \
                .to_be_visible(timeout=self.TIME_FOR_ITEM_CREATION_SUCCESS_MESSAGE_TO_APPEAR)
        elif is_ip_whitelist_address:
            expect(self.settings_detection_base_page.succesfull_ip_whitelist_adding_message) \
                .to_be_visible(timeout=self.TIME_FOR_ITEM_CREATION_SUCCESS_MESSAGE_TO_APPEAR)
        elif is_ip_blacklist_address:
            expect(self.settings_detection_base_page.succesfull_ip_blacklist_adding_message) \
                .to_be_visible(timeout=self.TIME_FOR_ITEM_CREATION_SUCCESS_MESSAGE_TO_APPEAR)

        elif is_url_blacklist_address:
            expect(self.settings_detection_base_page.succesfull_url_blacklist_adding_message) \
                .to_be_visible(timeout=self.TIME_FOR_ITEM_CREATION_SUCCESS_MESSAGE_TO_APPEAR)
        elif is_url_whitelist_address:
            expect(self.settings_detection_base_page.succesfull_url_whitelist_adding_message) \
                .to_be_visible(timeout=self.TIME_FOR_ITEM_CREATION_SUCCESS_MESSAGE_TO_APPEAR)

        if is_first:
            self.settings_detection_base_page.click_display_list_item()
            self.settings_detection_base_page.click_display_list_item()

    def add_two_items_to_list(self
                              , is_reciptent_white_list=False
                              , is_black_list_mail_sender=False
                              , is_white_list_mail_sender=False
                              , is_ip_blacklist_address=False
                              , is_ip_whitelist_address=False
                              , is_url_whitelist_address=False
                              , is_url_blacklist_address=False):
        self.add_item_to_list(is_first=True
                              , is_reciptent_white_list=is_reciptent_white_list
                              , is_black_list_mail_sender=is_black_list_mail_sender
                              , is_white_list_mail_sender=is_white_list_mail_sender
                              , is_ip_blacklist_address=is_ip_blacklist_address
                              , is_ip_whitelist_address=is_ip_whitelist_address
                              , is_url_whitelist_address=is_url_whitelist_address
                              , is_url_blacklist_address=is_url_blacklist_address)
        self.add_item_to_list(is_first=False
                              , is_reciptent_white_list=is_reciptent_white_list
                              , is_black_list_mail_sender=is_black_list_mail_sender
                              , is_white_list_mail_sender=is_white_list_mail_sender
                              , is_ip_blacklist_address=is_ip_blacklist_address
                              , is_ip_whitelist_address=is_ip_whitelist_address
                              , is_url_whitelist_address=is_url_whitelist_address
                              , is_url_blacklist_address=is_url_blacklist_address)

    def get_number_of_added_items_and_assert(self, expected_items_number):
        self.settings_detection_base_page.click_display_list_item()
        number_of_ips_after_text: string = self.settings_detection_base_page.get_label_list_item_number()

        number_of_sender_blacklist_ips_after = int(number_of_ips_after_text.split(' ')[0])
        Reporting.report_allure_and_logger("INFO",
                                           "number of_black list ips_after(from label)=" + str(
                                               number_of_sender_blacklist_ips_after))
        assert number_of_sender_blacklist_ips_after == expected_items_number, "Number of black list sender ip after addition in not correct(not increased by 2)!!"

    def search_for_items_and_assert_search_results_number(self, searched_item, expected_items_number):
        self.settings_detection_base_page.search_list(searched_item)
        number_of_mails_after_one_email_search = self.settings_detection_base_page.get_list_item_count()
        assert number_of_mails_after_one_email_search == expected_items_number, "number of mails after searching one mail <> >1"

    def edit_and_save_changes(self, ip_address_to_edit):
        self.settings_detection_base_page.click_edit_list_item()
        edited_ip_addrress1 = ip_address_to_edit + "1"
        self.settings_detection_base_page.set_filled_item_name_to_add_list(edited_ip_addrress1)
        self.settings_detection_base_page.click_save_list_item_changes()

    def cancel_search(self):
        self.settings_detection_base_page.cancel_search()
        self.settings_detection_base_page.click_display_list_item()

    def delete_list_item(self, is_first):
        if is_first:
            #self.page.pause()
            self.settings_detection_base_page.click_delete_list_item()
            self.settings_detection_base_page.delete_list_item_confirmation()
        else:
            self.settings_detection_base_page.click_delete_list_item()
            self.settings_detection_base_page.delete_list_item_confirmation()
            expect(
                self.settings_detection_base_page.bad_request_error_message).not_to_be_visible()  # ,"Bad Request error message appeared"

            self.settings_detection_base_page.verify_url(self.base_url + 'settings/detection')

    def delete_two_list_items(self):
        self.delete_list_item(is_first=True)
        self.delete_list_item(is_first=False)
