import os

from pages.login import login
from pages.BasePage import BasePage
from LogManager import LogManager
from pages.Settings.Preferences.PreferncesPage import preferences_page
from pages.Settings.Preferences.ChannelsPage import channels_page
from pages.Settings.SettingsMainPage import SettingsMainPage
from pages.xray_main_page import xrayInsightsMainPage


class SetupTearDownGuiOperations(BasePage):
    logger = LogManager().get_logger_instance()

    token_value = os.getenv('XRAY_USER_TOKEN1')

    def __init__(self, page, params_dictionary, is_acronis):
        self.page = page
        self.is_acronis = is_acronis

        if is_acronis:
            self.organization_id = params_dictionary.get('ACRONIS_ORGANIZATION_ID1')
            self.token_value = os.getenv('ACRONIS_USER_TOKEN1')
            self.base_url = params_dictionary.get("ACRONIS_BASE_URL")
            self.username = os.getenv("ACRONIS_USERNAME1")
            self.password = os.getenv("ACRONIS_PASSWORD1")
        else:
            self.organization_id = params_dictionary.get('XRAY_ORGANIZATION_ID')
            self.token_value = os.getenv('XRAY_USER_TOKEN1')
            self.base_url = params_dictionary.get("XRAY_BASE_URL")
            self.username = os.getenv("XRAY_USERNAME2")
            self.password = os.getenv("XRAY_PASSWORD2")
        super().__init__(self.page, "")

    def login(self, page):

        login_page = login(page, self.base_url)
        login_page.load()
        # When the user logs in with user+password
        login_page.login(self.username, self.password)
        xray_main_page = xrayInsightsMainPage(page)
        # verify main page apeared
        self.assert_main_page_reached(xray_main_page, self.base_url, page)

    def assert_main_page_reached(self, xray_main_page, base_url, page):
        assert xray_main_page.get_result_last_day() == 'LAST DAY'
        if not self.is_acronis:
            self.verify_page_title(page, "Perception Point X-Ray: Insights Dashboard")
        else:
            self.verify_page_title(page, "Acronis X-RAY: Insights Dashboard")

        self.verify_url(base_url + 'insights')
    @staticmethod
    def set_channel_gui(page, xray_main_page, set_office) -> None:
        xray_main_page.click_setting_menu_item()
        # click Preferences tab
        my_settings = SettingsMainPage(page)
        my_settings.click_preferences()

        my_prefernces = preferences_page(page)
        my_prefernces.click_channels_edit()

        my_channels = channels_page(page)
        if set_office:
            my_channels.check_office()
        else:
            my_channels.check_gmail()
        my_channels.click_save()