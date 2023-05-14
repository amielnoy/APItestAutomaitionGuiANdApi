import json
import os
from pathlib import Path

import allure
import pytest
import requests
from dotenv import load_dotenv
from faker import Faker
from TestBuildingBlocks.SetupTearDownOperations.setup_teardown_api_operations import SetupTearDownApiOperations
from Utils.DataDrriven.DataDrriven import read_test_data_from_csv_to_dictionary
from Utils.HttpRequests.base_http_requests import BaseHttpRequests
from Utils.HttpRequests.http_requests_acronis import AcronisHttpRequests
from Utils.Enviornment.enviornment_files_ops import get_envvars
import csv
from Utils.Reporting.Reporting import Reporting
import sys


load_dotenv(dotenv_path=r"D:\automaition_projects\annotations_trainval2017\PlayWright2023\enviornment\.env_ariel")
def generate_dict_from_list(list):
    # assuming that odd indexes have keys
    # and even indexes have values
    keys = list[0::2]
    values = list[1::2]
    tupels = zip(keys,values)
    return dict(tupels)
def go_back_to_root(root_dir_name):
    my_file_dir = os.path.dirname(os.path.abspath(__file__))
    dir_name = my_file_dir.split('\\')[-1]
    while dir_name != root_dir_name and dir_name != '':
        my_file_dir = os.path.dirname(my_file_dir)
        dir_name = my_file_dir.split('\\')[-1]

    if dir_name == root_dir_name:
        return my_file_dir
    raise Exception(f'cannot find root {dir_name} in path of file')

def read_my_env(root_dir):
    # we go 3 times up
    project_root_path = go_back_to_root(root_dir)
    env_non_secrets_file = project_root_path.as_posix() + '/enviornment/.non_secrets_env'
    env_secrets_file = project_root_path.as_posix() + '/enviornment/.env'
    # dotenv_path = Path('path/to/.env')
    load_dotenv(dotenv_path=env_secrets_file)
    env_non_secrets_dictionary = get_envvars(env_non_secrets_file)
    yield env_non_secrets_dictionary


def fake_max_length(fake_func,max_str_len):
    # takes a faker function fake_func wich generates a fake string
    # retries until it manages to get a string with a smaller length than max
    # length
    fake_value = fake_func()
    while len(fake_value) >= max_str_len:
        fake_value = str(fake_func())
    return fake_value

def create_fakedata():
    fake = Faker()
    values = []
    values.append(fake.name())
    values.append(fake.last_name())
    values.append(fake.date_of_birth().strftime('%Y-%m-%d'))
    values.append(fake.email())
    values.append(fake_max_length(fake.phone_number,15))
    values.append(fake_max_length(fake.address,40))
    values.append(fake_max_length(fake.address,40))
    values.append(fake.city())
    values.append(fake.state())
    values.append(fake.postcode())
    values.append(fake.country())
    values.append(201)
    return values

def setUpfakedata(number_of_fakes):
    all_data = []
    keys = ['firstName','lastName','birthdate','email','phone','street1','street2',
            'city','stateProvince','postalCode','country','expected_status']

    for i in range(number_of_fakes):
        values = create_fakedata()
        my_list_of_tupels = list(zip(keys,values))
        fake_data_dict = dict(my_list_of_tupels)
        all_data.append(fake_data_dict)

    my_file_dir = os.path.dirname(os.path.abspath(__file__))
    my_csv_path = os.path.join(my_file_dir,'add_data.csv')

    with open(my_csv_path, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(all_data)


class TestsRequests:
    # Test Case in TestTrail direct link
    # TODO Bug
    # after setting url and retriving smtp server
    # After pressing next we stay on same web page!!!!
    # USER1: test2@gmailbox.akjnhhk.xyz  :    MmnGy&$N2vBBsmgH7^6JNVJu

    token = None
    Fake_data = None
    csv_folder = r'D:\automaition_projects\APItestAutomaition\tests\ApiTests\ApiRequests\Ex'

    @pytest.fixture(autouse=True)
    @staticmethod
    def setUptoken() -> None:
        if TestsRequests.token == None:
            # b4 each test
            url = "https://thinking-tester-contact-list.herokuapp.com/users/login"
            payload = json.dumps({
                "email": "ariel.tsesarsky@gmail.com",
                "password": os.environ['password']
            })
            response = BaseHttpRequests.http_post_request(url, json_body=payload)
            TestsRequests.token = response.json()['token']


    @pytest.fixture(autouse=True)
    @staticmethod
    def setUpFakeData():
        if TestsRequests.Fake_data == None:
            setUpfakedata(3)
            TestsRequests.Fake_data = True


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
        csv_folder = r'D:\automaition_projects\APItestAutomaition\tests\ApiTests\ApiRequests\Ex'
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

    @allure.testcase('link to test case')
    @allure.issue('wrong pokemon name bug')
    @allure.description('use poke api to search for pokemon name')
    @pytest.mark.parametrize('data_dict', read_test_data_from_csv_to_dictionary
        (csv_folder + '\pokemon.csv'))
    def test_pokeapi(self,data_dict):
        Reporting.report_allure_and_logger(
            f'searching for pokemon'+data_dict['Name']+'in poke api\n','INFO')
        url = 'https://pokeapi.co/'
        suffix = 'api/v2/pokemon/'+ data_dict['Name']
        response = BaseHttpRequests.http_get_request(full_url=url+suffix)
        try:
            assert response.status_code == int(data_dict['Expected_status'])
            Reporting.report_allure_and_logger(
                f'pokemon is found :' + data_dict['Name'] + '\n', 'INFO')\

        except:
            print('unexpected result assertion incorrect !!!!!!!!!')
            Reporting.report_allure_and_logger(
                f'unexpected result , web response content :\n' + response.content, 'INFO')


    @allure.testcase('link to test case of add contact')
    @allure.issue('missing field bug or incorrect value in field')
    @allure.description('use hekroapp site to add contacts to existing user')
    @pytest.mark.parametrize("test_dict",
                             read_test_data_from_csv_to_dictionary(csv_folder+'\\add_data.csv'))
    def test_add_contact(self,test_dict):
        list1 = list(test_dict.items())[:11]
        new_contact_data = dict(list1)
        url = 'https://thinking-tester-contact-list.herokuapp.com/contacts'
        my_token = self.token
        payload = json.dumps(new_contact_data)
        response = BaseHttpRequests.http_post_request(full_url=url,json_body=payload,token=my_token)
        # print(response.status_code)
        # print(response.text)
        assert response.status_code == int(test_dict['expected_status'])

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