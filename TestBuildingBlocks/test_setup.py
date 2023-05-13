import os
import time
from tokenize import String

from SetupTearDownOperations.setup_teardown_api_operations import SetupTearDownApiOperations
from pages.BasePage import BasePage
from pages.login import login
from pages.xray_main_page import xrayInsightsMainPage


class TestSetup(BasePage):
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
        assert xray_main_page.get_result_last_day().inner_text() == 'LAST DAY'
        if not self.is_acronis:
            self.verify_page_title(page, "Perception Point X-Ray: Insights Dashboard")
        else:
            self.verify_page_title(page, "Acronis X-RAY: Insights Dashboard")

        self.verify_url(base_url + 'insights')

    def get_organization_license_seats_number(self) -> String:
        return SetupTearDownApiOperations.get_organization_license_seats_number(self.organization_id, self.token_value,
                                                                        self.is_acronis)

    def delete_domain_by_id_of_domain(self):
        SetupTearDownApiOperations.delete_organization_domain_by_id_of_organization(self.organization_id, self.token_value)
        time.sleep(5)

    def set_channel(self, new_channel_is_office365):
        if new_channel_is_office365:
            SetupTearDownApiOperations.set_channel(new_channel_is_office365=True, organization_id=self.organization_id,
                                           token_value=self.token_value)
        else:
            SetupTearDownApiOperations.set_channel(new_channel_is_office365=False, organization_id=self.organization_id,
                                           token_value=self.token_value)
