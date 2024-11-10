import time
from pages.homepage import HomePage
from pages.productpage import ProductPage


# Test to open Galaxy S6 page
def test_open_galaxy_s6(browser):
    homepage = HomePage (browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.check_title_is('Samsung galaxy s6')


# Test to open page with two monitors
def test_two_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_monitor()
    time.sleep(2)
    homepage.check_products_count(2)



