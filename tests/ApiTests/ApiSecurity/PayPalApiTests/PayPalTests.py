from Utils.HttpRequests.PayPalApi.PayPalApiHttpRequests import PayPalRequests
from Utils.HttpRequests.base_http_requests import BaseHttpRequests


class TestPayPalSecurityTests:
    def test_user_info(self):
        headers = BaseHttpRequests.get_headers(PayPalRequests.token_value)
        response = PayPalRequests.http_get_request('/v1/identity/oauth2/userinfo', '?schema=paypalv1.1')
        print(response)
