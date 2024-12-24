import pytest
from appium import webdriver
import openpyxl
from appium.options.common import AppiumOptions
import os
from dotenv import load_dotenv
import logging
from utils.config import config
import time
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Load environment variables
load_dotenv()
CURRENT_DIR = os.getenv("CURRENT_DIR", os.getcwd())

# Initialize session timing
session_start_time = None
session_end_time = None


@pytest.fixture(scope="session", autouse=True)
def session_setup():
    global session_start_time, session_end_time

    # Define paths
    tests_dir = os.path.join(CURRENT_DIR, "tests")
    apk_path = os.path.join(tests_dir, "apps", "ApplicationForm.apk")

    # Configure Appium options
    options = AppiumOptions()
    options.app_package = config.get("appPackage")
    options.app_activity = config.get("appActivity")
    options.platform_name = config.get("platformName")
    options.platform_version = config.get("platformVersion")
    options.device_name = config.get("deviceName")
    options.automation_name = config.get("automationName")
    options.no_reset = config.get("noReset", True)

    session_start_time = time.time()
    logger.info(f"Test session started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("Appium options: %s", options.to_capabilities())

    driver = None
    try:
        driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            options=options
        )
        driver.install_app(apk_path)

        if driver.is_app_installed(config["appPackage"]):
            logger.info("App installed successfully!")
        else:
            logger.error("Failed to install the app.")
        yield driver

    except Exception as e:
        logger.exception("Error during session setup")
        raise e

    finally:
        if driver:
            driver.quit()
        session_end_time = time.time()
        duration = session_end_time - session_start_time
        logger.info(f"Test session completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info(f"Total session duration: {duration:.2f} seconds")


@pytest.fixture(scope="class")
def class_setup(request):
    tests_dir = os.path.join(CURRENT_DIR, "tests")
    relative_path = os.path.join(tests_dir, "DummyData.xlsx")
    workbook = openpyxl.load_workbook(relative_path)

    data_sheet = workbook["DummyValues"]
    request.cls.workbook = workbook
    request.cls.data_sheet = data_sheet

    url = config.get("baseURL", "Default URL")
    return url


@pytest.fixture(scope="function")
def setup(session_setup, request):
    """
    This fixture prepares the app for each test and makes the driver available to the test class.
    """
    driver = session_setup
    app_package = config.get("appPackage", "com.example.applicationform")
    driver.activate_app(app_package)
    driver.implicitly_wait(15)

    # Make driver available in the test class
    request.cls.driver = driver  # This will assign the driver to the class

    yield driver
    driver.terminate_app(app_package)
