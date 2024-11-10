from selenium.webdriver.common.by import By
from conftest import browser


class ProductPage():
    def __init__(self, browser):
        self.browser = browser

    def check_title_is(self, title):
        page_title = self.browser.find_element(By.XPATH, "//h2[@class='name']")
        assert page_title.text == title

