# The API endpoint
import requests

from ApiTests.base_api_test import BaseApiTest


class TestJsonPlaceholderTests(BaseApiTest):
    def test_post(self):
        # Define new data to create
        new_data = {
            "userID": 1,
            "id": 1,
            "title": "Making a SPECIAL POST request!",
            "body": "This is the data we created.!"
        }

        # The API endpoint to communicate with
        url_post_suffix = "posts"
        url_post = BaseApiTest.base_url_json_placeholder + url_post_suffix

        # A POST request to the API
        post_response = requests.post(url_post, json=new_data)
        assert post_response.status_code == 200 or post_response.status_code == 201
        # Print the response
        post_response_json = BaseApiTest.get_response_dictionary(post_response)

        assert post_response_json['userID'] == 1
        assert post_response_json['id'] == 101
        assert post_response_json['title'] == "Making a SPECIAL POST request!"
        assert post_response_json['body'] == "This is the data we created.!"
        print(post_response_json)
