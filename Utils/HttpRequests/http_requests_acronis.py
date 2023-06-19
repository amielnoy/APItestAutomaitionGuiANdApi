import os

import requests

from Utils.HttpRequests.base_http_requests import BaseHttpRequests
from test_base import BaseTest


class AcronisHttpRequests(BaseHttpRequests):
    params_dictionary = BaseTest.get_non_secrets_and_secrets(BaseHttpRequests.non_secrets_file_name,
                                                 BaseHttpRequests.secrets_file_name)
    base_url = params_dictionary.get('ACRONIS_BASE_URL')

    organization_id = params_dictionary.get('ACRONIS_ORGANIZATION_ID1')
    token_value = os.getenv('ACRONIS_USER_TOKEN1')

    @staticmethod
    def http_delete_request(base_url, domain_suffix=''):
        response = requests.delete(base_url + domain_suffix  # + '/'
                                   , headers=BaseHttpRequests.get_headers(AcronisHttpRequests.token_value))
        # print(response.json())
        return response.json()

    @staticmethod
    def http_get_request(base_url, url_suffix=''):
        response = requests.get(
            url=base_url + url_suffix
            , headers=AcronisHttpRequests.get_headers(AcronisHttpRequests.token_value))
        # headers = {'Authorization': 'token ' + AcronisHttpRequests.token_value}

        # print('organization_domains=')
        # print(response.json())
        return response.json()

    @staticmethod
    def http_get_request_without_headers(base_url, url_suffix=''):
        response = requests.get(
            url=base_url + url_suffix)
        # headers = {'Authorization': 'token ' + AcronisHttpRequests.token_value}

        # print('organization_domains=')
        # print(response.json())
        return response.json()

    @staticmethod
    def http_get_request_without_token(base_url, url_suffix=''):
        response = requests.get(
            url=base_url + url_suffix
            )
        # headers = {'Authorization': 'token ' + AcronisHttpRequests.token_value}

        # print('organization_domains=')
        # print(response.json())
        return response.json()

    @staticmethod
    def http_post_request_pp(base_url):
        response = requests.get(
            base_url + '/api/v1/users/organization-domains/?organization_id='
            + AcronisHttpRequests.organization_id
            , headers={'Authorization': 'token '
                                        + AcronisHttpRequests.token_value})
        # print('organization_domains=')
        # print(response.json())
        return response.json()

    @staticmethod
    def http_post_request(base_url, suffix, json_body):
        response = requests.request(
            "POST"
            , base_url + suffix
            , data=json_body)
        assert response.status_code == 200 or response.status_code == 201
        # print('organization_domains=')
        # print(response.json())
        return response.json()

    @staticmethod
    def http_post_request(base_url, suffix, json_body, headers=''):
        response = requests.request(
            "POST"
            , base_url + suffix
            , data=json_body
            , headers=headers)
        assert response.status_code == 200 or response.status_code == 201
        # print('organization_domains=')
        # print(response.json())
        return response.json()

    @staticmethod
    def http_post_request_with_params(base_url, suffix, params, headers=''):
        response = requests.request(
            "POST"
            , base_url + suffix
            , params=params
            , headers=headers)
        assert response.status_code == 200 or response.status_code == 201
        # print('organization_domains=')
        # print(response.json())
        return response.json()




