
import requests

from Utils.HttpRequests.base_http_requests import BaseHttpRequests


class PayPalRequests(BaseHttpRequests):
    token_value = "A21AAL8A8rAjJjh1e8JcBuom2FEMJeCREs6Be0TY3T3aI610eKpQ93jV0lpJsvHj-YU7-lR2VaPZNLFOvUY6Wi4OCT7yv2BFA"
    base_url = 'https://api-m.sandbox.paypal.com'

    @staticmethod
    def get_headers(token):
        return {'Authorization': 'token ' + token}


    @staticmethod
    def http_get_request(url_suffix='', params=''):
        response = requests.get(
            PayPalRequests.base_url
            + url_suffix + params
            , headers=BaseHttpRequests.get_headers(token=PayPalRequests.token_value))
        print('organization_domains=')
        print(response.json())
        return response.json()
