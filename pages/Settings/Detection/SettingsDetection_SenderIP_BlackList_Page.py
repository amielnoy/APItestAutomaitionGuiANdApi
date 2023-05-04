import allure

from Utils.Reporting.Reporting import Reporting
from pages.Settings.SettingsDetectionBasePage import SettingsDetectionBasePage


class SettingsDetectionSenderIpBlackListPage(SettingsDetectionBasePage):

    def __init__(self, page, base_url, is_acronis):
        self.page = page
        self.is_acronis = is_acronis
        self.add_black_mail_button_to_ip_list = page.locator("id=ip-blacklist-create")
        self.search_ip_input = page.locator("[placeholder=\"Search\"]")
        self.search_ip_operation = page.locator("id=circle")

        self.black_list_ip_to_add = page.locator("input[name=\"Sender\\ IP\"]")
        self.add_ip_button = page.locator("button:has-text(\"Add Sender IP\")")

        self.ips_list_items = page.locator(
            "xpath=//li/div[@class='GridItem__wrapper--2qjuB SettingsList__grid-item-wrapper--16xCW is-boxshadow is-expandable is-content is-collapsed']")

        self.black_list_ips_number_label = page.get_by_text("IPs")
        self.display_ips_list1 = page.locator("id=ip-blacklist")

        # self.main_deleted = page.get_by_role("button",
        #                                     name="bing.com1 Starts With Normal Malicious Created at Dec 25, 2022 by Amiel Peled Edit Delete").get_by_role(
        #    "button", name="Delete")
        # page.locator("button:has-text(\"Delete\")")
        self.page.main_deleted1_xray = page.locator("//ul/li[1]/div/div/div[7]/div/div[2]/button/span/span[2]")
        self.page.main_deleted2_xray = page.locator("//ul/li[2]/div/div/div[7]/div/div[2]/button/span/span[2]")
        self.confirm_delete = page.get_by_role("button", name="Delete IP from Blacklist")

        self.edit_button = page.locator("button:has-text(\"Edit\")")
        self.save_changes_button = page.locator("button:has-text(\"Save Changes\")")
        self.bad_request_error_message = page.locator("text=Bad Request")
        # locate by substring
        self.succesfull_ip_blacklist_adding_message = page.locator("text=Added Sender IP to Blacklist:")
        # self.cancel_search = page.locator("//button[@title='Clear']/span/span")
        super().__init__(page, base_url, self.is_acronis)

    def debug_base_detection(self):
        print("debug_base_detection")

    @allure.step("Start clicking  add IP blacklist  button on detection PAGE")
    def click_add_to_list(self):
        self.add_black_mail_button_to_ip_list.click(force=True)
        Reporting.report_allure_and_logger("INFO", "Finished Clicking  add IP blacklist button on detection PAGE")

    @allure.step("Start setting  sender  blacklist ip address on detection PAGE")
    def set_filled_item_name_to_add_list(self, mail_address):
        self.black_list_ip_to_add.fill(mail_address)
        Reporting.report_allure_and_logger("INFO", "finished setting sender ip blacklist!")

    @allure.step("Start  clicking add sender ip blacklist BUTTON! on detection PAGE")
    def click_add_item_button_to_add_list(self):
        Reporting.report_allure_and_logger("INFO", "Starting clicking add sender ip blacklist BUTTON!")
        self.add_ip_button.click()
        Reporting.report_allure_and_logger("INFO", "finished clicking add sender ip blacklist BUTTON!")

    @allure.step("Start  clicking main delete button of sender ip blacklist!")
    def click_delete_list_item(self):
        print("Deleting in data member of Setting detection Black List sender ip!!!")
        locator_prefix = '//ul/li['
        acronis_locator_suffix = ']/div/div/div[4]/div/div[2]/button/span/span[2]'
        xray_locator_suffix = ']/div/div/div[5]/div/div[2]/button/span/span[2]'
        if self.is_acronis:
            self.delete_highest_detection_item_from_list(locator_prefix=locator_prefix
                                                         , locator_suffix=acronis_locator_suffix)
        else:
            self.delete_highest_detection_item_from_list(locator_prefix=locator_prefix
                                                         , locator_suffix=xray_locator_suffix)
        Reporting.report_allure_and_logger("INFO", "finished clicking main delete button of sender ip blacklist!")

    @allure.step("Start  clicking confirm delete button of sender ip blacklist!")
    def delete_list_item_confirmation(self):
        self.page.wait_for_timeout(2000)
        self.confirm_delete.click()
        self.page.wait_for_timeout(2000)
        Reporting.report_allure_and_logger("INFO", "finished clicking confirm delete button of sender ip blacklist!")

    @allure.step("Start  clicking display mails list button of sender ips blacklist!")
    def click_display_list_item(self):
        Reporting.report_allure_and_logger("INFO",
                                           "Started clicking display ips list button of sender ips blacklist!")
        self.display_ips_list1.click()
        Reporting.report_allure_and_logger("INFO",
                                           "finished clicking display ips list button of sender ips blacklist!")

    @allure.step("Start  get ips black list count on sender ips blacklist!")
    def get_list_item_count(self):
        number_of_mails_after_adding = self.ips_list_items.count()
        Reporting.report_allure_and_logger("INFO",
                                           "Finished getting mails list count on sender mail blacklist!==" + str(
                                               number_of_mails_after_adding))
        return number_of_mails_after_adding

    @allure.step("Start  get ips black list count(label) on sender ips blacklist")
    def get_label_list_item_number(self):
        Reporting.report_allure_and_logger("INFO",
                                           "Start  get ips black list count(label) on sender ips blacklist")
        return self.black_list_ips_number_label.nth(1).inner_html()

    @allure.step("Start  clicking search ips list  on sender ips blacklist!")
    def search_list(self, ip_to_search):
        self.search_ip_input.fill(ip_to_search)
        self.search_ip_operation.click()
        Reporting.report_allure_and_logger("INFO", "finished clicking search button of sender ips blacklist!")

    # TODO: FIX(get id?)
    # @allure.step("TO FIX")
    # @allure.step("Start clicking CANCEL search button of sender ips blacklist!")
    # def click_cancel_search(self):
    #     self.page.locator("text=Sender Email Address Blacklist1 Address Add Address >> button").nth(1).press("Enter")
    #     Reporting.report_allure_and_logger("INFO", "finished clicking CANCEL search button of sender ips blacklist!")

    @allure.step("Start performing cancel search  of sender ips blacklist!")
    def cancel_search(self):
        self.search_ip_input.fill("")
        self.page.reload()
        Reporting.report_allure_and_logger("INFO", "After performing cancel search  of sender ips blacklist!")

    @allure.step("Start clicking Edit of mail(on ips list)!  of sender ips blacklist!")
    def click_edit_list_item(self):
        self.edit_button.click()
        Reporting.report_allure_and_logger("INFO", "clicking Edit of ip(on ips list)!  of sender ip blacklist!")

    @allure.step("Start clicking Edit save button   of sender ips blacklist!")
    def click_save_list_item_changes(self):
        self.save_changes_button.click()
        Reporting.report_allure_and_logger("INFO", "After  clicking Edit save button   of sender ips blacklist!")

    @allure.step("Returning IP black list(first/Second)")
    def get_list_item(self, params_dictionary, is_first, is_acronis):
        if is_first:
            if not is_acronis:
                return params_dictionary.get("XRAY_SENDER_BLACK_LIST_IP1")
            else:
                return params_dictionary.get("ACRONIS_SENDER_BLACK_LIST_IP1")
        else:
            if not is_acronis:
                return params_dictionary.get("XRAY_SENDER_BLACK_LIST_IP2")
            else:
                return params_dictionary.get("ACRONIS_SENDER_BLACK_LIST_IP2")
