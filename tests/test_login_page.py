import logging
from random import randint
from faker import Faker
from pages.login_page import LoginPage
from pages.base_page import PetStore
from pages.registration_page import RegistrationPage
from pages.cart_page import CartPage
from generic.config.config_loader import ConfigLoader
from selenium.webdriver.common.by import By
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

class Tests:

    @classmethod
    def setup_class(cls):
        cls.EnvConfig = ConfigLoader.load_config()
        cls.fake = Faker()
        cls.random = randint(12345, 99999)

    def create_login_user(self, driver):
        base_page = PetStore(driver)
        register_page = RegistrationPage(driver)
        username = base_page.generate_user() #calls the fn generate_user() which returns a random username that is stored in the username variable
        password = base_page.generate_pass() # calls the fn generate_pass()
        base_page.navigate_to_registration_page() #calls the fn navigate_to_registration_page()
        register_page.complete_registration_form(username=username, password=password)
        return password

    def test_login(self):
        driver = webdriver.Chrome(executable_path="/Users/sherin/Downloads/sherin/chromedriver")
        password = self.create_login_user(driver) #Calling the fn create_login_user() and return value stored in password
        base_page = PetStore(driver)
        login_page = LoginPage(driver)
        base_page.load_url() #will go the fn defn in base_page to load the corresponding environment url
        base_page.click_in_sign_in() #calling the click_in_sign_in()
        login_page.login(password) #calling fn login..password returned from create_login_user() is given as parameter to login()
        assert 'Sign Out' in login_page.verify_signout_text()
