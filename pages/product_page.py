from .base_page import BasePage
from .login_page import LoginPage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math
import time
        
class  ProductPage(BasePage):

    def add_to_basket(self):
       button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASCKET)
       button.click()
       
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    def product_added(self):
        template = "{} has been added to your basket."
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ADD).text
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert template.format(message) == template.format(book_name), 'нет названия книги {message}'.format(message=message)
    
    def price_equal_basket(self):
        template = "Your basket total is now {}"
        book_price = self.browser.find_element(*ProductPageLocators.PRICE).text
        cart_size = self.browser.find_element(*ProductPageLocators.ALERT_CART_STATUS).text.split()[-1]
        assert template.format(book_price) == template.format(cart_size), 'цена {} не равна {}'.format(book_price, cart_size)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"
    def should_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is not disappeared"
