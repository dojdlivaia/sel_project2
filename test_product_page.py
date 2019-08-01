from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.locators import ProductPageLocators
import pytest
import time
product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(1)]

@pytest.mark.user_guest
class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        link="http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        reg = LoginPage(browser,link)
        reg.open()
        pas=str(time.time()) + "@fakemail.org"
        reg.register_new_user(pas,"We-65432444")
        reg.should_be_authorized_user()
    def test_user_cant_see_success_message(self,browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)


@pytest.mark.need_review
class TestUserAddToCartFromProductPage2(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        link="http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        reg = LoginPage(browser,link)
        reg.open()
        pas=str(time.time()) + "@fakemail.org"
        reg.register_new_user(pas,"We-65432444")
        reg.should_be_authorized_user()
    def test_user_can_add_product_to_cart(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.product_added()
        page.price_equal_basket()


@pytest.mark.need_review 
def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.product_added()
    page.price_equal_basket()
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link)
    page.open()
    page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)    
@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = CartPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_be_basket_clear()
    page.clear_basket_message()
    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

