# The API endpoint
import requests
def test_post():
    # Define new data to create
    new_data = {
        "userID": 1,
        "id": 1,
        "title": "Making a SPECIAL POST request!",
        "body": "This is the data we created.!"
    }

    # The API endpoint to communicate with
    base_url="https://jsonplaceholder.typicode.com/"
    url_post_suffix = "posts"
    url_post = base_url+url_post_suffix

    # A POST request to tthe API
    post_response = requests.post(url_post, json=new_data)
    assert post_response.status_code== 200 or post_response.status_code== 201
    # Print the response
    post_response_json = post_response.json()
    assert post_response_json['userID'] == 1
    assert post_response_json['id'] == 101
    assert post_response_json['title'] == "Making a SPECIAL POST request!"
    assert post_response_json['body'] == "This is the data we created.!"
    print(post_response_json)