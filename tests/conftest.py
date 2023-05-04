import errno
import os
from pathlib import Path

import allure
# ------------------------------------------------------------
# fixtures
# ------------------------------------------------------------
import pytest
from dotenv import load_dotenv
# ------------------------------------------------------------
# Imports
# ------------------------------------------------------------
from playwright.sync_api import Playwright

from Utils.Reporting.Reporting import Reporting
from Utils.Time.Time import Time
from Utils.Enviornment.enviornment_files_ops import get_envvars
from logManager import logManager
from pages.login import login
from test_base import BaseTest


@pytest.fixture(scope="session")
def read_non_secrets():
    conftest_file_path_parent = os.path.dirname(os.path.abspath(__file__))
    tests_directory_path = Path(conftest_file_path_parent)
    project_root_path = tests_directory_path.parent.absolute()
    env_non_secrets_file = project_root_path.as_posix() + '/enviornment/.non_secrets_env'
    env_secrets_file = project_root_path.as_posix() + '/enviornment/.env'
    # dotenv_path = Path('path/to/.env')
    load_dotenv(dotenv_path=env_secrets_file)
    env_non_secrets_dictionary = get_envvars(env_non_secrets_file)
    yield env_non_secrets_dictionary


@pytest.fixture(scope="function")
def login_setup(setup_data_driven_login, read_non_secrets):
    page = setup_data_driven_login
    dictionary_env_params = read_non_secrets
    acronis_url = dictionary_env_params.get("ACRONIS_BASE_URL")
    login_page = login(page, acronis_url)

    login_page.load()
    # When the user logs in with user+password
    acronis_username = os.getenv("ACRONIS_USERNAME1")
    acronis_password = os.getenv("ACRONIS_PASSWORD1")
    login_page.login(acronis_username, acronis_password)

    return page


@pytest.fixture(scope="function")
def setup_browser_page(playwright: Playwright, request) -> None:
    testname = request.node.name
    logger = logManager().get_logger_instance()
    logger.info("**********************************************************************************")
    logger.info("**********************STARTING TEST**** " + testname + "**************************")
    logger.info("**********************************************************************************")
    # browser = playwright.webkit.launch(headless=False)

    my_record_video_dir = testname + "_" + Time.get_current_date_time()

    current_date = Time.get_current_date()
    Path("videos/" + current_date).mkdir(parents=True, exist_ok=True)
    current_hour = Time.get_current_time().split('_')[0]
    Path("videos/" + current_date + '/' + current_hour).mkdir(parents=True, exist_ok=True)
    my_record_video_dir = "test_output/videos/" + current_date + '/' + current_hour + '/' + my_record_video_dir
    Path(my_record_video_dir).mkdir(parents=True, exist_ok=True)

    conftest_file_path_parent = os.path.dirname(os.path.abspath(__file__))
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1920, "height": 1080}, record_video_dir=my_record_video_dir)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    failed_before = request.session.testsfailed
    yield page

    # write mantis_viewer build number to .build_details_env file
    # so github workflow ci can read it
    # if not BaseTest.is_first_acronis_test:
    #     BaseTest.is_first_acronis_test = True
    # elif not BaseTest.is_first_xray_test:
    #     BaseTest.is_first_xray_test = True

    githubWorkflowNumber_acronis = ''
    githubWorkflowNumber_xray = ''
    github_run_id = page.evaluate('document.querySelector("meta[name=xray-build-version]").content.split("-")[0]')
    last_commit_hash = page.evaluate(
        'document.querySelector("meta[name=xray-build-version]").content.split("-")[1]')
    if not BaseTest.is_first_acronis_test and 'acronis' in testname:
        githubWorkflowNumber_acronis = page.evaluate(
            'document.querySelector("meta[name=xray-build-version]").content.split("-")[2]')
        githubWorkflowNumber_acronis = 'ACRONIS_' + githubWorkflowNumber_acronis
    elif not BaseTest.is_first_xray_test and 'xray' in testname:
        githubWorkflowNumber_xray = page.evaluate(
            'document.querySelector("meta[name=xray-build-version]").content.split("-")[2]')
        githubWorkflowNumber_xray = 'XRAY_' + githubWorkflowNumber_xray
    if not BaseTest.is_first_acronis_test or not BaseTest.is_first_xray_test:
        logger.info("EXTRACTED BUILD NUMBER=" + github_run_id)
        logger.info("EXTRACTED LAST COMMIT HASH=" + last_commit_hash)
        logger.info("GIT WORK FLOW ACRONIS NUMBER=" + githubWorkflowNumber_acronis)
        logger.info("GIT WORK FLOW XRAY NUMBER=" + githubWorkflowNumber_xray)

    conftest_file_path_parent = os.path.dirname(os.path.abspath(__file__))
    tests_directory_path = Path(conftest_file_path_parent)
    project_root_path = tests_directory_path.parent.absolute()
    env_build_details_file = project_root_path.as_posix() + '/.build_details_env'

    if not BaseTest.is_first_acronis_test or not BaseTest.is_first_xray_test:

        if not BaseTest.is_first_acronis_test and 'acronis' in testname:
            with open(env_build_details_file, "w") as envfile:
                envfile.write(f"ENV_BUILD_DETAILS_FILE={github_run_id}\n")
                envfile.write(f"ENV_BUILD_DETAILS_DICTIONARY={last_commit_hash}\n")
                envfile.write(f"GIT_HUB_WORK_FLOW_ACRONIS_NUMBER={githubWorkflowNumber_acronis}\n")
                BaseTest.acronis_last_build_number = githubWorkflowNumber_acronis
                envfile.write(f"GIT_HUB_WORK_FLOW_XRAY_NUMBER={BaseTest.xray_last_build_number}\n")
                BaseTest.is_first_acronis_test = True
        elif not BaseTest.is_first_xray_test and 'xray' in testname:
            with open(env_build_details_file, "w") as envfile:
                envfile.write(f"ENV_BUILD_DETAILS_FILE={github_run_id}\n")
                envfile.write(f"ENV_BUILD_DETAILS_DICTIONARY={last_commit_hash}\n")
                envfile.write(f"GIT_HUB_WORK_FLOW_ACRONIS_NUMBER={BaseTest.acronis_last_build_number}\n")
                BaseTest.xray_last_build_number = githubWorkflowNumber_xray
                envfile.write(f"GIT_HUB_WORK_FLOW_XRAY_NUMBER={githubWorkflowNumber_xray}\n")
                BaseTest.is_first_xray_test = True

    conftest_file_path_parent = os.path.dirname(os.path.abspath(__file__))
    project_root_path = Path(conftest_file_path_parent)
    log_file_path = os.path.join(project_root_path.parent, "test_output/TestLogs/tests.log")
    # log_file_path="/home/amielnoyfeld/PycharmProjects/playwright-python-xray-POC/TestLogs/tests.log"
    allure.attach.file(log_file_path, "tests log file", allure.attachment_type.TEXT)
    # delete old session storage file

    # recreate storge login session file
    # browser is still open !!
    if not page.is_closed():
        current_path_name = context.pages[0].video.path()
        print("videoPath=" + current_path_name)
    else:
        Reporting.report_allure_and_logger("INFO", "Browser already closed no video or screenshot SORRY!")

    # updated_video_path = os.path.join(current_path_name, f'{request.node.originalname}_{browser_name}.webm')
    # ONLY now the video exists!!!
    try:
        if request.session.testsfailed != failed_before:
            print("\nTest failed=" + testname + "\n")
            # Create TRACE in it's unique test trace folder
            trace_dir_path = "test_output/traces/" + current_date + '/' + current_hour + '/' \
                             + testname + "_" + Time.get_current_date_time()
            if not os.path.isdir(trace_dir_path):
                Path(trace_dir_path).mkdir(parents=True, exist_ok=True)
                test_trace_full_path = trace_dir_path + "/" + testname + "_" + "_trace.zip"
                context.tracing.stop(path=test_trace_full_path)
                # allure.attach.file(test_trace_full_path, "trace", allure.attachment_type.)
            if not page.is_closed():
                Reporting.take_screenshot_and_add_to_report(page, str(testname))
                # AwsOps.aws_s3_ops.list_s3_bucket()
                # Add screenshot to S3 Bucket
    except OSError as e:
        if e.errno == errno.EEXIST and os.path.isdir(input):
            pass
        else:
            raise
        print("Oops!", e.__class__, "occurred.")
        print()
        Reporting.report_allure_and_logger("INFO", "\nAllure teardown,failed to attach=" + testname + " screenshot")

    video_path = page.video.path()
    # browser.close()
    # context.close()
    page.context.close()
    try:
        if request.session.testsfailed != failed_before:
            allure.attach.file(video_path, "video", allure.attachment_type.WEBM)
            # Add The video in the ****same Path as local path***** to S3 Bucket
    except:
        Reporting.report_allure_and_logger("INFO", "\nAllure teardown,failed to attach=" + testname + " screenshot")
    # page.close()
    os.rename(current_path_name, my_record_video_dir + '/' + testname + '.webm')
    logger.info("**********************************************************************************")
    logger.info("***********FINISHING********** TEST: " + testname + "*********************************")
    logger.info("**********************************************************************************")


@pytest.fixture(scope="function")
def setup_data_driven_login(playwright: Playwright, request) -> None:
    testname = request.node.name
    logger = logManager().get_logger_instance()
    logger.info("**********************************************************************************")
    logger.info("**********************STARTING TEST**** " + testname + "**************************")
    logger.info("**********************************************************************************")
    # browser = playwright.webkit.launch(headless=False)

    my_record_video_dir = testname + "_" + Time.get_current_date_time()

    current_date = Time.get_current_date()
    Path("videos/" + current_date).mkdir(parents=True, exist_ok=True)
    current_hour = Time.get_current_time().split('_')[0]
    Path("videos/" + current_date + '/' + current_hour).mkdir(parents=True, exist_ok=True)
    my_record_video_dir = "videos/" + current_date + '/' + current_hour + '/' + my_record_video_dir
    Path(my_record_video_dir).mkdir(parents=True, exist_ok=True)
    browser = playwright.chromium.launch(headless=False)

    # conftest_file_path_parent = os.path.dirname(os.path.abspath(__file__))
    # project_root_path = Path(conftest_file_path_parent)
    context = browser.new_context(record_video_dir=my_record_video_dir)
    # context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    failed_before = request.session.testsfailed

    yield page

    conftest_file_path_parent = os.path.dirname(os.path.abspath(__file__))
    project_root_path = Path(conftest_file_path_parent)
    log_file_path = os.path.join(project_root_path.parent, "test_output/TestLogs/tests.log")
    # log_file_path="/home/amielnoyfeld/PycharmProjects/playwright-python-xray-POC/TestLogs/tests.log"
    allure.attach.file(log_file_path, "tests log file", allure.attachment_type.TEXT)

    # storage = context.storage_state(path=str(project_root_path.parent) + "/TestData/state.json")
    # print("saved new login session storage=")
    # print(storage)
    # browser is still open !!
    if not page.is_closed():
        current_path_name = context.pages[0].video.path()
        print("videoPath=" + current_path_name)
    else:
        Reporting.report_allure_and_logger("INFO", "Browser already closed no video or screenshot SORRY!")

    # updated_video_path = os.path.join(current_path_name, f'{request.node.originalname}_{browser_name}.webm')
    # ONLY now the video exists!!!
    if request.session.testsfailed == 1:
        print("\nTest failed=" + testname)
        # testname = request.session.testsfailed
        if not page.is_closed():
            Reporting.take_screenshot_and_add_to_report(page, str(testname))

    # browser.close()
    video_path = page.video.path()
    # browser.close()
    # context.close()
    page.context.close()
    if request.session.testsfailed != failed_before:
        allure.attach.file(video_path, "video", allure.attachment_type.WEBM)
    # page.close()
    # context.tracing.stop(path="trace.zip")
    os.rename(current_path_name, my_record_video_dir + '/' + testname + '.webm')
    logger.info("**********************************************************************************")
    logger.info("***********FINISHING********** TEST: " + testname + "*********************************")
    logger.info("**********************************************************************************")
