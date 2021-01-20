from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_product_page()
    page.solve_quiz_and_get_code()
    time.sleep(10)
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_product_page()
