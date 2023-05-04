import time

import allure

from TestBuildingBlocks.SetupTearDownOperations.setup_teardown_api_operations import SetupTearDownApiOperations
from Utils.Assertions.assertions import Assertions
from Utils.Reporting.Reporting import Reporting


class acronis_assertions:

    @staticmethod
    def assert_and_report_assertions_of_license_seats(organization_details_before, user_licenses_per_domain
                                                      , acronis_organization_id, acronis_token_value, params_dictionary):
        setup_tear_down_api_operations = SetupTearDownApiOperations(params_dictionary, is_acronis=True)
        for i in range(5):
            organization_details_after = setup_tear_down_api_operations.get_organization_license_seats_number(
                organization_id=acronis_organization_id,
                token_value=acronis_token_value
                , is_acronis=True)
            if int(organization_details_after) - int(organization_details_before) == int(user_licenses_per_domain):
                Reporting.report_allure_and_logger("INFO ",
                                                   "i=" + str(
                                                       i) + " Organization_after_details - Orgnization_before_details== user_licenses_per_domain")
                assert_license_seats(organization_details_before,
                                     organization_details_after,
                                     user_licenses_per_domain)
                break
            else:
                time.sleep(3)


@allure.step(
    "BEFORE ASSERTION {1}=organization_details_after -{0} = organization_details_before == user_licenses_per_domain={2}")
def assert_license_seats(organization_details_before, organization_details_after,
                         user_licenses_per_domain):
    Reporting.report_allure_and_logger("INFO", "ASSERTING:"
                                       + organization_details_after
                                       + "=organization_details_after "
                                       + organization_details_before
                                       + "=organization_details_before == user_licenses_per_domain="
                                       + user_licenses_per_domain)
    Assertions.assert_value_with_err_message(
        "user_licenses_per_domain after are increased by " + user_licenses_per_domain
        , int(organization_details_after) - int(organization_details_before)
        , int(user_licenses_per_domain)
        , "ERROR, The number of user licenses per seat didn't increase by " + user_licenses_per_domain)
