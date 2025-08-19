import pytest
import time
from pages.registration_page import RegistrationPage

# @pytest.mark.usefixtures("setup")
# class TestRegistration:

def test_register_new_account(driver):
        reg_page = RegistrationPage(driver)
        reg_page.open("http://localhost/opencart/")
        reg_page.open_registration()

        unique_email = f"testuser_{int(time.time())}@example.com"

        reg_page.register_account(
            fname="John",
            lname="Doe",
            email=unique_email,
            password="Password123"
        )

        success_text = reg_page.get_success_message()
        assert "Your Account Has Been Created!" in success_text

#pytest --alluredir=allure-results
# allure serve allure-results