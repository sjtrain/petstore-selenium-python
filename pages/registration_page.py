from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from generic.config.config_loader import ConfigLoader
from pages import base_page


class RegistrationPage:
    EnvConfig = ConfigLoader.load_config()
    USER_ID_INPUT = (By.CSS_SELECTOR, "input[name ='username']")
    NEW_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name ='password']")
    REPEAT_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name ='repeatedPassword']")
    FIRST_NAME = (By.CSS_SELECTOR, "input[name ='account.firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[name ='account.lastName']")
    EMAIL = (By.CSS_SELECTOR, "input[name ='account.email']")
    PHONE = (By.CSS_SELECTOR, "input[name ='account.phone']")
    ADDRESS_1 = (By.CSS_SELECTOR, "input[name ='account.address1']")
    ADDRESS_2 = (By.CSS_SELECTOR, "input[name ='account.address2']")
    CITY = (By.CSS_SELECTOR, "input[name ='account.city']")
    STATE = (By.CSS_SELECTOR, "input[name ='account.state']")
    ZIP = (By.CSS_SELECTOR, "input[name ='account.zip']")
    COUNTRY = (By.CSS_SELECTOR, "input[name ='account.country']")
    CONFIRM_BTN = (By.CSS_SELECTOR, "#Catalog > form > input[type=submit]")

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)
        self.BASE_PAGE = base_page.PetStore(self.browser)

    def complete_user_information(self, username, password):
        user_id = self.browser.find_element(*self.USER_ID_INPUT)
        user_id.send_keys(username)
        password_input = self.browser.find_element(*self.NEW_PASSWORD_INPUT)
        password_input.send_keys(password)
        repeat_pass = self.browser.find_element(*self.REPEAT_PASSWORD_INPUT)
        repeat_pass.send_keys(self.EnvConfig.password)

    def complete_account_information(self):
        first_name = self.browser.find_element(*self.FIRST_NAME)
        first_name.send_keys(self.EnvConfig.first_name)
        last_name = self.browser.find_element(*self.LAST_NAME)
        last_name.send_keys(self.EnvConfig.last_name)
        email = self.browser.find_element(*self.EMAIL)
        email.send_keys(self.EnvConfig.email)
        phone = self.browser.find_element(*self.PHONE)
        phone.send_keys(self.EnvConfig.phone)
        address_1 = self.browser.find_element(*self.ADDRESS_1)
        address_1.send_keys(self.EnvConfig.address_1)
        address_2 = self.browser.find_element(*self.ADDRESS_2)
        address_2.send_keys(self.EnvConfig.address_2)
        city = self.browser.find_element(*self.CITY)
        city.send_keys(self.EnvConfig.city)
        state = self.browser.find_element(*self.STATE)
        state.send_keys(self.EnvConfig.state)
        zip = self.browser.find_element(*self.ZIP)
        zip.send_keys(self.EnvConfig.zip)
        country = self.browser.find_element(*self.COUNTRY)
        country.send_keys(self.EnvConfig.country)

    def confirm_registration(self):
        confirm_btn = self.browser.find_element(*self.CONFIRM_BTN)
        confirm_btn.click()
        self.BASE_PAGE.wait_for_element(self.BASE_PAGE.SIGN_IN_BTN)

    def complete_registration_form(self, username, password):
        self.complete_user_information(username, password)
        self.complete_account_information()
        self.confirm_registration()