import os

from pages.EmailWizard.new_mail_service_wizard_page import NewMailServiceWizardPage
from TestBuildingBlocks.SetupTearDownOperations.setup_teardown_api_operations import SetupTearDownApiOperations
from Utils.Assertions.mail_wizard_assertions import acronis_assertions
from pages.EmailWizard.new_service_add_domain_page import NewServiceWizardAddDomain
from pages.EmailWizard.verify_domain_page import verify_domain
from pages.EmailWizard.view_status_page import view_status
from pages.xray_main_page import xrayInsightsMainPage


class TestBaseNewMailService:
    GMAIL_SERVICE_SUITE = 'G-Suite'

    def __init__(self, params_dictionary, is_acronis, is_accounts, service_type, user_licenses_per_domain):
        self.is_accounts = is_accounts
        self.my_add_domain_page = None
        self.is_acronis = is_acronis
        self.params_dictionary = params_dictionary
        self.user_licenses_per_domain = user_licenses_per_domain

    def test_new_mail_service_goto_menu_wizard_page(self, page):
        xray_main_page = xrayInsightsMainPage(page)
        xray_main_page.click_email_wizard()
        my_email_wizard = NewMailServiceWizardPage(page, self.is_acronis)
        # verify email wizard page apearedXRAY
        if self.is_acronis:
            new_service_top_text = self.params_dictionary.get("XRAY_CONFIGURE_SERVICES")
        else:
            new_service_top_text = self.params_dictionary.get("ACRONIS_CONFIGURE_SERVICES")
        assert my_email_wizard.get_connect_new_service_label_text() == new_service_top_text

    def assert_new_mail_service_add_domain(self, page, params_dictionary):
        self.my_add_domain_page = NewServiceWizardAddDomain(page)
        # verify we got to set_scanned_mail page
        assert self.my_add_domain_page.get_add_domain_label_text() == "Domains"

    def test_new_mail_service_add_domain(self, page, params_dictionary):
        self.my_add_domain_page.set_host(self.domain_to_add)
        self.my_add_domain_page.click_find_domain_smtp_server()
        if self.is_acronis:
            assert self.my_add_domain_page.set_user_licenses_per_domain(
                self.user_licenses_per_domain) == self.user_licenses_per_domain, "User licenses seats are<>" \
                                                                                 + str(self.user_licenses_per_domain)
        self.my_add_domain_page.click_next_button()

    def test_new_mail_service_add_text_records(self, page):
        my_verrify_added_domain = verify_domain(page)
        assert my_verrify_added_domain.get_add_text_records_text() == "Add TXT Records"
        my_verrify_added_domain.click_next_button()

    def test_new_mail_service_view_status(self, page):
        my_view_status = view_status(page)
        assert my_view_status.get_allmost_done_text() == "Almost Done!"
        my_view_status.click_view_status_button()
        my_view_status.verify_url(self.base_url + 'settings/domains/')

    def assert_and_report_assertions_of_license_seats(self, organization_details_before):
        acronis_assertions.assert_and_report_assertions_of_license_seats(organization_details_before
                                                                         , self.user_licenses_per_domain
                                                                         , self.acronis_organization_id
                                                                         , self.acronis_token_value)

    def reset_billing_method_and_verify_reset(self, set_billing_method):

        SetupTearDownApiOperations.reset_billing_method(self.acronis_organization_id
                                                        , self.acronis_token_value
                                                        , set_billing_method)
        jsonBillingStatus = SetupTearDownApiOperations.get_billing_status(self.acronis_organization_id,
                                                                          self.acronis_token_value)
        if set_billing_method:
            assert jsonBillingStatus["force_use_seats_amount_for_billing"]
        else:
            assert not jsonBillingStatus["force_use_seats_amount_for_billing"]
