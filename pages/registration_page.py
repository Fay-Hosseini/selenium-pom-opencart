from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegistrationPage(BasePage):
    My_ACCOUNT = (By.XPATH, "//span[text()='My Account']")
    REGISTER = (By.LINK_TEXT, "Register")
    FIRST_NAME = (By.ID, "input-firstname")
    LAST_NAME = (By.ID, "input-lastname")
    EMAIL = (By.ID, "input-email")
    PASSWORD = (By.ID, "input-password")

    NEWSLETTER_NO = (By.XPATH, "//input[@name='newsletter' and @value='1']")
    PRIVACY_POLICY = (By.NAME, "agree")
    CONTINUE = (By.CSS_SELECTOR, "button[class='btn btn-primary']")

    SUCCESS_MESSAGE = (By.XPATH, "//h1[contains(text(),'Your Account Has Been Created!')]")

    def open_registration(self):
        self.click(self.My_ACCOUNT)
        self.click(self.REGISTER)

    def register_account(self,fname,lname,email,password):
        self.type(self.FIRST_NAME, fname)
        self.type(self.LAST_NAME, lname)
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        self.click(self.NEWSLETTER_NO)
        self.click(self.PRIVACY_POLICY)
        self.click(self.CONTINUE)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)
