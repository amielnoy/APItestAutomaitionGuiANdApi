
from Utils.HttpRequests.rapid_api_requests import rapid_api_requests
from Utils.Reporting.Reporting import Reporting

import time
class TestRapidApi:


    def testSearchapi(self):
        params = {"q":"taylor swift","pageNumber":"1","pageSize":"10","autoCorrect":"true"}
        response = rapid_api_requests.image_search_api(params_image=params)
        Reporting.report_allure_and_logger("INFO", str(response.json()))
        print(response.json())
        time.sleep(3)

    def testnewSearchapi(self):
        params = {"q":"taylor swift","pageNumber":"1","pageSize":"10","autoCorrect":"true","fromPublishedDate":"null","toPublishedDate":"null"}
        response = rapid_api_requests.newsSearch_api(params_newsearch=params)
        Reporting.report_allure_and_logger("INFO", str(response.json()))
        print(response.json())
        time.sleep(3)

    def testWebsearch(self):
        params =  {"q":"taylor swift","pageNumber":"1","pageSize":"10","autoCorrect":"true"}
        response = rapid_api_requests.webSearch_api(web_params=params)
        json_response =response.json()
        Reporting.report_allure_and_logger("INFO",'_type='+ json_response['_type'])
        Reporting.report_allure_and_logger("INFO", 'totalCount=' + str(json_response['totalCount']))
        Reporting.report_allure_and_logger("INFO",'relatedSearch='+ '\n'.join(json_response['relatedSearch']))
        expected_str =['<b><b>taylor swift</b> video</b>', '<b><b>taylor swift</b> 000</b>', '<b><b>taylor swift</b> homepage</b>',
         '<b><b>taylor swift</b> web</b>', '<b>music <b>taylor swift</b></b>', '<b><b>taylor swift</b> news</b>',
         '<b><b>taylor swift</b> instagram</b>', '<b><b>taylor swift</b> online</b>',
         '<b>watch <b>taylor swift</b></b>', '<b><b>taylor swift</b> scooter braun</b>',
         '<b>new york <b>taylor swift</b></b>', '<b>lyrics <b>taylor swift</b></b>']
        assert json_response['relatedSearch'] == expected_str
        print(response.json())
        time.sleep(3)

    def testSpellcheck(self):
        params = {"text":"I am vry happy"}
        response = rapid_api_requests.spellcheck_api(spell_params=params)
        Reporting.report_allure_and_logger("INFO", str(response.json()))
        print(response.content)
        time.sleep(3)

    def testAuto(self):
        params = {"text":"ram "}
        response = rapid_api_requests.autocomplete_api(auto_params=params)
        Reporting.report_allure_and_logger("INFO", str(response.json()))
        print(response.content)
        time.sleep(3)