from selenium import webdriver
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
#        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

#    def should_be_login_url(self):
#        assert "login" in str(self.browser.current_url), "Login is not presented in url"      

    def register_new_user(self,email, password):
        email1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email1.send_keys(email)
        password1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password1.send_keys(password)
        confirm = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM)
        confirm.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.SUBMIT)
        button.click()
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTOR_FORM) , "Register form is not presented"
