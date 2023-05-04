# TODO
# TODO Tests for all sections(admin user)
# TODO Settings-->Detection
# TODO  ADD+EDIT+DELETE

# TODO git ignore LogFiles and reports
# from urllib import request

import allure

from TestBuildingBlocks.EmailWizard.EmailServices.test_office365_mail_service import TestOffice365NewMailService
from TestBuildingBlocks.SetupTearDownOperations.setup_teardown_api_operations import SetupTearDownApiOperations
from TestBuildingBlocks.SetupTearDownOperations.setup_teardown_gui_operations import SetupTearDownGuiOperations
from TestBuildingBlocks.test_new_mail_service import TestNewMailService
from test_base import BaseTest


class TestsEmailWizardAcronis(BaseTest):
    # Test Case in TestTrail direct link
    # TODO Bug
    # after setting url and retriving smtp server
    # After pressing next we stay on same web page!!!!
    @allure.testcase('https://perceptionpointtemp.testrail.io/index.php?/cases/view/2343')
    # issue in JIRA direct link(bugs+todo items)
    # issue:
    @allure.issue("https://perception-point.atlassian.net/browse/MS-8798")
    @allure.description('log to chrome and record video of the test')
    # USER1: test2@gmailbox.akjnhhk.xyz  :    MmnGy&$N2vBBsmgH7^6JNVJu
    def test_email_acronis_wizard_gmail_acronis(self, setup_browser_page, read_non_secrets):
        page = setup_browser_page
        page.pause()
        params_dictionary = read_non_secrets

        setup_tear_down_gui_operations = SetupTearDownGuiOperations(page, params_dictionary=params_dictionary,
                                                                    is_acronis=True)
        setup_tear_down_api_operations = SetupTearDownApiOperations(params_dictionary=params_dictionary,
                                                                    is_acronis=True)
        organization_details_before = setup_tear_down_api_operations.get_current_organization_license_seats_number()
        setup_tear_down_api_operations.delete_current_domain_by_id_of_domain()
        setup_tear_down_api_operations.set_current_channel(new_channel_is_office365=False)
        setup_tear_down_gui_operations.login(page)

        test_new_mail_service = TestNewMailService(params_dictionary, is_acronis=True, is_accounts=False,
                                                   service_type="Gmail")
        test_new_mail_service.test_new_mail_service_wizard_page(page, params_dictionary)
        test_new_mail_service.test_complete_gmail_configuration_page(page, params_dictionary)
        test_new_mail_service.test_new_mail_service_add_domain(page, params_dictionary)
        test_new_mail_service.test_new_mail_service_add_text_records(page)
        test_new_mail_service.test_new_mail_service_view_status(page)
        test_new_mail_service.assert_and_report_assertions_of_license_seats(organization_details_before)
        test_new_mail_service.goto_settings_channels_and_disable_channel(page, is_disable_gmail_channel=True)

    @allure.testcase('https://perceptionpointtemp.testrail.io/index.php?/cases/view/2343')
    # issue in JIRA direct link(bugs+todo items)
    # issue:
    @allure.issue("https://perception-point.atlassian.net/browse/MS-8798")
    @allure.description('log to chrome and record video of the test')
    # USER1: atp@office365.ecknhhk.xyz : Q4@NO^@PLqfZ3meO
    # USER2: OFFICE365 connection mail:test@office365.ecknhhk.xyz : Tot60814
    def test_email_wizard_office365_acronis(self, setup_browser_page, read_non_secrets):
        page = setup_browser_page
        params_dictionary = read_non_secrets

        setup_tear_down_gui_operations = SetupTearDownGuiOperations(page, params_dictionary=params_dictionary,
                                                                    is_acronis=True)
        setup_tear_down_api_operations = SetupTearDownApiOperations(params_dictionary=params_dictionary,
                                                                    is_acronis=True)
        organization_seats_before = setup_tear_down_api_operations.get_current_organization_license_seats_number()
        setup_tear_down_api_operations.delete_current_domain_by_id_of_domain()
        setup_tear_down_api_operations.set_current_channel(new_channel_is_office365=False)
        setup_tear_down_gui_operations.login(page)

        test_new_office365_service = TestOffice365NewMailService(params_dictionary, is_acronis=True, is_accounts=False,
                                                                 service_type="Office 365")
        test_new_office365_service.test_office365_new_mail_service_wizard_start_page(page)
        test_new_office365_service.test_new_mail_service_add_domain(page, params_dictionary)
        test_new_office365_service.test_new_mail_service_add_text_records(page)
        test_new_office365_service.test_new_mail_service_view_status(page)
        test_new_office365_service.assert_and_report_assertions_of_license_seats(organization_seats_before)
