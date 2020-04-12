from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    # LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_FORM = (By.NAME, "login-username")
    PASSWORD_FORM = (By.NAME, "login-password")
    SUBMIT_BTN = (By.NAME, "login-submit")
    SUBMIT_BTN = (By.LINK_TEXT, "Я забыл пароль")

class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    SUCCESS_ADDED_ITEM_ALERT = (By.CSS_SELECTOR, "#messages>.alert:nth-child(1)>.alertinner>strong") 
    BASKET_TOTAL_COST_ALERT = (By.CSS_SELECTOR, "#messages>.alert:nth-child(3)>.alertinner>p>strong") 
    ADDING_ITEM_NAME = (By.CSS_SELECTOR, ".product_main>h1") 
    ADDING_ITEM_COST = (By.CSS_SELECTOR, ".product_main>.price_color")
