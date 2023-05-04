import allure
from playwright.sync_api import expect

from Utils.Reporting.Reporting import Reporting
from pages.BasePage import BasePage


class SettingsDetectionBasePage(BasePage):
    def __init__(self, page, base_url, is_acronis):
        self.page = page
        self.is_acronis = is_acronis

        self.bad_request_error_message = page.locator("text=Bad Request")
        self.succesfull_ip_blacklist_adding_message = page.locator("text=Added Sender IP to Blacklist:")
        self.succesfull_ip_whitelist_adding_message = page.locator("text=Added Sender IP to Whitelist:")
        self.succesfull_Recipient_mail_adding_message = page.locator("text=Added Recipient Address to Whitelist: ")
        self.succesfull_sender_blacklist_adding_message = page.locator("text=Added Sender Address to Blacklist: ")
        self.succesfull_sender_whitelist_adding_message = page.locator("text=Added Sender Address to Whitelist: ")
        self.succesfull_url_whitelist_adding_message = page.locator("text=Added Sender URL to Whitelist: ")
        self.succesfull_url_blacklist_adding_message = page.locator("text=Added Sender URL to Blacklist: ")

        super().__init__(self.page, base_url)

    # Base page method for polymorphizem
    # On drriven classes the correct method will implement there own version)
    @allure.step("Start clicking  add to list button on detection PAGE")
    def click_add_to_list(self):
        Reporting.report_allure_and_logger("INFO", "Finished Clicking  add  to list button on detection PAGE BASE")

    # On drriven classes the correct method will implement there own version)
    @allure.step("Start setting  sender  blacklist ip address on detection PAGE")
    def set_filled_item_name_to_add_list(self, item_name):
        Reporting.report_allure_and_logger("INFO", "finished setting sender ip blacklist BASE!")

    # On drriven classes the correct method will implement there own version)
    @allure.step("Start  clicking add sender ip whitelist BUTTON! on detection PAGE")
    def click_add_item_button_to_add_list(self):
        Reporting.report_allure_and_logger("INFO", "Before clicking add sender ip whitelist BUTTON!")

    @allure.step("Start  clicking main delete button of sender ip blacklist!")
    def click_delete_list_item(self, is_acronis):
        Reporting.report_allure_and_logger("INFO", "finished clicking main delete button of sender ip blacklist!")

    @allure.step("Start  clicking confirm delete button of sender ip blacklist!")
    def delete_list_item_confirmation(self, is_acronis):
        Reporting.report_allure_and_logger("INFO", "finished clicking confirm delete button of list item!")

    @allure.step("Start clicking display mails list button of list item!")
    def click_display_list_item(self):
        Reporting.report_allure_and_logger("INFO",
                                           "finished clicking display mails list button of list item!")

    @allure.step("Start  get ips black list count on sender ips blacklist!")
    def get_list_item_count(self):
        Reporting.report_allure_and_logger("INFO",
                                           "Finished getting mails list count on sender mail blacklist!==")
        return None

    @allure.step("Start  get ips black list count(label) on sender ips blacklist")
    def get_label_list_item_number(self):
        return None

    @allure.step("Start  clicking search ips list items!")
    def search_list(self, item_to_search):
        Reporting.report_allure_and_logger("INFO", "finished clicking search button of list items!")

    # TODO: FIX(get id?)
    # @allure.step("TO FIX")
    # @allure.step("Start clicking CANCEL search button of sender ips blacklist!")
    # def click_cancel_search(self):
    #     self.page.locator("text=Sender Email Address Blacklist1 Address Add Address >> button").nth(1).press("Enter")
    #     Reporting.report_allure_and_logger("INFO", "finished clicking CANCEL search button of sender ips blacklist!")

    @allure.step("Start performing cancel search  of sender ips blacklist!")
    def cancel_search(self):
        Reporting.report_allure_and_logger("INFO", "After performing cancel search  of sender ips blacklist!")

    @allure.step("Start clicking Edit of item in list!")
    def click_edit_list_item(self):
        Reporting.report_allure_and_logger("INFO", "clicking Edit of item in list!")

    @allure.step("Start clicking Edit list item and save button of list item!")
    def click_save_list_item_changes(self):
        Reporting.report_allure_and_logger("INFO", "clicking Edit list item and save button of list item!")

    @allure.step("Returning IP black list(first/Second)")
    def get_list_item(self, params_dictionary, is_first):
        return None

    def delete_highest_detection_item_from_list(self, gui_item_position=1, locator_prefix='', locator_suffix=''):
        string_locator_acronis = self.build_locator_string(gui_item_position=gui_item_position
                                                           , locator_prefix_string=locator_prefix
                                                           , locator_suffix_string=locator_suffix)
        string_locator_xray = self.build_locator_string(gui_item_position=gui_item_position
                                                        , locator_prefix_string=locator_prefix
                                                        , locator_suffix_string=locator_suffix)

        if self.is_acronis:
            expect(self.page.locator(string_locator_acronis)).to_be_visible(timeout=10000)
            self.page.locator(string_locator_acronis).click()
        else:
            expect(self.page.locator(string_locator_xray)).to_be_visible(timeout=10000)
            self.page.locator(string_locator_xray).click()
