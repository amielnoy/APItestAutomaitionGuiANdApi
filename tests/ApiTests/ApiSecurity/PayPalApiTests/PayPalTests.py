from Utils.HttpRequests.PayPalApi.PayPalApiHttpRequests import PayPalRequests


# {{base_url}}/v1/identity/oauth2/userinfo?schema=paypalv1.1

class TestPayPalSecurityTests:
    def test_user_info(self):
        headers = BaseHttpRequests.get_headers(token=token_value)
        response = PayPalRequests.http_get_request('/v1/identity/oauth2/userinfo', '?schema=paypalv1.1')
        print(response)
