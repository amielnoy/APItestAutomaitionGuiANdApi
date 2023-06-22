class BaseApiTest:
    base_url_json_placeholder = "https://jsonplaceholder.typicode.com/"
    base_url_zippopotam = "http://api.zippopotam.us/"

    @staticmethod
    def get_response_dictionary(response):
        return response.json()
