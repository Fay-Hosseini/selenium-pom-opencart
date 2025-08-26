from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    MY_ACCOUNT_DROPDOWN = (By.XPATH, "//span[text()='My Account']")
    LOGIN_LINK = (By.LINK_TEXT, "Login")
    EMAIL_INPUT = (By.ID, "input-email")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR,"button[class='btn btn-primary']")
    ACCOUNT_HEADER = (By.XPATH, "//h1[text()='My Account']")

    def open_login_page(self):
        self.click(self.MY_ACCOUNT_DROPDOWN)
        self.click(self.LOGIN_LINK)

    def login(self, email, password):
        self.type(self.EMAIL_INPUT, email)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_account_page_header_text(self):
        return self.get_text(self.ACCOUNT_HEADER)
