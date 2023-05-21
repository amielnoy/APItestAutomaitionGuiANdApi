import os
from pathlib import Path
from tokenize import String

from dotenv import load_dotenv

from Utils.Enviornment.enviornment_files_ops import get_envvars
from LogManager import LogManager


class BaseTest:
    logger = LogManager().get_logger_instance()
    is_first_acronis_test = False
    acronis_last_build_number = 'InitAcronis'
    is_first_xray_test = False
    xray_last_build_number = 'InitXray'

    params_dictionary = None

    @staticmethod
    def get_page_url(page) -> String:
        return page.url

    @staticmethod
    def get_page_title(page) -> String:
        return page.title()

    @classmethod
    def get_non_secrets_and_secrets(cls, non_secrets_file_name, secrets_file_name):
        conftest_file_path_parent = os.path.dirname(os.path.abspath(__file__))
        tests_directory_path = Path(conftest_file_path_parent)
        project_root_path = tests_directory_path.parent.absolute()
        env_non_secrets_file = project_root_path.as_posix() + '/enviornment/' + non_secrets_file_name
        env_secrets_file = project_root_path.as_posix() + '/enviornment/' + secrets_file_name
        # dotenv_path = Path('path/to/.env')
        load_dotenv(dotenv_path=env_secrets_file)
        env_non_secrets_dictionary = get_envvars(env_non_secrets_file)
        cls.params_dictionary = env_non_secrets_dictionary
        return cls.params_dictionary
