import os

import requests

from Utils.HttpRequests.base_http_requests import BaseHttpRequests
from test_base import BaseTest


class XrayHttpRequests(BaseHttpRequests):
    params_dictionary = BaseTest.get_non_secrets_and_secrets(BaseHttpRequests.non_secrets_file_name,
                                                 BaseHttpRequests.secrets_file_name)
    base_url = params_dictionary.get('XRAY_BASE_URL')
    orgnization_id = params_dictionary.get('XRAY_ORGANIZATION_ID')
    token_value = os.getenv('XRAY_USER_TOKEN1')

    @staticmethod
    def http_delete_request(domain_suffix='', base_url=BaseHttpRequests.base_url_testing):
        response = requests.delete(
            XrayHttpRequests.base_url_testing + domain_suffix + '/'
            , headers=BaseHttpRequests.get_headers(XrayHttpRequests.token_value))
        # print(response.json())
        return response.json()

    @staticmethod
    def http_get_request(base_url, url_suffix=''):
        response = requests.get(
            base_url + url_suffix
            , headers={'Authorization': 'token ' + XrayHttpRequests.token_value})
        print('organization_domains=')
        print(response.json())
        return response.json()
