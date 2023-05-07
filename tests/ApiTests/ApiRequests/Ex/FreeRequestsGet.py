import json
import os
from pathlib import Path
import pytest
import requests
from dotenv import load_dotenv
from faker import Faker
from TestBuildingBlocks.SetupTearDownOperations.setup_teardown_api_operations import SetupTearDownApiOperations
from Utils.HttpRequests.base_http_requests import BaseHttpRequests
from Utils.HttpRequests.http_requests_acronis import AcronisHttpRequests

load_dotenv(dotenv_path=r"D:\automaition_projects\annotations_trainval2017\PlayWright2023\enviornment\.env_ariel")


def shorten(str):
    if len(str) > 10:
        return str[:10]
    return str
def create_fakedata():
    fake = Faker()
    values = []
    values.append(fake.name())
    values.append(fake.last_name())
    values.append(fake.date_of_birth().strftime('%Y-%m-%d'))
    values.append(fake.email())
    values.append(fake.phone_number())
    values.append(fake.address())
    values.append(fake.address())
    values.append(fake.city())
    values.append(fake.state())
    values.append(fake.postcode())
    values.append(fake.country())
    short_values = [shorten(value) for value in values]
    return short_values

def setUpfakedata():
    all_data = []
    keys = ['firstName','lastName','birthdate','email','phone','street1','street2',
            'city','stateProvince','postalCode','country']
    for i in range(30):
        values = create_fakedata()
        my_list_of_tupels = list(zip(keys,values))
        fake_data_dict = dict(my_list_of_tupels)
        all_data.append(fake_data_dict)

    return all_data

def add_contact_data_for_test():
    data = setUpfakedata()
    test_data = [(data_dict, '201') for data_dict in data]
    return test_data


class TestsRequests:
    # Test Case in TestTrail direct link
    # TODO Bug
    # after setting url and retriving smtp server
    # After pressing next we stay on same web page!!!!
    # USER1: test2@gmailbox.akjnhhk.xyz  :    MmnGy&$N2vBBsmgH7^6JNVJu

    token = None

    @pytest.fixture(autouse=True)
    @staticmethod
    def setUptoken() -> None:
        if TestsRequests.token == None:
            # b4 each test
            url = "https://thinking-tester-contact-list.herokuapp.com/users/login"
            payload = json.dumps({
                "email": "ariel.tsesarsky@gmail.com",
                # "password": "L6caQEBgrku6JQ3",
                "password": os.environ['password']
            })
            response = BaseHttpRequests.http_post_request(url, json_body=payload)
            TestsRequests.token = response.json()['token']






    def test_requests_get(self, read_non_secrets):
        parameters_dectionary=read_non_secrets

        setup_tear_down_api_operations = SetupTearDownApiOperations(parameters_dectionary ,is_acronis=True)
        organization_details_responce = setup_tear_down_api_operations.get_organization_details(is_acronis=True)
        assert organization_details_responce['id'] == 9042
        assert organization_details_responce['name'] == 'amiel.acronis'
        assert organization_details_responce['support_email'] == 'amiel.peled+acronis@perception-pont.io'

        #negative test
        assert organization_details_responce['city'] == None,"ERROR I have a value!"
        assert organization_details_responce['address1'] == "", "ERROR I have a value!"


    def  test_free_get(self):
        base_url = 'https://api.testing.perception-point.io/'

        # response = requests.get(
        #     base_url + 'api/organizations/' + organization_id
        #     , headers={'Authorization': 'token ' + token_value})
        base_url='https://jsonplaceholder.typicode.com'
        url_suffix = '/users'

        response = AcronisHttpRequests.http_get_request(base_url, url_suffix)
        assert response
        assert response[0]['id'] == 1
        #assert response['00']['id'] == 1
        assert response[1]['email'] == 'Shanna@melissa.tv'
        #assert response[name] == 1
        assert response[2]['id'] == 3
        # assert response['00']['id'] == 1
        assert response[9]['email'] == 'Rey.Padberg@karina.biz'
        # assert response[name] == 1

        for i in range(len(response)):
            assert response[i]['id'] == i+1 ,f"the id of response[{i}]['id'] is invalid.does not equal {i+1}"

    @pytest.mark.parametrize('pokemon_name,response_code', [
        # each element of this list will provide values for the
        # topics "value_A" and "value_B" of the test and will
        # generate a stand-alone test case.
        ('alakazam', 200),
        ('squirtle', 200),
        ('charmamnder',404),
        ('kabuki',404)
    ])
    def test_pokeapi(self,pokemon_name,response_code):
        url = 'https://pokeapi.co/'
        suffix = 'api/v2/pokemon/'+ pokemon_name
        response = BaseHttpRequests.http_get_request(full_url=url+suffix)
        assert response.status_code == response_code , f"problem with page returns {response.status_code}"


    @pytest.mark.parametrize("new_contact_data,expected_status_code",add_contact_data_for_test())
    def test_add_contact(self,new_contact_data,expected_status_code):
        url = 'https://thinking-tester-contact-list.herokuapp.com/contacts'
        my_token = self.token
        payload = json.dumps(new_contact_data)
        response = BaseHttpRequests.http_post_request(full_url=url,json_body=payload,token=my_token)
        # print(response.status_code)
        # print(response.text)
        assert response.status_code == expected_status_code

    def test_add_contact_negative(self):
        url = 'https://thinking-tester-contact-list.herokuapp.com/contacts'
        my_token = self.token
        new_contact_data = {'lastName':'Moshiko'}
        payload = json.dumps(new_contact_data)
        response = BaseHttpRequests.http_post_request(full_url=url,json_body=payload,token=my_token)
        assert response.status_code == 400


    def test_update_contact(self):
        contact_list_url = 'https://thinking-tester-contact-list.herokuapp.com/contacts'
        my_token = self.token
        update_contact_data = {"firstName": "Moshiko","lastName": "Mosh","birthdate": "1984-06-30","email": "fake@foo.com",
        "phone": "8005551001","street1": "2 Elm St.","street2": "Unit 2","city": "Springfield","stateProvince": "ON",
        "postalCode": "L8R1P8","country": "Canada"}
        payload = json.dumps(update_contact_data)
        page = BaseHttpRequests.http_get_request(full_url=contact_list_url,token_value=my_token)
        contacts_str = page.content.decode('utf-8')
        contacts_array = json.loads(contacts_str)
        id_1 = contacts_array[0]['_id']
        contact_url = contact_list_url + '/' + str(id_1)
        page = BaseHttpRequests.http_put_request(contact_url, json_body=payload,token_value=my_token)
        assert page.status_code == 200
        print(0)

    def test_delete_contact(self):
        contact_list_url = 'https://thinking-tester-contact-list.herokuapp.com/contacts'
        my_token = self.token
        page = BaseHttpRequests.http_get_request(full_url=contact_list_url,token_value=my_token)
        contacts_array = page.content.decode('utf-8')
        contacts_array = json.loads(contacts_array)
        assert contacts_array
        id_1 = contacts_array[0]['_id']
        contact_url = contact_list_url + '/' + str(id_1)
        page = BaseHttpRequests.http_delete_request(contact_url,my_token)
        assert 200 <= page.status_code < 300
        print(page.content)

    def test_2(self):
        url = 'https://thinking-tester-contact-list.herokuapp.com/users'
        data = {
            "firstName": "Mishel",
            "lastName": "Tsesarsky",
            "email": "thefutureishere1@fake.com",
            "password": "1234567",
        }

        page = requests.post(url,json=data)
        #page = requests.post(url, data=json.dumps(data))
        print(page)


    # to do another 5 test like this positive and negative , and format an assertion error
    # evreyone with the same link for loops , find another free link requests free link
    # seek all of the questions in chat GPT with another url freestyle 