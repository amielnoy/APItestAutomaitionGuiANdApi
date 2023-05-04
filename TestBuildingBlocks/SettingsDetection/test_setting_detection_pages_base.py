from playwright.sync_api import expect

from TestBuildingBlocks.SetupTearDownOperations.setup_teardown_gui_operations import SetupTearDownGuiOperations
from pages.BasePage import BasePage


class BaseSettingDetectionTestPages(BasePage):
    def __init__(self, page, params_dictionary, is_acronis):

        self.is_acronis = is_acronis
        self.params_dictionary = params_dictionary
        self.setup_tear_down_gui_operations = SetupTearDownGuiOperations(page, params_dictionary, is_acronis)
        self.page = page
        self.my_help_search_results_page = None

        if not self.is_acronis:
            self.base_url = self.params_dictionary.get("XRAY_BASE_URL")
        else:
            self.base_url = self.params_dictionary.get("ACRONIS_BASE_URL")

        super().__init__(self.page, self.base_url)
