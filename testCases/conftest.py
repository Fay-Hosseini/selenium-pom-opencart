import time

import allure
import pytest
from selenium import webdriver
from allure_commons.types import AttachmentType

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    time.sleep(3)
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # This hook is executed after a test has been run
    # and provides information on its result.
    outcome = yield
    report = outcome.get_result()

    # Check if the test result is 'failed'
    if report.when == "call" and report.failed:
        # Get the WebDriver instance from the test fixture
        try:
            driver = item.funcargs['driver']

            # Take a screenshot and attach it to the Allure report
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=AttachmentType.PNG
            )
        except Exception as e:
            # Handle cases where the driver isn't available
            print(f"Failed to capture screenshot: {e}")