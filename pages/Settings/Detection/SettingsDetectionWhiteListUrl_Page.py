import allure

from pages.Settings.SettingsDetectionBasePage import SettingsDetectionBasePage
from Utils.Reporting.Reporting import Reporting


class SettingsDetectionUrlWhiteListPage(SettingsDetectionBasePage):
    URL = 'https://xray.testing.perception-point.io/settings/detection'

    def __init__(self, page, is_acronis):
        self.page = page
        self.is_acronis = is_acronis

        self.add_whitelist_mail_button = page.locator("id=url-whitelist-create")
        # page.get_by_role("heading", name="URL Whitelist 3 URLs Add URL").get_by_role(
        # "button", name="Add URL")
        self.search_url_input = page.locator("[placeholder=\"Search\"]")
        self.search_url_operation = page.locator("id=circle")

        self.white_list_url_to_add = page.locator("input[name=\"URL\"]")
        self.add_url_button = page.locator("div[role=\"document\"] button:has-text(\"Add URL\")")

        self.urls_list_items = page.locator(
            "xpath=//li/div[@class='GridItem__wrapper--2qjuB SettingsList__grid-item-wrapper--16xCW is-boxshadow is-expandable is-content is-collapsed']")
        self.white_list_url_label = page.get_by_text("URLs")
        self.display_urls_list1 = page.locator("id=url-whitelist")

        self.main_deleted = page.locator("button:has-text(\"Delete\")")
        self.confirm_delete = page.get_by_role("button", name="Delete URL from Whitelist")

        self.edit_button = page.locator("button:has-text(\"Edit\")")
        self.save_changes_button = page.locator("button:has-text(\"Save Changes\")")
        self.bad_request_error_message = page.locator("text=Bad Request")
        # locate by substring
        self.succesfull_url_whitelist_adding_message = page.locator("text=Added Sender URL to Whitelist: ")
        # self.cancel_search = page.locator("//button[@title='Clear']/span/span")
        super().__init__(self.page, self.URL, self.is_acronis)

    @allure.step("Start clicking add whitelist URL button on detection PAGE")
    def click_add_to_list(self):
        Reporting.report_allure_and_logger("INFO", "Before clicking  add whitelist URL button on detection PAGE")
        self.add_whitelist_mail_button.click(force=True)
        Reporting.report_allure_and_logger("INFO", "Finished Clicking  add whitelist URL button on detection PAGE")

    @allure.step("Start setting sender whitelist URL address on detection PAGE")
    def set_filled_item_name_to_add_list(self, url_address):
        Reporting.report_allure_and_logger("INFO", "Before setting sender IP whitelist!")
        self.white_list_url_to_add.fill(url_address)
        Reporting.report_allure_and_logger("INFO", "finished setting sender URL whitelist!")

    @allure.step("Start clicking add sender url whitelist BUTTON! on detection PAGE")
    def click_add_item_button_to_add_list(self):
        Reporting.report_allure_and_logger("INFO", "Before clicking add url whitelist BUTTON!")
        self.add_url_button.click()
        Reporting.report_allure_and_logger("INFO", "finished clicking add sender url whitelist BUTTON!")

    @allure.step("Start clicking main delete button of sender url whitelist!")
    def click_delete_list_item(self):
        Reporting.report_allure_and_logger("INFO", "Before clicking main delete button of url whitelist!")
        locator_prefix = '//ul/li['

        acronis_locator_suffix = "]/div/div/div[5]/div/div[2]/button/span/span[2]"
        xray_locator_suffix = "]/div/div/div[6]/div/div[2]/button/span/span[2]"
        if self.is_acronis:
            self.delete_highest_detection_item_from_list(locator_prefix=locator_prefix
                                                         , locator_suffix=acronis_locator_suffix)
        else:
            self.delete_highest_detection_item_from_list(locator_prefix=locator_prefix
                                                         , locator_suffix=xray_locator_suffix)
        Reporting.report_allure_and_logger("INFO", "finished clicking main delete button of sender mail blacklist!")
        Reporting.report_allure_and_logger("INFO", "Finished clicking main delete button of url whitelist!")

    @allure.step("Start  clicking confirm delete button of url whitelist!")
    def delete_list_item_confirmation(self):
        self.page.wait_for_timeout(2000)
        self.confirm_delete.click()
        self.page.wait_for_timeout(2000)
        Reporting.report_allure_and_logger("INFO", "finished clicking confirm delete button of url whitelist!")

    @allure.step("Start  clicking display URL list button of URL'S whitelist!")
    def click_display_list_item(self):
        self.display_urls_list1.click()
        Reporting.report_allure_and_logger("INFO",
                                           "finished clicking display urls list button of urls whitelist!")

    @allure.step("Start  get URL's list count on urls whitelist!")
    def get_list_item_count(self):
        return self.urls_list_items.count()

    # @allure.step("Start  get white list sender mails count(label) on sender mail whitelist!")
    # def get_list_item_count(self):
    #     return self.white_list_url_label.nth(0).inner_html()

    @allure.step("Start  get URL'S whitelist  count(label) on URL'S whitelist!")
    def get_label_list_item_number(self):
        return self.white_list_url_label.nth(0).inner_html()

    @allure.step("Start  clicking search urls list  on urls whitelist!")
    def search_list(self, url_to_search):
        self.search_url_input.fill(url_to_search)
        self.search_url_operation.click()
        Reporting.report_allure_and_logger("INFO", "finished clicking search button of urls whitelist!")

    # TODO: FIX(get id?)
    # @allure.step("TO FIX")
    # @allure.step("Start")
    # def click_cancel_search(self):
    #     self.page.locator("text=Sender Url Address Whitelist1 Address Add Address >> button").nth(1).press("Enter")
    #     Reporting.report_allure_and_logger("INFO", "finished clicking CANCEL search button of utls whitelist!")

    @allure.step("Start performing cancel search  of sender urls whitelist!")
    def cancel_search(self):
        self.search_url_input.fill("")
        self.page.reload()
        Reporting.report_allure_and_logger("INFO", "After performing cancel search of urls whitelist!")

    @allure.step("Start clicking Edit of WHITELIST URL(on url list)!  of urls whitelist!")
    def click_edit_list_item(self):
        self.edit_button.click()
        Reporting.report_allure_and_logger("INFO",
                                           "Finish clicking Edit of WHITELIST URL(on url list)!  of urls whitelist!")

    @allure.step("Start clicking Edit save button of urls whitelist!")
    def click_save_list_item_changes(self):
        self.save_changes_button.click()
        Reporting.report_allure_and_logger("INFO", "After  clicking Edit save button   of urls whitelist!")

    @allure.step("Returning URL White list(first/Second)")
    def get_list_item(self, params_dictionary, is_first, is_xray):
        if is_first:
            if is_xray:
                return params_dictionary.get("XRAY_URL_WHITE_LIST1")
            else:
                return params_dictionary.get("ACRONIS_URL_WHITE_LIST1")
        else:
            if is_xray:
                return params_dictionary.get("XRAY_URL_WHITE_LIST2")
            else:
                return params_dictionary.get("ACRONIS_URL_WHITE_LIST2")
