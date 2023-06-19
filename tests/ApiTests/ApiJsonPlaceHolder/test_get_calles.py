import requests as requests


def test_get_locations_for_us_90210_check_status_code_equals_200():
    base_url="http://api.zippopotam.us/"
    suffix="us/90210"
    url = base_url+suffix

    response = requests.get(url)

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"

    response_dectionary= response.json()
    assert response_dectionary['post code'] == '90210', "the get code was not 90210 but instead"+response_dectionary['post code']
    assert response_dectionary['country'] == 'United States', "the get country was not 'United States' but instead"+response_dectionary['country']
    assert response_dectionary['country abbreviation'] == 'US'

    places_list_element = response_dectionary['places'][0]
    assert places_list_element['latitude'] == '34.0901'
    assert places_list_element['longitude'] == '-118.4065'
    assert places_list_element['place name'] == 'Beverly Hills'
    assert places_list_element['state'] == 'California'
    assert places_list_element['state abbreviation'] == 'CA'
    print('Test of '+url+"ended succesfuly")