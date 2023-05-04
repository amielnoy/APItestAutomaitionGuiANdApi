import os

from pages.EmailWizard.CompleteIntegration.complete_office365_configuration_page import \
    CompleteOffice365ConfigurationPage
from pages.Settings.SettingsMainPage import SettingsMainPage
from pages.EmailWizard.CompleteIntegration.complete_gmail_configuration_page import CompleteGmailConfigurationPage
from pages.Settings.Colaboration.email_application_integrations_page import EmailApplicationIntegrationsPage
from TestBuildingBlocks.SetupTearDownOperations.setup_teardown_api_operations import SetupTearDownApiOperations
from Utils.Assertions.mail_wizard_assertions import acronis_assertions
from pages.EmailWizard.new_mail_service_wizard_page import NewMailServiceWizardPage
from pages.EmailWizard.new_service_add_domain_page import NewServiceWizardAddDomain
from pages.EmailWizard.verify_domain_page import verify_domain
from pages.EmailWizard.view_status_page import view_status
from pages.xray_main_page import xrayInsightsMainPage


class TestNewMailService:
    def __init__(self, params_dictionary, is_acronis, is_accounts, service_type):
        self.user_licenses_per_domain = '10'
        self.is_acronis = is_acronis
        self.is_accounts = is_accounts
        self.params_dictionary = params_dictionary

        if is_acronis:
            self.acronis_organization_id = params_dictionary.get("ACRONIS_ORGANIZATION_ID1")
            self.base_url = params_dictionary.get("ACRONIS_BASE_URL")
            self.acronis_token_value = os.getenv("ACRONIS_USER_TOKEN1")
        else:
            self.xray_organization_id = params_dictionary.get("XRAY_ORGANIZATION_ID")
            self.base_url = params_dictionary.get("XRAY_BASE_URL")
            self.xray_token_value = os.getenv("XRAY_USER_TOKEN1")

        self.service_type = service_type

    def test_new_mail_service_wizard_page(self, page, params_dictionary):
        xray_main_page = xrayInsightsMainPage(page)
        xray_main_page.click_email_wizard()
        my_email_wizard_page = NewMailServiceWizardPage(page, self.is_acronis)
        # verify email wizard page appeared XRAY/ACRONIS
        if self.is_acronis:
            new_service_top_text = params_dictionary.get("ACRONIS_CONFIGURE_SERVICES")
        else:
            new_service_top_text = params_dictionary.get("XRAY_CONFIGURE_SERVICES")
        assert my_email_wizard_page.get_connect_new_service_label_text() == new_service_top_text

        # my_email_wizard.set_organisation("amiel.noyfeld")
        # page.pause()
        if self.service_type == "Gmail":
            my_email_wizard_page.click_gmail_service()
            my_email_wizard_page.click_next_button_enable("G-Suite")
        else:
            my_email_wizard_page.click_office365_service()
            my_email_wizard_page.click_next_button()

    def test_new_mail_service_add_domain(self, page, params_dictionary):
        my_add_domain_page = NewServiceWizardAddDomain(page)
        # verify we got to set_scanned_mail page
        assert my_add_domain_page.get_add_domain_label_text() == "Domains"
        if self.service_type == "Gmail":
            if self.is_accounts:
                domain_to_add = params_dictionary.get("ACRONIS_DOMAIN_GMAIL2")
                my_add_domain_page.click_accounts()
            else:
                if self.is_acronis:
                    domain_to_add = params_dictionary.get("XRAY_DOMAIN_GMAIL")
                else:
                    domain_to_add = params_dictionary.get("ACRONIS_DOMAIN_GMAIL1")
        # Office 365
        else:
            if self.is_accounts:
                domain_to_add = params_dictionary.get("ACRONIS_DOMAIN_OFFICE365_1")
                my_add_domain_page.click_accounts()
            else:
                if self.is_acronis:
                    domain_to_add = params_dictionary.get("ACRONIS_DOMAIN_OFFICE365_1")
                else:
                    domain_to_add = params_dictionary.get("XRAY_DOMAIN_OFFICE365")
        my_add_domain_page.set_host(domain_to_add)
        my_add_domain_page.click_find_domain_smtp_server()
        if self.is_acronis:
            assert my_add_domain_page.set_user_licenses_per_domain(
                self.user_licenses_per_domain) == self.user_licenses_per_domain, "User licenses seats are<>" \
                                                                                 + str(self.user_licenses_per_domain)

        my_add_domain_page.click_next_button()

    def test_complete_gmail_configuration_page(self, page, params_dictionary):
        my_complete_gmail_configuration_page = CompleteGmailConfigurationPage(page)
        # verify we got to set_scanned_mail page
        if self.is_acronis:
            text_to_verify = params_dictionary.get("ACRONIS_COMPLETE_GMAIL_CONFIGURATION")
        else:
            text_to_verify = params_dictionary.get("XRAY_COMPLETE_GMAIL_CONFIGURATION")
        assert my_complete_gmail_configuration_page.get_complete_gmail_configuration_label_text() == text_to_verify

        mail_to_set = params_dictionary.get("ACRONIS_GMAIL_CONFIGURATION_MAIL")
        my_complete_gmail_configuration_page.set_gmail_configuration_mail(mail_to_set)
        my_complete_gmail_configuration_page.click_next_button()#click_next_button_enable("G-Suite")

    def test_complete_office_configuration_page(self, page, params_dictionary):
        my_complete_office365_configuration_page = CompleteOffice365ConfigurationPage(page)
        # verify we got to set_scanned_mail page
        # if self.is_acronis:
        #     text_to_verify = params_dictionary.get("ACRONIS_COMPLETE_OFFICE365_CONFIGURATION")
        # else:
        #     text_to_verify = params_dictionary.get("XRAY_COMPLETE_OFFICE365_CONFIGURATION")
        # assert my_complete_office365_configuration_page.get_complete_gmail_configuration_label_text() == text_to_verify

        mail_to_set = params_dictionary.get("ACRONIS_OFFICE365_CONFIGURATION_MAIL")
        password_to_set = params_dictionary.get("ACRONIS_OFFICE365_CONFIGURATION_PASSWORD")
        my_complete_office365_configuration_page.set_office365_configuration_mail(mail_to_set)
        my_complete_office365_configuration_page.click_next_button()
        my_complete_office365_configuration_page.set_office365_configuration_password(password_to_set)
        my_complete_office365_configuration_page.click_sign_in_button()
        my_complete_office365_configuration_page.click_next_button_enable("G-Suite")

    def test_new_mail_service_add_text_records(self, page):
        my_verrify_added_domain = verify_domain(page)
        assert my_verrify_added_domain.get_add_text_records_text() == "Add TXT Records"
        my_verrify_added_domain.click_next_button()

    def test_new_mail_service_view_status(self, page):
        my_view_status = view_status(page)
        assert my_view_status.get_allmost_done_text() == "Almost Done!"
        my_view_status.click_view_status_button()
        my_view_status.verify_url(self.base_url + 'settings/domains/')

    def goto_settings_channels_and_disable_channel(self, page, is_disable_gmail_channel):
        setting_main_page = SettingsMainPage(page)
        collaboration_email_application_integreation_page = EmailApplicationIntegrationsPage(page)
        setting_main_page.click_channels()
        collaboration_email_application_integreation_page.click_disable_channel(is_gmail=is_disable_gmail_channel)

    def assert_and_report_assertions_of_license_seats(self, organization_details_before):
        acronis_assertions.assert_and_report_assertions_of_license_seats(organization_details_before
                                                                         , self.user_licenses_per_domain
                                                                         , self.acronis_organization_id
                                                                         , self.acronis_token_value
                                                                         , params_dictionary=self.params_dictionary)

    def reset_billing_method_and_verify_reset(self, set_billing_method):
        setup_tear_down_api_operation = SetupTearDownApiOperations(params_dictionary=self.params_dictionary
                                                                   , is_acronis=self.is_acronis)
        setup_tear_down_api_operation.reset_billing_method(self.acronis_organization_id
                                                           , self.acronis_token_value
                                                           , set_billing_method)
        jsonBillingStatus = setup_tear_down_api_operation.get_billing_status(self.acronis_organization_id,
                                                                             self.acronis_token_value)
        if set_billing_method:
            assert jsonBillingStatus["force_use_seats_amount_for_billing"]
        else:
            assert not jsonBillingStatus["force_use_seats_amount_for_billing"]
