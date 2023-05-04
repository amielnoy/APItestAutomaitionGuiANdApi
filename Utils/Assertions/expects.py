from playwright.sync_api import expect


class Expects:
    @staticmethod
    def expect_condition_visible(locator, timeout, error_message):
        expect(locator).to_be_visible(timeout=timeout), error_message

    @staticmethod
    def expect_condition_enabled(locator, timeout, error_message):
        expect(locator).to_be_enabled(timeout=timeout), error_message

    @staticmethod
    def expect_conditions_visible_and_enabled(locator, timeout, error_message_visible, error_message_enabled):
        Expects.expect_condition_visible(locator, timeout, error_message_visible)
        Expects.expect_condition_enabled(locator, timeout, error_message_enabled)
