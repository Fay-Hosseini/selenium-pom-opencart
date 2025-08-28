from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ForgottenPasswordPage(BasePage):
    Forgotten_PASSWORD_LINK = (By.LINK_TEXT, "Forgotten Password")
    EMAIL_INPUT = (By.ID, "input-email")
    CONTINUE_BUTTON = (By.XPATH, "//button[text()='Continue']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

    def open_forgot_password(self):
        """Clicks the 'Forgotten Password' link on the login page."""
        self.click(self.Forgotten_PASSWORD_LINK)
    def enter_email_continue(self, email):
        """Enters an email address and clicks the continue button."""
        self.type(self.EMAIL_INPUT, email)
        self.click(self.CONTINUE_BUTTON)
    def get_success_text(self):
        """Returns the text of the success message."""
        return self.get_text(self.SUCCESS_MESSAGE)



