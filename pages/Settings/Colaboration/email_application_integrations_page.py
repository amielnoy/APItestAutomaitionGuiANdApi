import allure

from Utils.Assertions.expects import Expects
from Utils.Reporting.Reporting import Reporting
from pages.BasePage import BasePage


class EmailApplicationIntegrationsPage(BasePage):
    URL = 'https://xray.testing.perception-point.io/settings/collaboration'

    def __init__(self, page):
        self.page = page
        page.pause()
        self.DisableGmail = page.get_by_role("button", name="Disable")
        self.DisableOffice365 = page.locator("text=Disable")
        self.ActivateAfterDisable = page.get_by_role("button", name="Activate")
        super().__init__(self.page, self.URL)

    def click_disable_channel(self, is_gmail):
        allure.step("Started clicking  DISABLE Channel Gamail/Office365 ****is GAMIL=" + str(is_gmail))
        if is_gmail:
            Expects.expect_condition_visible(self.DisableGmail, 30000, "Failed to get to: Settings->collaboration")
            self.DisableGmail.click()
            Expects.expect_condition_visible(self.ActivateAfterDisable, 30000, "Failed to renable Gmail")
        else:
            self.DisableOffice365.click()
            Expects.expect_condition_visible(self.ActivateAfterDisable, 30000, "Failed to renable Office365")

        Reporting.report_allure_and_logger("INFO",
                                           "Finished clicking  DISABLE Channel Gamail/Office365 ****is GAMIL=" + str(
                                               is_gmail))
