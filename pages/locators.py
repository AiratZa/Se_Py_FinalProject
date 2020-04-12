from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, "registration_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_FORM = (By.NAME, "login-username")
    PASSWORD_FORM = (By.NAME, "login-password")
    SUBMIT_BTN = (By.NAME, "login-submit")
    SUBMIT_BTN = (By.LINK_TEXT, "Я забыл пароль")