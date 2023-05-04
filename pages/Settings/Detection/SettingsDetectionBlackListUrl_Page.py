import allure
from playwright.sync_api import expect
from pytest_base_url.plugin import base_url

from pages.Settings.SettingsDetectionBasePage import SettingsDetectionBasePage
from Utils.Reporting.Reporting import Reporting


class SettingsDetectionUrlBlackListPage(SettingsDetectionBasePage):

    def __init__(self, page, parms_dictionary, is_acronis):
        self.page = page
        self.is_acronis = is_acronis

        if is_acronis:
            self.base_url = parms_dictionary.get('ACRONIS_BASE_URL')
        else:
            self.base_url = parms_dictionary.get('XRAY_BASE_URL')

        self.add_black_url_button = page.locator("id=url-blacklist-create")
        self.search_url_input = page.locator("[placeholder=\"Search\"]")
        self.search_url_operation = page.locator("id=circle")

        self.black_list_url_to_add = page.locator("input[name=\"URL\"]")
        self.add_url_button = page.locator("div[role=\"document\"] button:has-text(\"Add URL\")")
        self.urls_list_items = page.locator(
            "xpath=//li/div[@class='GridItem__wrapper--2qjuB SettingsList__grid-item-wrapper--16xCW is-boxshadow is-expandable is-content is-collapsed']")
        self.black_list_urls_number_label = page.get_by_text("URLs")
        self.display_urls_list1 = page.locator("id=url-blacklist")

        self.page.main_deleted1_xray = page.locator("//ul/li[1]/div/div/div[7]/div/div[2]/button/span/span[2]")
        self.page.main_deleted2_xray = page.locator("//ul/li[2]/div/div/div[7]/div/div[2]/button/span/span[2]")
        self.confirm_delete = page.get_by_role("button", name="Delete URL from Blacklist")

        self.edit_button = page.locator("button:has-text(\"Edit\")")
        self.save_changes_button = page.locator("button:has-text(\"Save Changes\")")
        self.bad_request_error_message = page.locator("text=Bad Request")
        # locate by substring
        self.succesfull_url_blacklist_adding_message = page.locator("text=Added Sender URL to Blacklist: ")
        # self.cancel_search = page.locator("//button[@title='Clear']/span/span")
        super().__init__(self.page, base_url, self.is_acronis)

    def debug_me(self):
        print("debug in SETTING_DETECTION_BLACKLIST_URL debug_me method!!!")

    @allure.step("Start clicking add blacklist URL button on detection PAGE")
    def click_add_to_list(self):
        Reporting.report_allure_and_logger("INFO", "Before clicking  add blacklist URL button on detection PAGE")
        self.add_black_url_button.click(force=True)
        Reporting.report_allure_and_logger("INFO", "Finished Clicking  add blacklist URL button on detection PAGE")

    @allure.step("Start setting blacklist URL address on detection PAGE")
    def set_filled_item_name_to_add_list(self, url_address):
        Reporting.report_allure_and_logger("INFO", "Before setting URL blacklist!")
        self.black_list_url_to_add.fill(url_address)
        Reporting.report_allure_and_logger("INFO", "finished setting URL blacklist!")

    @allure.step("Start clicking add url blacklist BUTTON! on detection PAGE")
    def click_add_item_button_to_add_list(self):
        Reporting.report_allure_and_logger("INFO", "Before clicking add url blacklist BUTTON!")
        self.add_url_button.click()
        Reporting.report_allure_and_logger("INFO", "finished clicking add url blacklist BUTTON!")

    @allure.step("Start clicking main delete button of sender url blacklist!")
    def click_delete_list_item(self, position=1):
        Reporting.report_allure_and_logger("INFO", "Finished clicking main delete button of url blacklist!")
        locator_prefix = '//ul/li['
        acronis_locator_suffix = "]/div/div/div[6]/div/div[2]/button/span/span[2]"
        xray_locator_suffix = "]/div/div/div[7]/div/div[2]/button/span/span[2]"

        string_locator_acronis = self.build_locator_string(gui_item_position=1
                                                           , locator_prefix_string=locator_prefix
                                                           , locator_suffix_string=acronis_locator_suffix)
        string_locator_xray = self.build_locator_string(gui_item_position=1
                                                        , locator_prefix_string=locator_prefix
                                                        , locator_suffix_string=xray_locator_suffix)
        if self.is_acronis:
            expect(self.page.locator(string_locator_acronis)).to_be_visible(timeout=10000)
            self.page.locator(string_locator_acronis).click()
        else:
            expect(self.page.locator(string_locator_xray)).to_be_visible(timeout=10000)
            self.page.locator(string_locator_xray).click()
        Reporting.report_allure_and_logger("INFO", "Finished clicking main delete button of url blacklist!")

    @allure.step("Start  clicking confirm delete button of url blacklist!")
    def delete_list_item_confirmation(self):
        # try:
        self.page.wait_for_timeout(2000)
        self.confirm_delete.click()
        self.page.wait_for_timeout(2000)
        Reporting.report_allure_and_logger("INFO", "finished clicking confirm delete button of url blacklist!")

    # except:
    #     # SetupTearDownOperations.delete_detection_item_by_id_of_item(is_acronis, organization_id, token_value, item_position=1)
    #     SetupTearDownOperations.delete_detection_item_by_id_of_item(self.is_acronis, organization_id, token_value)
    #     raise AssertionError("Failed to delete black list url using gui clicking!!")

    @allure.step("Start  clicking display URL list button of URL'S blacklist!")
    def click_display_list_item(self):
        self.display_urls_list1.click()
        Reporting.report_allure_and_logger("INFO",
                                           "finished clicking display urls list button of urls blacklist!")

    @allure.step("Start  get URL's black list count on urls blacklist!")
    def get_list_item_count(self):
        return self.urls_list_items.count()

    @allure.step("Start  get urls black list count(label) on sender urls blacklist")
    def get_label_list_item_number(self):
        return self.black_list_urls_number_label.nth(1).inner_html()

    @allure.step("Start  clicking search urls list  on urls blacklist!")
    def search_list(self, url_to_search):
        self.search_url_input.fill(url_to_search)
        self.search_url_operation.click()
        Reporting.report_allure_and_logger("INFO", "finished clicking search button of urls blacklist!")

    # TODO: FIX(get id?)
    # @allure.step("TO FIX")
    # @allure.step("Start")
    # def click_cancel_search(self):
    #     self.page.locator("text=Sender Url Address Whitelist1 Address Add Address >> button").nth(1).press("Enter")
    #     Reporting.report_allure_and_logger("INFO", "finished clicking CANCEL search button of urls blacklist!")

    @allure.step("Start performing cancel search  of sender urls blacklist!")
    def cancel_search(self):
        self.search_url_input.fill("")
        self.page.reload()
        Reporting.report_allure_and_logger("INFO", "After performing cancel search of urls blacklist!")

    @allure.step("Start clicking Edit of BLACKLIST URL(on url list)!  of urls blacklist!")
    def click_edit_list_item(self):
        self.edit_button.click()
        Reporting.report_allure_and_logger("INFO",
                                           "Finish clicking Edit of BLACKLIST URL(on url list)!  of urls blacklist!")

    @allure.step("Start clicking Edit save button of urls blacklist!")
    def click_save_list_item_changes(self):
        self.save_changes_button.click()
        Reporting.report_allure_and_logger("INFO", "After  clicking Edit save button   of urls blacklist!")

    @allure.step("Returning White  list sender(first/Second)")
    def get_list_item(self, params_dictionary, is_first, is_acronis):
        if is_first:
            if is_acronis:
                return params_dictionary.get("ACRONIS_URL_BLACK_LIST1")
            else:
                return params_dictionary.get("XRAY_URL_BLACK_LIST1")
        else:
            if is_acronis:
                return params_dictionary.get("ACRONIS_URL_BLACK_LIST2")
            else:
                return params_dictionary.get("XRAY_URL_BLACK_LIST2")
