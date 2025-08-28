import pytest

from pages.forgotten_password_page import ForgottenPasswordPage
from pages.login_page import LoginPage
from  pages.base_page import BasePage

def test_forgot_password_success(driver):
    """
    Test case to validate the "Forgot Password" functionality up to the
    point of the email being sent.
    """
    # Create instances of the page objects
    login_page = LoginPage(driver)
    forgot_page = ForgottenPasswordPage(driver)

    # --- Test Steps ---
    # 1. Open the application URL and navigate to the Login Page
    login_page.open("http://localhost/opencart/")
    login_page.open_login_page()
    # 2. Click on 'Forgotten Password' link
    forgot_page.open_forgot_password()
    # 3. Enter the email address of an existing account and click 'Continue'
    # NOTE: This email must belong to an existing account.
    forgot_page.enter_email_continue("pavanotrainings@gmail.com")
    # --- Validation ---
    # 4. Assert that the success message is displayed
    success_message_text = forgot_page.get_success_text()
    expected_message = "text_success"
    assert expected_message in success_message_text
