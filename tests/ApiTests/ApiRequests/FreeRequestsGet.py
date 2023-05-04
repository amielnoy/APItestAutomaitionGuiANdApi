from SetupTearDownOperations.setup_teardown_api_operations import SetupTearDownApiOperations
from Utils.HttpRequests.http_requests_acronis import AcronisHttpRequests


class TestsRequests:
    # Test Case in TestTrail direct link
    # TODO Bug
    # after setting url and retriving smtp server
    # After pressing next we stay on same web page!!!!
    # USER1: test2@gmailbox.akjnhhk.xyz  :    MmnGy&$N2vBBsmgH7^6JNVJu
    def test_requests_get(self, read_non_secrets):
        parameters_dectionary=read_non_secrets

        setup_tear_down_api_operations = SetupTearDownApiOperations(parameters_dectionary ,is_acronis=True)
        organization_details_responce = setup_tear_down_api_operations.get_organization_details(is_acronis=True)
        assert organization_details_responce['id'] == 9042
        assert organization_details_responce['name'] == 'amiel.acronis'
        assert organization_details_responce['support_email'] == 'amiel.peled+acronis@perception-pont.io'

        #negative test
        assert organization_details_responce['city'] == None,"ERROR I have a value!"
        assert organization_details_responce['address1'] == "", "ERROR I have a value!"


    def  test_free_get(self):
        base_url = 'https://api.testing.perception-point.io/'

        # response = requests.get(
        #     base_url + 'api/organizations/' + organization_id
        #     , headers={'Authorization': 'token ' + token_value})
        base_url='https://jsonplaceholder.typicode.com'
        url_suffix = '/users'

        response = AcronisHttpRequests.http_get_request(base_url, url_suffix)
        assert response
        assert response[0]['id'] == 1
        #assert response['00']['id'] == 1
        assert response[1]['email'] == 'Shanna@melissa.tv'
        #assert response[name] == 1