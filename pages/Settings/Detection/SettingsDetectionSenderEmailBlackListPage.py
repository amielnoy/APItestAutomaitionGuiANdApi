import allure

from pages.Settings.SettingsDetectionBasePage import SettingsDetectionBasePage
from Utils.Reporting.Reporting import Reporting


class SettingsDetectionSenderBlackListPage(SettingsDetectionBasePage):

    def __init__(self, page, params_dictionary, is_acronis):
        self.page = page
        self.is_acronis = is_acronis

        if not is_acronis:
            self.base_url = params_dictionary.get('XRAY_BASE_URL')
        else:
            self.base_url = params_dictionary.get('ACRONIS_BASE_URL')
        self.add_whitelist_mail_button = page.locator("id=email-blacklist-create")
        self.search_mail_input = page.locator("[placeholder=\"Search\"]")
        self.search_mail_operation = page.locator("id=circle")

        self.reciepent_email_to_add_address = page.locator("input[name=\"Sender\\ Email\\ Address\"]")
        self.add_mail_button = page.locator("button:has-text(\"Add Sender Email Address\")")
        self.mails_number_label = page.get_by_text("Addresses")

        self.mail_list_items = page.locator("id=email-blacklist-create")
        self.display_mails_list1 = page.locator("id=email-blacklist")

        self.main_deleted = page.locator("button:has-text(\"Delete\")")
        self.confirm_delete = page.get_by_role("button", name="Delete Address from Blacklist")

        self.edit_button = page.locator("button:has-text(\"Edit\")")
        self.save_changes_button = page.locator("button:has-text(\"Save Changes\")")
        self.bad_request_error_message = page.locator("text=Bad Request")
        # locate by substring
        # self.succesfull_mail_adding_message = page.locator("text=Added Sender Address to Blacklist: ")
        self.succesfull_sender_blacklist_adding_message = page.locator("text=Added Sender Address to Blacklist: ")
        # self.cancel_search = page.locator("//button[@title='Clear']/span/span")
        super().__init__(self.page, self.base_url + '/settings/detection', self.is_acronis)

    @allure.step("Start clicking  add blacklist mail button on detection PAGE")
    def click_add_to_list(self):
        self.add_whitelist_mail_button.click(force=True)
        self.page.wait_for_timeout(1000)
        Reporting.report_allure_and_logger("INFO", "Finished Clicking  add blacklist mail button on detection PAGE")

    @allure.step("Start setting  sender  blacklist mail email address on detection PAGE")
    def set_filled_item_name_to_add_list(self, mail_address):
        self.reciepent_email_to_add_address.fill(mail_address)
        Reporting.report_allure_and_logger("INFO", "finished setting sender mail blacklist!")

    @allure.step("Start  clicking add sender mail blacklist BUTTON! on detection PAGE")
    def click_add_item_button_to_add_list(self):
        self.add_mail_button.click()
        Reporting.report_allure_and_logger("INFO", "finished clicking add sender mail blacklist BUTTON!")

    @allure.step("Start  getting mail number text sender mail blacklist label! on detection PAGE")
    def get_label_list_item_number(self):
        return self.mails_number_label.nth(2).inner_html()

    @allure.step("Start  clicking main delete button of sender mail blacklist!")
    def click_delete_list_item(self):
        Reporting.report_allure_and_logger("INFO", "Started clicking main delete button of sender mail blacklist!")
        locator_prefix = "//div[3]/div/div/ul/li["
        acronis_locator_suffix = "]/div/div/div[4]/div/div[2]/button/span/span[2]"
        xray_locator_suffix = "]/div/div/div[5]/div/div[2]/button/span/span[2]"

        if self.is_acronis:
            self.delete_highest_detection_item_from_list(locator_prefix=locator_prefix
                                                         , locator_suffix=acronis_locator_suffix)
        else:
            self.delete_highest_detection_item_from_list(locator_prefix=locator_prefix
                                                         , locator_suffix=xray_locator_suffix)
        Reporting.report_allure_and_logger("INFO", "finished clicking main delete button of sender mail blacklist!")

    @allure.step("Start  clicking confirm delete button of sender mail blacklist!")
    def delete_list_item_confirmation(self):
        self.page.wait_for_timeout(2000)
        self.confirm_delete.click()
        self.page.wait_for_timeout(2000)
        Reporting.report_allure_and_logger("INFO", "finished clicking confirm delete button of sender mail blacklist!")

    @allure.step("Start  clicking display mails list button of sender mail blacklist!")
    def click_display_list_item(self):
        self.display_mails_list1.click()
        Reporting.report_allure_and_logger("INFO",
                                           "finished clicking display mails list button of sender mail blacklist!")

    @allure.step("Start  get mails list count on sender mail whitelist!")
    def get_list_item_count(self):
        Reporting.report_allure_and_logger("INFO",
                                           "Getting mails list count on sender mail whitelist!")

        return self.mail_list_items.count()

    @allure.step("Start  clicking search mails list  on sender mail blacklist!")
    def search_list(self, mail_to_search):
        self.search_mail_input.fill(mail_to_search)
        self.search_mail_operation.click()
        Reporting.report_allure_and_logger("INFO", "finished clicking search button of sender mail blacklist!")

    # TODO: FIX(get id?)
    # @allure.step("TO FIX")
    # @allure.step("Start")
    # def click_cancel_search(self):
    #     self.page.locator("text=Sender Email Address Blacklist1 Address Add Address >> button").nth(1).press("Enter")
    #     Reporting.report_allure_and_logger("INFO", "finished clicking CANCEL search button of sender mail blacklist!")

    @allure.step("Start performing cancel search  of sender mail blacklist!")
    def cancel_search(self):
        self.search_mail_input.fill("")
        self.page.reload()
        Reporting.report_allure_and_logger("INFO", "After performing cancel search  of sender mail blacklist!")

    @allure.step("Start clicking Edit of mail(on mails list)!  of sender mail whitelist!")
    def click_edit_list_item(self):
        self.edit_button.click()
        Reporting.report_allure_and_logger("INFO", "clicking Edit of mail(on mails list)!  of sender mail whitelist!")

    @allure.step("Start clicking Edit save button   of sender mail blacklist!")
    def click_save_list_item_changes(self):
        self.save_changes_button.click()
        Reporting.report_allure_and_logger("INFO", "After  clicking Edit save button   of sender mail blacklist!")

    @allure.step("Returning IP black list(first/Second)")
    def get_list_item(self, params_dictionary, is_first, is_xray):
        if is_first:
            if is_xray:
                return params_dictionary.get("XRAY_SENDER_BLACK_LIST_IP1")
            else:
                return params_dictionary.get("ACRONIS_SENDER_BLACK_LIST_IP1")
        else:
            if is_xray:
                return params_dictionary.get("XRAY_SENDER_BLACK_LIST_IP2")
            else:
                return params_dictionary.get("ACRONIS_SENDER_BLACK_LIST_IP2")
