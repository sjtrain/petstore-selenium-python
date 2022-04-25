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

    def test_verify_total_cost_text(self):
        driver = webdriver.Chrome(executable_path="/Users/sherin/Downloads/sherin/chromedriver")
        password = self.create_login_user(driver)
        base_page = PetStore(driver)
        cart_page = CartPage(driver)
        base_page.load_url()  # will go the fn defn in base_page to load the corresponding environment url
        base_page.click_in_sign_in()  # calling the click_in_sign_in()
        login_page = LoginPage(driver)
        login_page.login(password)
        assert 'Sign Out' in login_page.verify_signout_text()
        print("After Login")
        cart_page.add_allitems_to_cart(["https://petstore.octoperf.com/actions/Catalog.action?viewItem=&itemId=EST-1",
                                        "https://petstore.octoperf.com/actions/Catalog.action?viewItem=&itemId=EST-18"])
        print("cart" + cart_page.verify_total_cost_text())
        assert "Sub Total: $210.00" == cart_page.verify_total_cost_text()
