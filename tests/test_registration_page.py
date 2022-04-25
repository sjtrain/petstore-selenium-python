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

    def test_registration(self):
        driver = webdriver.Chrome(executable_path="/Users/sherin/Downloads/sherin/chromedriver")
        base_page = PetStore(driver)
        register_page = RegistrationPage(driver)
        base_page.navigate_to_registration_page()
        username = base_page.generate_user()
        password = base_page.generate_pass()
        register_page.complete_registration_form(username=username, password=password)
        assert driver.current_url == base_page.URL
