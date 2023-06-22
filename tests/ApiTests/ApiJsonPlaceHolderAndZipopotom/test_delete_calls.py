import requests

from ApiTests.base_api_test import BaseApiTest


class TestJsonPlaceholderDeleteTests(BaseApiTest):
    def test_delete(self):
        # Define new data to delete

        # The API endpoint to communicate with
        url_delete_suffix = "posts/1"
        url_delete = BaseApiTest.base_url_json_placeholder + url_delete_suffix

        # A DELETE request to the API
        delete_response = requests.delete(url_delete)
        assert delete_response.status_code == 200 or delete_response.status_code == 201
        # Print the response
        delete_response_json = BaseApiTest.get_response_dictionary(delete_response)

        print(delete_response_json)
