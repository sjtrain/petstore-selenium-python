import os
from random import randint
from generic.config.config_loader import ConfigLoader
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PetStore:
    EnvConfig = ConfigLoader.load_config() #ConfigLoader is a class which contains fn load_config() that returns either dev, test or stage environment and stores in the variable EnvConfig
    URL = EnvConfig.url #Corresponding environment.url(DevConfig.url or TestConfig.url or StageConfi.url  from the environment_config.py is stored in URL
    SIGN_IN_BTN = (By.CSS_SELECTOR, '#MenuContent > a:nth-child(3)')  #Locating the "Sign In"  link
    LOGIN_PAGE_TEXT = (By.CSS_SELECTOR, "#Catalog > form > p:nth-child(1)") #Locating the text "Please enter your username and password" in SignIn page
    USER_ID_INPUT = (By.CSS_SELECTOR, "input[name ='username']") #Locating "User ID" text box in the Register page
    REGISTER_NOW_BTN = (By.CSS_SELECTOR, "#Catalog > a") #Locating the "Register Now" button

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def load_url(self):
        self.browser.get(self.URL)

    def wait_for_element(self, element):
        self.wait.until(EC.presence_of_element_located(element))

    def click_in_sign_in(self): #this fn locates the signin button and clicks it. Then wait for the text "Please enter your username and password" to appear
        sign_in_btn = self.browser.find_element(*self.SIGN_IN_BTN)
        sign_in_btn.click()
        self.wait_for_element(self.LOGIN_PAGE_TEXT) #calls the fn wait_for_element() and waits until the locator for that elemt(text pls enter usern n pwd) is loaded

    def navigate_to_registration_page(self): #this fn. just go to the register page from sign in page
        self.load_url() #since we r in the sigin page we need to go the start page
        self.click_in_sign_in()
        register_btn = self.browser.find_element(*self.REGISTER_NOW_BTN) #locating the "Register Now" button in the sign in page
        register_btn.click() #clicking it
        self.wait_for_element(self.USER_ID_INPUT) #waiting for the "User ID" text box in the Register page to load

    def get_login_text(self):
        login_text = self.browser.find_element(*self.LOGIN_PAGE_TEXT).text
        return login_text

    def generate_user(self):
        random = str(randint(12345, 99999))
        env = os.getenv('env', 'dev')
        return env + random

    def generate_pass(self):
        random_password = "Test."
        random = str(randint(12345, 99999))
        return random_password + random