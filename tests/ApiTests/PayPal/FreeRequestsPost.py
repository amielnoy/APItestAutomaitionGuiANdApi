import json

import requests

from SetupTearDownOperations.setup_teardown_api_operations import SetupTearDownApiOperations


class TestsRequests:
    # Test Case in TestTrail direct link
    # TODO Bug
    # after setting url and retriving smtp server
    # After pressing next we stay on same web page!!!!
    # USER1: test2@gmailbox.akjnhhk.xyz  :    MmnGy&$N2vBBsmgH7^6JNVJu
    def test_pp_requests_get(self, read_non_secrets):
        parameters_dectionary=read_non_secrets

        setup_tear_down_api_operations = SetupTearDownApiOperations(parameters_dectionary,is_acronis=True)
        organization_details_responce = setup_tear_down_api_operations.get_organization_details(is_acronis=True)
        assert organization_details_responce['id'] == 9042
        assert organization_details_responce['name'] == 'amiel.acronis'
        assert organization_details_responce['support_email'] == 'amiel.peled+acronis@perception-pont.io'

        #negative test
        assert organization_details_responce['city'] == None,"ERROR I have a value!"
        assert organization_details_responce['address1'] == "", "ERROR I have a value!"
        # organization_details_before = setup_tear_down_api_operations.get_current_organization_license_seats_number()
        # setup_tear_down_api_operations.delete_current_domain_by_id_of_domain()
        # setup_tear_down_api_operations.set_current_channel(new_channel_is_office365=False)
    def test_paypal_post(self):
        base_url = "https://api-m.sandbox.paypal.com"
        url = base_url + "/v2/checkout/orders"

        payload = json.dumps({
            "intent": "CAPTURE",
            "purchase_units": [
                {
                    "amount": {
                        "currency_code": "USD",
                        "value": "100.00"
                    }
                }
            ]
        })
        prefer_representation_detailes='return=representation'
        headers = {
            'Content-Type': 'application/json',
            'Prefer': prefer_representation_detailes,
            'PayPal-Request-Id': '20fa2104-9fb4-4235-ba9a-9ef87ff72eb8'
        }

        response = requests.post(url, headers=headers, data=payload)

        print(response.text)
