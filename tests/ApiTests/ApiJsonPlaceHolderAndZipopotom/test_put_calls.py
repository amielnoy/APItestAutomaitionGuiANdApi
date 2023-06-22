import requests

from ApiTests.base_api_test import BaseApiTest


class TestJsonPlaceholderPutTests(BaseApiTest):
    def test_put(self):
        # Define new data to create
        new_data = {
            "title": "Updated Title",
            "body": "Updated body content",
            "userId": 1
        }

        # The API endpoint to communicate with
        url_put_suffix = "posts/1"
        url_put = BaseApiTest.base_url_json_placeholder + url_put_suffix

        # A POST request to the API
        put_response = requests.put(url_put, json=new_data)
        assert put_response.status_code == 200 or put_response.status_code == 201
        # Print the response
        put_response_json = BaseApiTest.get_response_dictionary(put_response)

        assert put_response_json['userId'] == 1,"error in userId. expected="+1 + "userId actual="+put_response_json['userId']
        assert put_response_json['id'] == 1,"error in id expected="+1 + " id actual="+put_response_json['id']
        assert put_response_json['title'] == "Updated Title","error in title expected="\
                                                             +"Updated Title" + "  actual title="+put_response_json['title']
        assert put_response_json['body'] == "Updated body content", "error expected body =Updated Body  actual title="+put_response_json['body']
        print(put_response_json)
