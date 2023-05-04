from Utils.HttpRequests.base_http_requests import BaseHttpRequests


class rapid_api_requests(BaseHttpRequests):
    base_url = 'https://contextualwebsearch-websearch-v1.p.rapidapi.com/api'
    headers = {
	"content-type": "application/octet-stream",
	"X-RapidAPI-Key": "8b1f6b7d28mshf7d2608a9de156bp15e100jsnb82ef8191754",
	"X-RapidAPI-Host": "contextualwebsearch-websearch-v1.p.rapidapi.com"
    }

    @staticmethod
    def image_search_api(params_image):
        suffix = '/Search/ImageSearchAPI'
        response = BaseHttpRequests.http_get_request(full_url=rapid_api_requests.base_url + suffix
                                                     ,params=params_image,
                                                     headers=rapid_api_requests.headers)
        return response
    @staticmethod
    def newsSearch_api(params_newsearch):
        suffix = '/search/NewsSearchAPI'
        response = BaseHttpRequests.http_get_request(full_url=rapid_api_requests.base_url + suffix
                                                     ,params=params_newsearch,
                                                     headers=rapid_api_requests.headers)
        return response

    @staticmethod
    def webSearch_api(web_params):
        suffix = '/Search/WebSearchAPI'
        response = BaseHttpRequests.http_get_request(full_url=rapid_api_requests.base_url + suffix,params=web_params,
                                                     headers=rapid_api_requests.headers)
        return response

    @staticmethod
    def spellcheck_api(spell_params):
        suffix = '/spelling/SpellCheck'
        response = BaseHttpRequests.http_get_request(full_url=rapid_api_requests.base_url + suffix, params=spell_params,
                                                     headers=rapid_api_requests.headers)
        return response
    @staticmethod
    def autocomplete_api( auto_params):
        suffix = '/spelling/AutoComplete'
        response = BaseHttpRequests.http_get_request(full_url=rapid_api_requests.base_url + suffix, params=auto_params,
                                                     headers=rapid_api_requests.headers)
        return response



