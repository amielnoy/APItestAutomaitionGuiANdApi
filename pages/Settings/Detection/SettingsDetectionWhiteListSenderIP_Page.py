import allure

from pages.Settings.SettingsDetectionBasePage import SettingsDetectionBasePage
from Utils.Reporting.Reporting import Reporting


class SettingsDetectionSenderIpWhiteListPage(SettingsDetectionBasePage):
    URL = 'https://xray.testing.perception-point.io/settings/detection'

    def __init__(self, page, is_acronis):
        self.page = page
        self.is_acronis = is_acronis

        self.add_whitelist_mail_button = page.locator("id=ip-whitelist-create")
        self.search_ip_input = page.locator("[placeholder=\"Search\"]")
        self.search_ip_operation = page.locator("id=circle")

        self.white_list_ip_to_add = page.locator("input[name=\"Sender\\ IP\"]")
        self.add_ip_button = page.locator("button:has-text(\"Add Sender IP\")")

        self.ips_list_items = page.locator(
            "xpath=//li/div[@class='GridItem__wrapper--2qjuB SettingsList__grid-item-wrapper--16xCW is-boxshadow is-expandable is-content is-collapsed']")
        self.white_list_sender_ip_number_label = page.get_by_text("IPs")

        self.display_ips_list1 = page.locator("id=ip-whitelist")

        self.main_deleted = page.locator("button:has-text(\"Delete\")")
        self.confirm_delete = page.get_by_role("button", name="Delete IP from Whitelist")

        self.edit_button = page.locator("button:has-text(\"Edit\")")
        self.save_changes_button = page.locator("button:has-text(\"Save Changes\")")
        self.bad_request_error_message = page.locator("text=Bad Request")
        # locate by substring
        self.succesfull_ip_whitelist_adding_message = page.locator("text=Added Sender IP to Whitelist:")

        # self.cancel_search = page.locator("//button[@title='Clear']/span/span")
        super().__init__(self.page, self.URL, self.is_acronis)

    @allure.step("Start clicking add whitelist IP button on detection PAGE")
    def click_add_to_list(self):
        Reporting.report_allure_and_logger("INFO", "Before clicking  add whitelist IP button on detection PAGE")
        self.add_whitelist_mail_button.click(force=True)
        Reporting.report_allure_and_logger("INFO", "Finished Clicking  add whitelist IP button on detection PAGE")

    @allure.step("Start setting sender whitelist IP address on detection PAGE")
    def set_filled_item_name_to_add_list(self, ip_address):
        Reporting.report_allure_and_logger("INFO", "Before setting sender IP whitelist!")
        self.white_list_ip_to_add.fill(ip_address)
        Reporting.report_allure_and_logger("INFO", "finished setting sender IP whitelist!")

    @allure.step("Start  clicking add sender ip whitelist BUTTON! on detection PAGE")
    def click_add_item_button_to_add_list(self):
        Reporting.report_allure_and_logger("INFO", "Before clicking add sender ip whitelist BUTTON!")
        self.add_ip_button.click()
        Reporting.report_allure_and_logger("INFO", "finished clicking add sender ip whitelist BUTTON!")

    @allure.step("Start  clicking main delete button of sender ip whitelist!")
    def click_delete_list_item(self):
        Reporting.report_allure_and_logger("INFO", "Before clicking main delete button of sender ip whitelist!")
        locator_prefix = "//div[4]/div/div/ul/li["
        acronis_locator_suffix = "]/div/div/div[4]/div/div[2]/button/span/span[2]"
        xray_locator_suffix = "]/div/div/div[5]/div/div[2]/button/span/span[2]"

        if self.is_acronis:
            self.delete_highest_detection_item_from_list(locator_prefix=locator_prefix
                                                         , locator_suffix=acronis_locator_suffix)
        else:
            self.delete_highest_detection_item_from_list(locator_prefix=locator_prefix
                                                         , locator_suffix=xray_locator_suffix)
        Reporting.report_allure_and_logger("INFO", "Finished clicking main delete button of sender ip whitelist!")

    @allure.step("Start  clicking confirm delete button of sender ip whitelist!")
    def delete_list_item_confirmation(self):
        self.page.wait_for_timeout(2000)
        self.confirm_delete.click()
        self.page.wait_for_timeout(2000)
        Reporting.report_allure_and_logger("INFO", "finished clicking confirm delete button of sender ip whitelist!")

    @allure.step("Start  clicking display IP list button of sender ips whitelist!")
    def click_display_list_item(self):
        self.display_ips_list1.click()
        Reporting.report_allure_and_logger("INFO",
                                           "finished clicking display ips list button of sender ips whitelist!")

    @allure.step("Start  get IP's list count on sender ips whitelist!")
    def get_list_item_count(self):
        return self.ips_list_items.count()

    @allure.step("Start  getting ip's list count  of sender ips from label! on detection PAGE")
    def get_label_list_item_number(self):
        return self.white_list_sender_ip_number_label.nth(0).inner_html()

    @allure.step("Start  clicking search ips list  on sender ips whitelist!")
    def search_list(self, ip_to_search):
        self.search_ip_input.fill(ip_to_search)
        self.search_ip_operation.click()
        Reporting.report_allure_and_logger("INFO", "finished clicking search button of sender ips whitelist!")

    # TODO: FIX(get id?)
    # @allure.step("TO FIX")
    # @allure.step("Start")
    # def click_cancel_search(self):
    #     Reporting.report_allure_and_logger("INFO", "Starting clicking CANCEL search button of sender ips whitelist!")
    #     self.page.locator("text=Sender Email Address Whitelist1 Address Add Address >> button").nth(1).press("Enter")
    #     Reporting.report_allure_and_logger("INFO", "finished clicking CANCEL search button of sender ips whitelist!")

    @allure.step("Start performing cancel search  of sender ips whitelist!")
    def cancel_search(self):
        self.search_ip_input.fill("")
        self.page.reload()
        Reporting.report_allure_and_logger("INFO", "After performing cancel search of sender ips whitelist!")

    @allure.step("Start clicking Edit of IP(on ips list)!  of sender ips whitelist!")
    def click_edit_list_item(self):
        self.edit_button.click()
        Reporting.report_allure_and_logger("INFO", "clicking Edit of ip(on ips list)!  of sender ip whitelist!")

    @allure.step("Start clicking Edit save button of sender ips whitelist!")
    def click_save_list_item_changes(self):
        self.save_changes_button.click()
        Reporting.report_allure_and_logger("INFO", "After  clicking Edit save button   of sender ips whitelist!")

    @allure.step("Returning sender white list(first/Second) Mail")
    def get_list_item(self, params_dictionary, is_first, is_xray):
        if is_first:
            if is_xray:
                return params_dictionary.get("XRAY_SENDER_WHITE_LIST_IP1")
            else:
                return params_dictionary.get("ACRONIS_SENDER_WHITE_LIST_IP1")
        else:
            if is_xray:
                return params_dictionary.get("XRAY_SENDER_WHITE_LIST_IP2")
            else:
                return params_dictionary.get("ACRONIS_SENDER_WHITE_LIST_IP2")
