# # TODO
# # TODO Tests for all sections(admin user)
# # TODO Settings-->Detection
# # TODO  ADD+EDIT+DELETE
#
# # TODO git ignore LogFiles and reports
# # from urllib import request
#
# import allure
#
# from TestBuildingBlocks.SetupTearDownOperations.setup_teardown_api_operations import SetupTearDownApiOperations
# from TestBuildingBlocks.SetupTearDownOperations.setup_teardown_gui_operations import SetupTearDownGuiOperations
# from TestBuildingBlocks.test_new_mail_service import TestNewMailService
# from test_base import BaseTest
#
#
# class TestsEmailWizardXray(BaseTest):
#     # Test Case in TestTrail direct link
#     @allure.testcase('https://perceptionpointtemp.testrail.io/index.php?/cases/view/2343')
#     # issuekipa in JIRA direct link(bugs+todo items)
#     # issue:
#     @allure.issue("https://perception-point.atlassian.net/browse/MS-8798")
#     @allure.description('log to chrome and record video of the test')
#     def _test_xray_email_wizard_gmail(self, setup_browser_page, read_non_secrets, request):
#         page = setup_browser_page
#         params_dictionary = read_non_secrets
#
#         setup_tear_down_gui_operations = SetupTearDownGuiOperations(page, params_dictionary, is_acronis=False)
#         setup_tear_down_api_operations = SetupTearDownApiOperations(params_dictionary, is_acronis=False)
#
#         setup_tear_down_api_operations.delete_current_domain_by_id_of_domain()
#         setup_tear_down_api_operations.set_current_channel(new_channel_is_office365=False)
#         setup_tear_down_gui_operations.login(page)
#
#         test_new_mail_service = TestNewMailService(params_dictionary, is_acronis=False, is_accounts=False,
#                                                    service_type="Gmail")
#         test_new_mail_service.test_new_mail_service_wizard_page(page, params_dictionary)
#         test_new_mail_service.test_complete_gmail_configuration_page(page, params_dictionary)
#         test_new_mail_service.test_new_mail_service_add_domain(page, params_dictionary)
#         test_new_mail_service.test_new_mail_service_add_text_records(page)
#         test_new_mail_service.test_new_mail_service_view_status(page)
#         test_new_mail_service.goto_settings_channels_and_disable_channel(page, is_disable_gmail_channel=True)
#     # Test Case in TestTrail direct link
#     @allure.testcase('https://perceptionpointtemp.testrail.io/index.php?/cases/view/2343')
#     # issue in JIRA direct link(bugs+todo items)
#     # issue:
#     @allure.issue("https://perception-point.atlassian.net/browse/PM-929")
#     @allure.description('log to chrome and record video of the test')
#     def _test_xray_email_wizard_office365(self, setup_browser_page, read_non_secrets):
#         # Given login page is displayed
#         page = setup_browser_page
#         params_dictionary = read_non_secrets
#
#         setup_tear_down_gui_operations = SetupTearDownGuiOperations(page, params_dictionary, is_acronis=False)
#         setup_tear_down_api_operations = SetupTearDownApiOperations(params_dictionary, is_acronis=False)
#         setup_tear_down_api_operations.set_current_channel(new_channel_is_office365=False)
#         setup_tear_down_api_operations.delete_current_domain_by_id_of_domain()
#
#         setup_tear_down_gui_operations.login(page)
#
#         test_new_mail_service = TestNewMailService(params_dictionary, is_acronis=False, is_accounts=False,
#                                                    service_type="Office 365")
#         test_new_mail_service.test_new_mail_service_wizard_page(page, params_dictionary)
#         test_new_mail_service.test_new_mail_service_add_domain(page, params_dictionary)
#         test_new_mail_service.test_new_mail_service_add_text_records(page)
#         test_new_mail_service.test_new_mail_service_view_status(page)
