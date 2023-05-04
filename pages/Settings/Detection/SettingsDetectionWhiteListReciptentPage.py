import allure

from pages.Settings.SettingsDetectionBasePage import SettingsDetectionBasePage
from Utils.Reporting.Reporting import Reporting


class SettingsDetectionReciptentWhiteListPage(SettingsDetectionBasePage):
    URL = 'https://xray.testing.perception-point.io/settings/detection'

    def __init__(self, page, is_acronis):
        self.page = page
        self.add_whitelist_mail_button = page.locator("//*[@id='recipient-whitelist-create']")
        self.is_acronis = is_acronis
        # page.get_by_role("heading",
        # name="Recipient Email Address Whitelist 0 Addresses Add Address").get_by_role("button",
        # name="Add Address")
        # page.locator("id=recipient-whitelist-create")
        self.search_mail_input = page.locator("[placeholder=\"Search\"]")
        self.search_mail_operation = page.locator("id=circle")

        self.reciepent_email_to_set = page.locator("input[name=\"Recipient\\ Email\\ Address\"]")
        self.add_mail_button = page.locator("text=Add Recipient Email Address")
        self.mail_list_items = page.locator(
            "xpath=//li/div[@class='GridItem__wrapper--2qjuB SettingsList__grid-item-wrapper--16xCW is-boxshadow is-expandable is-content is-collapsed']")
        self.display_mails_list1 = page.locator("id=recipient-whitelist")
        self.recipitent_whitelist_mails_number_label = page.get_by_text("Addresses")

        self.main_deleted = page.locator("(//span[text()='Delete'])[1]")
        self.confirm_delete = page.get_by_role("button", name="Delete Recipient Address from Whitelist")

        self.edit_button = page.locator("button:has-text(\"Edit\")")
        self.save_changes_button = page.locator("button:has-text(\"Save Changes\")")
        self.bad_request_error_message = page.locator("text=Bad Request")
        # locate by substring
        # self.succesfull_mail_adding_message = page.locator("text=Added Recipient Address to Whitelist: ")
        self.succesfull_Recipient_mail_adding_message = page.locator("text=Added Recipient Address to Whitelist: ")
        # self.cancel_search = page.locator("//button[@title='Clear']/span/span")
        super().__init__(self.page, self.URL, self.is_acronis)

    @allure.step("Start clicking  add RECIEPTENT whitelist mail button on detection PAGE")
    def click_add_to_list(self):
        Reporting.report_allure_and_logger("INFO",
                                           "Started Clicking  add RECIEPTENT whitelist mail button on detection PAGE")
        self.add_whitelist_mail_button.click(force=True)
        self.page.wait_for_timeout(1000)
        Reporting.report_allure_and_logger("INFO",
                                           "Finished Clicking  add RECIEPTENT whitelist mail button on detection PAGE")

    @allure.step("Start setting RECIEPTENT   whitelist mail email address on detection PAGE")
    def set_filled_item_name_to_add_list(self, mail_address):
        self.reciepent_email_to_set.fill(mail_address)
        Reporting.report_allure_and_logger("INFO", "finished setting RECIEPTENT  mail whitelist!")

    @allure.step("Start  clicking add RECIEPTENT mail whitelist BUTTON! on detection PAGE")
    def click_add_item_button_to_add_list(self):
        self.add_mail_button.nth(1).click()
        Reporting.report_allure_and_logger("INFO", "finished clicking add RECIEPTENT mail whitelist BUTTON!")

    @allure.step("Start  clicking main delete button of RECIEPTENT mail whitelist!")
    def click_delete_list_item(self):
        Reporting.report_allure_and_logger("INFO", "Starting clicking main delete button of RECIEPTENT mail whitelist!")

        locator_prefix = "//div[2]/div/div/ul/li["
        acronis_locator_suffix = "]/div/div/div[4]/div/div[2]/button/span/span[2]"
        xray_locator_suffix = "]/div/div/div[5]/div/div[2]/button/span/span[2]"

        if self.is_acronis:
            self.delete_highest_detection_item_from_list(locator_prefix=locator_prefix
                                                         , locator_suffix=acronis_locator_suffix)
        else:
            self.delete_highest_detection_item_from_list(locator_prefix=locator_prefix
                                                         , locator_suffix=xray_locator_suffix)

        Reporting.report_allure_and_logger("INFO", "finished clicking main delete button of RECIEPTENT mail whitelist!")

    @allure.step("Start  clicking confirm delete button of RECIEPTENT mail whitelist!")
    def delete_list_item_confirmation(self):
        self.page.wait_for_timeout(2000)
        self.confirm_delete.click()
        self.page.wait_for_timeout(2000)
        Reporting.report_allure_and_logger("INFO",
                                           "finished clicking confirm delete button of RECIEPTENT mail whitelist!")

    @allure.step("Start  clicking display mails list button of RECIEPTENT mail whitelist!")
    def click_display_list_item(self):
        self.display_mails_list1.click()
        Reporting.report_allure_and_logger("INFO",
                                           "finished clicking display mails list button of RECIEPTENT mail whitelist!")

    @allure.step("Start  get mails list count on sender mail whitelist!")
    def get_list_item_count(self):
        Reporting.report_allure_and_logger("INFO",
                                           "getting mails list count on RECIEPTENT mail whitelist!")

        return self.mail_list_items.count()

    @allure.step("Start  getting mail number text RECIEPTENT mailWHITElist label! on detection PAGE")
    def get_label_list_item_number(self):
        return self.recipitent_whitelist_mails_number_label.nth(1).inner_html()

    @allure.step("Start  clicking search mails list  on RECIEPTENT mail whitelist!")
    def search_list(self, mail_to_search):
        self.search_mail_input.fill(mail_to_search)
        self.search_mail_operation.click()
        Reporting.report_allure_and_logger("INFO", "finished clicking search button of RECIEPTENT mail whitelist!")

    # TODO: FIX(get id?)
    # @allure.step("TO FIX")
    # @allure.step("Start clicking CANCEL search button of RECIEPTENT mail whitelist!")
    # def click_cancel_search(self):
    #     self.page.locator("text=Sender Email Address Whitelist1 Address Add Address >> button").nth(1).press("Enter")
    #     Reporting.report_allure_and_logger("INFO",
    #                                        "finished clicking CANCEL search button of RECIEPTENT mail whitelist!")

    @allure.step("Start performing cancel search  of RECIEPTENT  mail whitelist!")
    def cancel_search(self):
        self.search_mail_input.fill("")
        self.page.reload()
        Reporting.report_allure_and_logger("INFO", "After performing cancel search  of RECIEPTENT  mail whitelist!")

    @allure.step("Start clicking Edit of mail(on mails list)!  of RECIEPTENT  mail whitelist!")
    def click_edit_list_item(self):
        self.edit_button.click()
        Reporting.report_allure_and_logger("INFO",
                                           "clicking Edit of mail(on mails list)!  of RECIEPTENT  mail whitelist!")

    @allure.step("Start clicking Edit save button   of RECIEPTENT  mail whitelist!")
    def click_save_list_item_changes(self):
        self.save_changes_button.click()
        Reporting.report_allure_and_logger("INFO", "After  clicking Edit save button   of RECIEPTENT  mail whitelist!")

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
