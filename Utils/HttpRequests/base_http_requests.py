import requests


class BaseHttpRequests:
    base_url = ''
    organization_id = ''
    token_value = ''

    base_url_pp = 'https://testing.api-pp.com/'
    base_url_testing = 'https://api.testing.perception-point.io'
    non_secrets_file_name = '.non_secrets_env'
    secrets_file_name = '.env'

    default_params = {'key': 'value'}

    @staticmethod
    def get_headers(token):
        return {'Authorization': 'Bearer ' + token}

    @staticmethod #??? duplicate function
    def http_delete_request(base_url, url_suffix, organization_id=organization_id, token_value=token_value):
        response = requests.delete(
            base_url
            + '/' + url_suffix
            + '/?organization_id=' + organization_id
            , headers={'Authorization': 'token ' + token_value})
        # print(response.json())
        return response.json()

    @staticmethod
    def http_delete_request(base_url, url_suffix, token_value=token_value):
        if token_value != '':
            response = requests.delete(
                base_url
                + '/' + url_suffix
                , headers={'Authorization': 'token ' + token_value})
            # print(response.json())
            return response
        else:
            response = requests.delete(
                base_url
                + '/' + url_suffix
            )
            return response

    @staticmethod # ??? two duplicate functions
    def http_delete_request(base_url, url_suffix, organization_id=organization_id, token_value=token_value):
        if token_value != '':
            response = requests.delete(
                base_url
                + '/' + url_suffix
                + '/?organization_id=' + organization_id
                , headers={'Authorization': 'token ' + token_value})
        else:
            response = requests.delete(
                base_url
                + '/' + url_suffix
            )
        # print(response.json())
        return response.json()

    @staticmethod
    def http_get_request(organization_id=organization_id, url_suffix='', token_value=token_value):
        response = requests.get(
            BaseHttpRequests.base_url_pp + url_suffix
            , headers=BaseHttpRequests.get_headers(token=token_value))
        #print('organization_domains=')
        #print(response.json())
        return response

    @staticmethod
    def http_get_request(url_suffix='', params=default_params, token_value=''):
        response = requests.get(
            BaseHttpRequests.base_url_pp
            + url_suffix
            , headers=BaseHttpRequests.get_headers(token=token_value))
        #print('organization_domains=')
        #print(response.json())
        return response

    @staticmethod
    def http_get_request(full_url='', params=default_params, token_value='',headers=''):
        if headers == '':
            headers = BaseHttpRequests.get_headers(token=token_value)
        response = requests.get(
           full_url,params=params
            , headers=headers)
        #print('organization_domains=')
        #print(response.json())
        return response

    @staticmethod # method without token
    def http_post_request(full_url, json_body,token = ''):
        headers = {
            'Content-Type': 'application/json',
        }
        if token != '':
            headers.update(BaseHttpRequests.get_headers(token))
        response = requests.request("POST", full_url, headers=headers, data=json_body)
        # print('organization_domains=')
        # print(response.json())
        # assert (response.status_code == 200
        #         or response.status_code == 201
        #         or response.status_code == 202
        #         or response.status_code == 203
        #         or response.status_code == 204)
        'ERROR POST REQUEST FAILED with status code=' + str(response.status_code)
        return response

    @staticmethod
    def http_put_request(base_url, url_prefix, json_body='', token_value=''):
        response = requests.get(
            base_url + url_prefix
            , json_body
            , headers=BaseHttpRequests.get_headers(token=token_value))
        # print('organization_domains=')
        # print(response.json())
        return response



    @staticmethod
    def http_put_request(url_prefix, json_body='', token_value=''):
        response = requests.get(
            BaseHttpRequests.base_url + url_prefix
            , json_body
            , headers=BaseHttpRequests.get_headers(token=token_value))
        # assert response.status_code == 200 \
        #     , 'ERROR put request failed status codes=' + response.status_code
        # print(response.json())
        return response

    @staticmethod
    def http_put_request(full_url, json_body='', token_value=''):
        response = requests.put(
            full_url
            , json_body
            , headers=BaseHttpRequests.get_headers(token=token_value))
        # assert response.status_code == 200 \
        #     , 'ERROR put request failed status codes=' + response.status_code
        # print(response.json())
        return response

    @staticmethod
    def http_delete_request(full_url, token_value=''):
        response = requests.delete(
            full_url
            , headers=BaseHttpRequests.get_headers(token=token_value))
        # assert response.status_code == 200 \
        #     , 'ERROR put request failed status codes=' + response.status_code
        # print(response.json())
        return response