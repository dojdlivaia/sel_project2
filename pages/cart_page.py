from .base_page import BasePage
from .locators import BasketPageLocators


class CartPage(BasePage):
    def should_be_basket_clear(self):
       assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT),"Cart is not clear"

    def clear_basket_message(self):
        baskrt_message = self.browser.find_element(*BasketPageLocators.BASKET_TEXT).text
        assert ("Your basket is empty" in baskrt_message) \
               or ("Ваша корзина пуста" in baskrt_message), "Text not 'is empty'"      


#    def should_be_login_form(self):
#        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

#    def should_be_register_form(self):
#        assert self.is_element_present(*LoginPageLocators.REGISTOR_FORM) , "Register form is not presented"
