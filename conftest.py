import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Fixture to initialize WebDriver
@pytest.fixture()
def browser():

    # Add arguments to WebDriver
    options = Options()

    # Set up headless mode
    options.add_argument('--headless')

    # Initialize WebDriver (you can use any browser driver like Chrome, Firefox, etc.)
    browser = webdriver.Chrome(options=options)

    # Maximize windows in browser
    browser.maximize_window()

    # Optionally configure an implicit wait
    browser.implicitly_wait(10)  # seconds

    # Yielding the driver object so it can be used in tests
    yield browser

    # Cleanup: Quit the driver after the test is complete
    browser.quit()

