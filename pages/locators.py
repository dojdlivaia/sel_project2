from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")    
class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTOR_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    SUBMIT = (By.NAME,"registration_submit")
class ProductPageLocators(object):
    ADD_TO_BASCKET = (By.CLASS_NAME, "btn-add-to-basket")
    MESSAGE_ADD = (By.CSS_SELECTOR, ".alertinner > strong")
    PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    BASKET_MESSAGE = (By.CSS_SELECTOR, "div.alertinner strong")
    ALERT_CART_STATUS = (By.CSS_SELECTOR, ".alert-noicon.alert-info p")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")
class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
class BasketPageLocators(object):
    BASKET_CONTENT = (By.CSS_SELECTOR, ".basket-items")
    BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
