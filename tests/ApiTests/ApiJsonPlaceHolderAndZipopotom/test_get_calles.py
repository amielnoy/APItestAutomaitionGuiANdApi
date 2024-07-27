import requests as requests

from ApiTests.base_api_test import BaseApiTest


class TestZippopotam(BaseApiTest):
    def test_get_locations_for_us_90210_check_status_code_equals_200(BaseApiTest):
        suffix = "us/90210"
        url = BaseApiTest.base_url_zippopotam + suffix

        response = requests.get(url)

        assert response.status_code == 200, "we expected 200 but actually got:" + response.status_code
        assert response.headers[
                   "Content-Type"] == "application/json", "we expected application/json but actually got:" + \
                                                          response.headers["Content-Type"]

        response_dectionary = BaseApiTest.get_response_dictionary(response)

        assert response_dectionary['post code'] == '90210', "the get code was not 90210 but instead" + \
                                                            response_dectionary['post code']
        assert response_dectionary[
                   'country'] == 'United States', "the get country was not 'United States' but instead" + \
                                                  response_dectionary['country']
        assert response_dectionary['country abbreviation'] == 'US'

        places_list_element = response_dectionary['places'][0]
        assert places_list_element['latitude'] == '34.0901', "we expected to get 34.0901 but actualy got:" + \
                                                             places_list_element['latitude']
        assert places_list_element['longitude'] == '-118.4065'
        assert places_list_element['place name'] == 'Beverly Hills'
        assert places_list_element['state'] == 'California'
        assert places_list_element['state abbreviation'] == 'CA'
        print('Test of ' + url + "endged succesfuly")

    def test_auth_token(self):
        zenhub_token = 'zh_1956a72a679d9790df29ebb629aaa108f490cfd7f8c6d608a4b92ee18ff36ec9'
        headers = {'X-Authentication-Token': 'Bearer ' + zenhub_token}

        base_url = 'https:/api.zenhub.com'
        full_url = base_url + '/p2/repositories/129749216/workspaces'
        response = requests.get(url=full_url, headers=headers)
        assert response.status_code, 200
