from playwright.sync_api import expect

from Utils.Assertions.assertions import Assertions
from Utils.Assertions.expects import Expects
from pages.Help.help_search_results_page import HelpSearchResultsPage
from pages.Help.main_help_page import HelpPage
from pages.xray_main_page import xrayInsightsMainPage


class TestHelpPages:
    def __init__(self, params_dictionary, is_acronis):
        self.is_acronis = is_acronis
        self.params_dictionary = params_dictionary
        self.main_help_page = None
        self.my_help_search_results_page = None

        if not is_acronis:
            self.base_url = self.params_dictionary.get("XRAY_BASE_URL")
        else:
            self.base_url = self.params_dictionary.get("ACRONIS_BASE_URL")

    def test_main_help_page(self, page, is_menu_help):
        if not is_menu_help:
            page.goto(self.base_url)

        xray_main_page = xrayInsightsMainPage(page)

        if is_menu_help:
            new_help_page = xray_main_page.click_documentation_center_menu_item(is_acronis=self.is_acronis)
        else:
            new_help_page = xray_main_page.click_documentation_center_on_bottom_of_main_xray(
                is_acronis=self.is_acronis)

        if self.is_acronis:
            help_page_url = self.params_dictionary.get("ACRONIS_HELP_URL")
        else:
            help_page_url = self.params_dictionary.get("XRAY_HELP_URL")

        main_help_page = HelpPage(new_help_page, help_page_url)
        self.main_help_page = main_help_page
        # assert main_help_page.get_page_url() == help_page_url
        Assertions.assert_value_with_err_message("Help page url", main_help_page.get_page_url(), help_page_url,
                                                 "ERROR!,Url of main help page <> " + help_page_url)

    def assert_expected_two_lines_help_text(self, main_help_page, expected_line1_text, expected_line2_text):
        Assertions.assert_value_with_err_message("expected line1 text",
                                                 main_help_page.get_acronis_main_help_page_line1_text(self.is_acronis)
                                                 , expected_line1_text
                                                 , "text is <> from expected line1 text=" + expected_line1_text)

        Assertions.assert_value_with_err_message("expected line2 text"
                                                 , main_help_page.get_acronis_main_help_page_line2_text()
                                                 , expected_line2_text
                                                 , "text is <> from expected line2 text=" + expected_line2_text)

    def assert_main_help_page(self):
        # validate main help page text
        if not self.is_acronis:
            main_help_page_line1_text = "Welcome to the Perception Point"
            main_help_page_line2_text = "Documentation Center"
        else:
            main_help_page_line1_text = "Welcome to the Advanced Email Security"
            main_help_page_line2_text = "Documentation Center"

        self.assert_expected_two_lines_help_text(self.main_help_page, main_help_page_line1_text,
                                                 main_help_page_line2_text)

    def test_main_help_page_search(self):
        search_string = "Connecting Email Services"
        self.main_help_page.set_keyword_to_search_help(search_string)

        error_message_visible = 'Result heading doesnt\'t appear to be VISIBLE,ERROR!!'
        error_message_enabled = 'Result heading doesnt\'t appear to be ENABLED,ERROR!!'
        Expects.expect_conditions_visible_and_enabled(self.main_help_page.main_middle_search.nth(1)
                                                      , timeout=10000,
                                                      error_message_visible=error_message_visible
                                                      , error_message_enabled=error_message_enabled)
        self.main_help_page.click_search_help_keyword()
        # main_help_page.get_page().wait_for_timeout(10000)
        my_help_search_results_page = HelpSearchResultsPage(self.main_help_page.get_page(), "")
        self.my_help_search_results_page = my_help_search_results_page
        expect(my_help_search_results_page.resultHeading.nth(0)).to_be_visible(timeout=30000)

        error_message = 'Result heading doesnt\'t appear ERROR!'
        Expects.expect_condition_visible(my_help_search_results_page.resultHeading.nth(0)
                                         , timeout=30000,
                                         error_message=error_message)

    def assert_help_search_results(self):
        heading_full_text1 = "Your search for \"Connecting Email Services\" returned "
        heading_full_text2 = " result(s)"

        Assertions.assert_value_in_string("heading text part1"
                                          , heading_full_text1
                                          , self.my_help_search_results_page.resultHeading.first.inner_text())

        Assertions.assert_value_in_string("heading text part2"
                                          , heading_full_text2
                                          , self.my_help_search_results_page.resultHeading.first.inner_text())
