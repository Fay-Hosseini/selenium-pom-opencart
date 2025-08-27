import pytest
from pages.login_page import LoginPage

def test_login_with_valid_credential(driver):
    login_page = LoginPage(driver)
    login_page.open("http://localhost/opencart/")
    login_page.open_login_page()
    login_page.login(
        email="pavanotrainings@gmail.com",
        password="123456"
    )
    account_header_text = login_page.get_account_page_header_text()
    assert "My Account" in account_header_text