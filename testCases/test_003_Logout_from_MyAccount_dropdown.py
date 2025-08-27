import pytest
from pages.login_page import LoginPage
def test_logout_with_valid_credentials(driver):
    """
    Test case to validate a successful logout after logging in.

    Preconditions:
    1. A user account exists.
    2. The user is logged in.

    Steps:
    1. Click on the 'My Account' dropdown.
    2. Select 'Logout'.
    3. Assert that the 'Account Logout' page is displayed.
    4. Assert that the 'My Account' dropdown now shows 'Login' again.
    """
    # Create an instance of the Login Page
    login_page = LoginPage(driver)

    # --- Login Step (to set up the test) ---
    # NOTE: This assumes a valid user account exists.
    login_page.open("http://localhost/opencart/")
    login_page.open_login_page()
    login_page.login(
        email="pavanotrainings@gmail.com",
        password="123456"
    )
    # Validate successful login
    account_header_text = login_page.get_account_page_header_text()
    assert "My Account" in account_header_text


    # --- Logout Step ---
    login_page.logout()

    # --- Validation ---
    # 1. Assert that the user is on the Account Logout page
    logout_header_text = login_page.get_logout_success_header_text()
    assert "Account Logout" in logout_header_text

    # 2. Assert that the dropdown menu now shows the Login link
    login_page.click(login_page.MY_ACCOUNT_DROPDOWN)
    login_link = login_page.driver.find_element(*login_page.LOGIN_LINK)
    assert login_link.is_displayed()