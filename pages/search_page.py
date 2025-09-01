from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SearchPage(BasePage):
    SEARCH_INPUT = (By.NAME, "search")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    SEARCH_RESULT_HEADING = (By.XPATH, "//h1[contains(text(), 'Search')]")

    def search_for_product(self, product_name):
        """Types the product name into the search bar and clicks the search button."""
        self.type(self.SEARCH_INPUT, product_name)
        self.click(self.SUBMIT_BUTTON)

    def get_search_results_heading(self):
        """Returns the text of the search results heading."""
        return self.get_text(self.SEARCH_RESULT_HEADING)



