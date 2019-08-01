from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
import time
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage(object):
    def test_guest_can_go_to_login_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        login_page = page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
    
    def test_guest_should_see_login_link(self,browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        time.sleep(2)
        page.should_be_login_link()

    
def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = CartPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_be_basket_clear()
    page.clear_basket_message()

def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = CartPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_be_basket_clear()
    page.clear_basket_message()
    
