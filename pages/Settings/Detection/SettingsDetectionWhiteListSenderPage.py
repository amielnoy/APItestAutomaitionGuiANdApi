import allure
from playwright.sync_api import expect

from pages.Settings.SettingsDetectionBasePage import SettingsDetectionBasePage
from Utils.Reporting.Reporting import Reporting


class SettingsDetectionSenderWhiteListPage(SettingsDetectionBasePage):
    URL = 'https://xray.testing.perception-point.io/settings/detection'

    def __init__(self, page, is_acronis):
        self.page = page
        self.is_acronis = is_acronis

        self.add_whitelist_mail_button = page.locator("id=email-whitelist-create")
        # page.get_by_role("heading", name="Sender Email Address Whitelist 0 Addresses Add Address").get_by_role("button", name="Add Address")
        #
        self.search_mail_input = page.locator("[placeholder=\"Search\"]")
        self.search_mail_operation = page.locator("id=circle")

        self.reciepent_email_to_add_address = page.locator("input[name=\"Sender Email Address\"]")
        self.add_mail_button = page.locator("button:has-text(\"Add Sender Email Address\")")

        self.mail_list_items = page.locator(
            "xpath=//li/div[@class='GridItem__wrapper--2qjuB SettingsList__grid-item-wrapper--16xCW is-boxshadow is-expandable is-content is-collapsed']")
        self.white_list_sender_mails_number_label = page.get_by_text("Addresses")
        self.display_mails_list1 = page.locator("id=email-whitelist")

        self.main_deleted = page.locator("text=Delete")
        self.confirm_delete = page.get_by_role("button", name="Delete Address from Whitelist")

        self.edit_button = page.locator("button:has-text(\"Edit\")")
        self.save_changes_button = page.locator("button:has-text(\"Save Changes\")")
        self.bad_request_error_message = page.locator("text=Bad Request")
        # locate by substring
        self.succesfull_mail_adding_message = page.locator("text=Added Sender Address to Whitelist: ")

        # self.cancel_search = page.locator("//button[@title='Clear']/span/span")
        super().__init__(self.page, self.URL, self.is_acronis)

    @allure.step("Start clicking  add whitelist mail button on detection PAGE")
    def click_add_to_list(self):
        self.add_whitelist_mail_button.click(force=True)
        Reporting.report_allure_and_logger("INFO", "Finished Clicking  add whitelist mail button on detection PAGE")

    @allure.step("Start setting  sender  whitelist mail email address on detection PAGE")
    def set_filled_item_name_to_add_list(self, mail_address):
        self.reciepent_email_to_add_address.fill(mail_address)
        Reporting.report_allure_and_logger("INFO", "finished setting sender mail whitelist!")

    @allure.step("Start  clicking add sender mail whitelist BUTTON! on detection PAGE")
    def click_add_item_button_to_add_list(self):
        self.add_mail_button.click()
        Reporting.report_allure_and_logger("INFO", "finished clicking add sender mail whitelist BUTTON!")

    @allure.step("Start  clicking main delete button of sender mail whitelist!")
    def click_delete_list_item(self):
        Reporting.report_allure_and_logger("INFO", "Started clicking main delete button of sender mail whitelist!")
        string_locator_acronis = self.build_locator_string(gui_item_position=1
                                                           , locator_prefix_string="//ul/li["
                                                           ,
                                                           locator_suffix_string="]/div/div/div[4]/div/div[2]/button/span/span[2]")
        string_locator_xray = self.build_locator_string(gui_item_position=1
                                                        , locator_prefix_string="//ul/li["
                                                        ,
                                                        locator_suffix_string="]/div/div/div[5]/div/div[2]/button/span/span[2]")

        if self.is_acronis:
            expect(self.page.locator(string_locator_acronis)).to_be_visible(timeout=10000)
            self.page.locator(string_locator_acronis).click()
        else:
            expect(self.page.locator(string_locator_xray)).to_be_visible(timeout=10000)
            self.page.locator(string_locator_xray).click()
        Reporting.report_allure_and_logger("INFO", "finished clicking main delete button of sender mail whitelist!")

    @allure.step("Start  clicking confirm delete button of sender mail whitelist!")
    def delete_list_item_confirmation(self):
        self.page.wait_for_timeout(2000)
        self.confirm_delete.click()
        self.page.wait_for_timeout(2000)
        Reporting.report_allure_and_logger("INFO", "finished clicking confirm delete button of sender mail whitelist!")

    @allure.step("Start  clicking display mails list button of sender mail whitelist!")
    def click_display_list_item(self):
        self.display_mails_list1.click()
        Reporting.report_allure_and_logger("INFO",
                                           "finished clicking display mails list button of sender mail whitelist!")

    @allure.step("Start  get white list mails count on sender mail whitelist!")
    def get_list_item_count(self):
        Reporting.report_allure_and_logger("INFO",

                                           "Finished get white list mails count on sender mail whitelist!")
        return self.mail_list_items.count()

    @allure.step("Start  get white list sender mails count(label) on sender mail whitelist!")
    def get_label_list_item_number(self):
        Reporting.report_allure_and_logger("INFO",

                                           "Finished get sender white list mails count on sender mail whitelist!")
        return self.white_list_sender_mails_number_label.nth(0).inner_html()

    @allure.step("Start  clicking search mails list  on sender mail whitelist!")
    def search_list(self, mail_to_search):
        self.search_mail_input.fill(mail_to_search)
        self.search_mail_operation.click()
        Reporting.report_allure_and_logger("INFO", "finished clicking search button of sender mail whitelist!")

    # TODO: FIX(get id?)
    # @allure.step("TO FIX")
    # @allure.step("Start")
    # def click_cancel_search(self):
    #     Reporting.report_allure_and_logger("INFO", "Started clicking CANCEL search button of sender mail whitelist!")
    #     # self.cancel_search.click()
    #     self.page.locator("text=Sender Email Address Whitelist1 Address Add Address >> button").nth(1).press("Enter")
    #     Reporting.report_allure_and_logger("INFO", "finished clicking CANCEL search button of sender mail whitelist!")

    @allure.step("Start performing cancel search  of sender mail whitelist!")
    def cancel_search(self):
        self.search_mail_input.fill("")
        self.page.reload()
        Reporting.report_allure_and_logger("INFO", "After performing cancel search  of sender mail whitelist!")

    @allure.step("Start clicking Edit of mail(on mails list)!  of sender mail whitelist!")
    def click_edit_list_item(self):
        self.edit_button.click()
        Reporting.report_allure_and_logger("INFO", "clicking Edit of mail(on mails list)!  of sender mail whitelist!")

    @allure.step("Start clicking Edit save button   of sender mail whitelist!")
    def click_save_list_item_changes(self):
        self.save_changes_button.click()
        Reporting.report_allure_and_logger("INFO", "After  clicking Edit save button   of sender mail whitelist!")

    @allure.step("Returning White  list sender(first/Second)")
    def get_list_item(self, params_dictionary, is_first, is_xray):
        if is_first:
            if is_xray:
                return params_dictionary.get("XRAY_SENDER_WHITE_LIST_EMAIL1")
            else:
                return params_dictionary.get("ACRONIS_SENDER_WHITE_LIST_EMAIL1")
        else:
            if is_xray:
                return params_dictionary.get("XRAY_SENDER_WHITE_LIST_EMAIL2")
            else:
                return params_dictionary.get("ACRONIS_SENDER_WHITE_LIST_EMAIL2")
