import pytest
from pages.search_page import SearchPage

def test_search_product(driver):
    """
    Test case to validate searching with an existing product name.

    Preconditions:
    1. The product 'iMac' exists in the database.

    Steps:
    1. Open the application URL.
    2. Search for the product 'iMac'.
    3. Assert that the search results page heading contains the product name.
    """
    # Create an instance of the Search Page
    search_page = SearchPage(driver)

    # --- Test Steps ---
    # 1. Open the application URL
    search_page.open("http://localhost/opencart/")

     # 2. Search for the product "iMac"
    search_page.search_for_product("imac")

    # --- Validation ---
    # 3. Assert that the search results heading is correct
    search_results_heading = search_page.get_search_results_heading()
    assert "Search" in search_results_heading and "imac" in search_results_heading