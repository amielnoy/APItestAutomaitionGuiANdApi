import os
import time
from tokenize import String

import allure
import requests
from docutils.utils import Reporter

from Utils.HttpRequests.base_http_requests import BaseHttpRequests
from Utils.HttpRequests.http_requests_acronis import AcronisHttpRequests
from Utils.HttpRequests.http_requests_xray import XrayHttpRequests
from Utils.Reporting.Reporting import Reporting
from LogManager import LogManager


class SetupTearDownApiOperations:
    logger = LogManager().get_logger_instance()

    running_scan_id = 'init_value'

    token_value = os.getenv('XRAY_USER_TOKEN1')

    def __init__(self, params_dictionary, is_acronis):
        self.is_acronis = is_acronis

        if is_acronis:
            self.organization_id = params_dictionary.get('ACRONIS_ORGANIZATION_ID1')
            self.token_value = os.getenv('ACRONIS_USER_TOKEN1')
            self.base_url = params_dictionary.get("ACRONIS_BASE_URL")
            self.username = os.getenv("ACRONIS_USERNAME1")
            self.password = os.getenv("ACRONIS_PASSWORD1")
        else:
            self.organization_id = params_dictionary.get('XRAY_ORGANIZATION_ID')
            self.token_value = os.getenv('XRAY_USER_TOKEN1')
            self.base_url = params_dictionary.get("XRAY_BASE_URL")
            self.username = os.getenv("XRAY_USERNAME2")
            self.password = os.getenv("XRAY_PASSWORD2")

    @staticmethod
    def delete_domain(organization_id, domain_to_delete_id, token_value):
        response = requests.delete(
            'https://api.testing.perception-point.io/api/v1/users/organization-domains/' + domain_to_delete_id
            + '/?organization_id=' + organization_id
            , headers={'Authorization': 'token ' + token_value})
        # print(response.json())

    @staticmethod
    def get_organization_domains(organization_id, token_value, is_acronis):
        # response = requests.get(
        #     'https://testing.api-pp.com/api/v1/users/organization-domains/?organization_id=' + organization_id
        #     , headers={'Authorization': 'token ' + token_value})

        if is_acronis:
            url_suffix = 'api/v1/users/organization-domains/?organization_id=' + organization_id
            response = AcronisHttpRequests.http_get_request(BaseHttpRequests.base_url_pp, url_suffix=url_suffix)
        # xray
        else:
            url_suffix = 'api/v1/users/organization-domains/?organization_id=' + organization_id
            response = XrayHttpRequests.http_get_request(BaseHttpRequests.base_url_pp, url_suffix=url_suffix)
        print('organization_domains=')
        print(response[0])
        return response[0]

    @staticmethod
    def get_organization_details(is_acronis):
        base_url = 'https://api.testing.perception-point.io/'

        # response = requests.get(
        #     base_url + 'api/organizations/' + organization_id
        #     , headers={'Authorization': 'token ' + token_value})
        if is_acronis:
            url_suffix = 'api/organizations/' + AcronisHttpRequests.organization_id
            response = AcronisHttpRequests.http_get_request(base_url, url_suffix)
        else:
            url_suffix = 'api/organizations/' + XrayHttpRequests.organization_id
            response = XrayHttpRequests.http_get_request(base_url, url_suffix)
        # print('organization_details')
        # print(response.json())
        return response

    def delete_current_domain_by_id_of_domain(self):
        SetupTearDownApiOperations.delete_domain_by_id_of_domain(self.is_acronis, self.organization_id,
                                                                 self.token_value)
        time.sleep(5)

    @allure.step("delete organization domain by id of organization")
    def delete_domain_by_id_of_domain(is_acronis, organization_id, token_value):
        domain_to_delete_id = ''
        try:
            domains_json = SetupTearDownApiOperations.get_organization_domains(organization_id, token_value,
                                                                               is_acronis=is_acronis)
            domain_to_delete_id = str(domains_json['id'])
            # SettingsOperations.delete_domain(organization_id, domain_to_delete_id, token_value)
            url_suffix = '/api/v1/users/organization-domains/' + domain_to_delete_id
            if is_acronis:
                AcronisHttpRequests.http_delete_request(BaseHttpRequests.base_url_testing, url_suffix)
            else:
                XrayHttpRequests.http_delete_request(BaseHttpRequests.base_url_testing, url_suffix)
            print("domain=" + domain_to_delete_id + " of organization=" + organization_id + " deleted successfully")
        except Exception as e:
            print(e)
            print('failed to get domain of organization')
            SetupTearDownApiOperations.logger.error('failed to DELETE domain=' + domain_to_delete_id)

    def get_current_organization_license_seats_number(self) -> String:
        return self.get_organization_license_seats_number(self.organization_id, self.token_value,
                                                          self.is_acronis)

    def get_organization_license_seats_number(self, organization_id, token_value, is_acronis):
        Reporting.report_allure_and_logger("INFO",
                                           "get license seats number by organization id=" + organization_id
                                           + " and token=" + token_value)
        organization_details_json = self.get_organization_details(
            is_acronis=is_acronis)
        domain_number_of_seats = str(organization_details_json['number_of_seats'])
        print(
            "organization=" + self.organization_id + " license seats number=" + domain_number_of_seats + " retrieved successfully")
        return domain_number_of_seats

    @staticmethod
    def get_billing_status(organization_id, is_acronis):
        base_url = 'https://api.testing.perception-point.io/'
        # response = requests.get(
        #     base_url + 'automation/xray/billing-method/' + organization_id
        #     , headers=BaseHttpRequests.get_headers(token_value))

        url_suffix_billing = 'automation/xray/billing-method/' + organization_id

        if is_acronis:
            response = AcronisHttpRequests.http_get_request(base_url=base_url, url_suffix=url_suffix_billing)
        else:
            response = XrayHttpRequests.http_get_request(base_url=base_url, url_suffix=url_suffix_billing)
        print('get billing status response' + str(response))
        return response

    @staticmethod
    def reset_billing_method(organization_id, token_value, set_billing_method):
        if set_billing_method == False:
            json_body_set_billing = {
                "enable_number_of_mailboxes_from_api": "false",
                "force_use_recipients_count_for_billing": "false",
                "force_use_seats_amount_for_billing": "false",
                "number_of_mailboxes_from_api": 0,
                "number_of_seats": 1392
            }
        else:
            json_body_set_billing = {
                "enable_number_of_mailboxes_from_api": "false",
                "force_use_recipients_count_for_billing": "true",
                "force_use_seats_amount_for_billing": "true",
                "number_of_mailboxes_from_api": 0,
                "number_of_seats": 1392
            }
        base_url = 'https://api.testing.perception-point.io/'
        response = requests.put(
            base_url + 'automation/xray/billing-method/' + organization_id + '/'
            , json_body_set_billing
            , headers=BaseHttpRequests.get_headers(token_value))
        print('reset billing status response' + str(response.json()))
        return response.json()

    def set_current_channel(self, new_channel_is_office365):
        if new_channel_is_office365:
            SetupTearDownApiOperations.set_channel(new_channel_is_office365=True, organization_id=self.organization_id,
                                                   token_value=self.token_value)
        else:
            SetupTearDownApiOperations.set_channel(new_channel_is_office365=False, organization_id=self.organization_id,
                                                   token_value=self.token_value)

    @staticmethod
    def set_channel(new_channel_is_office365, organization_id, token_value):
        json_body_office365 = {
            "origins": {
                "email": "office365"
            }
        }
        json_body_gmail = {
            "origins": {
                "email": "gmail"
            }
        }

        base_url = 'https://api.testing.perception-point.io'

        if new_channel_is_office365:
            response = requests.put(base_url + '/api/organizations/' + organization_id + '/'
                                    , json=json_body_office365,
                                    headers=BaseHttpRequests.get_headers(token_value))
            print(response.json())
        else:
            response = requests.put('https://api.testing.perception-point.io/api/organizations/' + organization_id + '/'
                                    , json=json_body_gmail,
                                    headers=BaseHttpRequests.get_headers(token_value))
            print(response.json())

    ############################################################################
    ######################Sync on Finished scan on Elastic search###############
    ############################################################################
    #     https: // api.testing.perception - point.io / api / v1 / scans / running_list /?organization_id = 7933 & limit = 5 &
    #                                                                                                                      verbose_origin[] = analyze &
    #                                                                                                                                         verbose_origin[] = api & owner_email_address = amiel.peled % 2
    #     Bautomation % 40
    #
    #     perception - point.io & verbose_status = RUN
    # Step1:
    #####################################################################################
    # find running password/passwordless file/url scan id ###############################
    #####################################################################################
    # https://api.testing.perception-point.io/api/v1/scans/running_list/?organization_id=7933&limit=5&
    #          +  verbose_origin[]=analyze & verbose_origin[] = api
    #          & owner_email_address = amiel.peled + automation @ perception - point.io
    #          & verbose_status = RUN
    #
    # Step2  use scan_id extracted from step 1
    # https://api.testing.perception-point.io/api/v1/scans/list/00017933_1_17d1c0a4-3691-4604-9317-5a9dc626c0d1_20230102/

    # 'https://api.testing.perception-point.io/api/v1/scans/list/'+scan_id+'/'
    ########################################################################
    # poll until status!=Running
    ########################################################################

    @staticmethod
    @allure.step("get detection item id={0} by detection item index(position)={1}")
    def get_running_scan_id(is_acronis, user_email_address, organization_id):
        if not is_acronis:
            user_email_address_xray = 'amiel%2Bamiel.peled.gsuite.8783610.xyz'
            user_email_address = user_email_address_xray
        get_running_scan_id_url_suffix = '/api/v1/scans/running_list/?organization_id=' \
                                         + organization_id \
                                         + '&limit=5' \
                                         + '&verbose_origin[]=analyze&verbose_origin[]=api' \
                                         + '&owner_email_address=' + user_email_address \
                                         + '&verbose_status=RUN'
        mantis_base_url = 'https://api.testing.perception-point.io'
        if is_acronis:
            current_running_scans_list = AcronisHttpRequests.http_get_request(base_url=mantis_base_url
                                                                              ,
                                                                              url_suffix=get_running_scan_id_url_suffix)
        else:
            current_running_scans_list = XrayHttpRequests.http_get_request(base_url=mantis_base_url
                                                                           , url_suffix=get_running_scan_id_url_suffix)
        # current_scan_id = current_running_scans_list[0]['id']
        Reporting.report_allure_and_logger("INFO"
                                           , "current running scans list status=" + str(not current_running_scans_list))
        return not current_running_scans_list

    ################################################################
    ################ is scan finished?? ############################
    ################################################################
    @staticmethod
    @allure.step("get is running scan by id of item")
    def get_is_running_scan_by_id_of_item(is_acronis, user_email_address, organization_id, running_scan_file_name):
        running_scan_status = ''

        if SetupTearDownApiOperations.running_scan_id == 'init_value':
            SetupTearDownApiOperations.running_scan_id = SetupTearDownApiOperations.get_running_scan_id(is_acronis,
                                                                                                        user_email_address,
                                                                                                        organization_id)
        Reporting.report_allure_and_logger("INFO",
                                           "scanned file name=" + running_scan_file_name + "\nrunning_scan_id" + SetupTearDownApiOperations.running_scan_id)

        url_is_running_item_suffix = '/api/v1/scans/list/' + SetupTearDownApiOperations.running_scan_id + '/'

        if is_acronis:
            running_scan_details = AcronisHttpRequests.http_get_request(base_url=BaseHttpRequests.base_url_testing
                                                                        , url_suffix=url_is_running_item_suffix)
        else:
            running_scan_details = XrayHttpRequests.http_get_request(base_url=BaseHttpRequests.base_url_testing
                                                                     , url_suffix=url_is_running_item_suffix)

        try:
            if len(running_scan_details['finished_at']) > 0:
                Reporting.report_allure_and_logger("INFO",
                                                   "SCAN FINISHED!!! scanned file name=" + running_scan_file_name + "\nscan_finished_at=" +
                                                   running_scan_details['finished_at'])
                SetupTearDownApiOperations.running_scan_id = 'init_value'
                return 'finished'
        except:
            print('no ****finished_at**** field in response')
            time.sleep(3)

    @staticmethod
    @allure.step("get detection item id={0} by detection item index(position)={1}")
    def get_detection_item_id_by_position(is_acronis, item_position, organization_id):
        detection_item_to_delete_url_suffix = 'api/v1/' + 'whitelist/email' \
                                              + '/?limit = 9000 & organization_id = ' + organization_id
        Reporting.report_allure_and_logger("INFO"
                                           "get detection item id by detection item index(position)" + item_position)
        if is_acronis:
            detection_item_id_by_position = AcronisHttpRequests.http_get_request(
                url_suffix=detection_item_to_delete_url_suffix)
        else:
            detection_item_id_by_position = AcronisHttpRequests.http_get_request(
                url_suffix=detection_item_to_delete_url_suffix)

        Reporting.report_allure_and_logger(
            " detection_item_position=" + item_position
            + "detection item id by position=" + detection_item_id_by_position)
        return detection_item_id_by_position

    @staticmethod
    @allure.step("delete organization domain by id of organization")
    def delete_detection_item_by_id_of_item(is_acronis, organization_id, item_position=1):
        domain_to_delete_id = ''
        try:
            detection_item_to_delete_url_suffix = 'api/v1/' + 'whitelist/email' \
                                                  + '/?limit = 9000 & organization_id = ' + organization_id
            detection_item_id_json = SetupTearDownApiOperations.get_detection_item_id_by_position(is_acronis,
                                                                                                  item_position)
            DetectionToDeleteId = str(detection_item_id_json['id'])
            # SettingsOperations.delete_domain(organization_id, domain_to_delete_id, token_value)

            DetectionType = 'whitelist/email/'
            # DetectionToDeleteId = '11938'
            url_detection_item_suffix = 'api/v1/' + DetectionType + DetectionToDeleteId + '/?organization_id = ' + organization_id

            if is_acronis:
                AcronisHttpRequests.http_delete_request(base_url=BaseHttpRequests.base_url_testing
                                                        , domain_suffix=url_detection_item_suffix)
            else:
                XrayHttpRequests.http_delete_request(base_url=BaseHttpRequests.base_url_testing
                                                     , domain_suffix=url_detection_item_suffix)

            print("domain=" + domain_to_delete_id + " of organization=" + organization_id + " deleted successfully")
        except Exception as e:
            print(e)
            print('failed to get domain of organization')
            Reporting.report_allure_and_logger("ERROR", 'failed to DELETE domain=' + domain_to_delete_id)
