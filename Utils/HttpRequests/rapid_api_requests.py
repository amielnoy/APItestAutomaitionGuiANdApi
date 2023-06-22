from Utils.HttpRequests.base_http_requests import BaseHttpRequests


class rapid_api_requests(BaseHttpRequests):
    base_url = 'https://contextualwebsearch-websearch-v1.p.rapidapi.com/api'
    headers = {
        "content-type": "application/octet-stream",
        "X-RapidAPI-Key": "8b1f6b7d28mshf7d2608a9de156bp15e100jsnb82ef8191754",
        "X-RapidAPI-Host": "contextualwebsearch-websearch-v1.p.rapidapi.com"
    }


    @staticmethod
    def http_get_rapid_api(url_suffix, params):
        response = BaseHttpRequests.http_get_request(full_url=rapid_api_requests.base_url + url_suffix
                                                     , params=params, headers=rapid_api_requests.headers)
        return response

