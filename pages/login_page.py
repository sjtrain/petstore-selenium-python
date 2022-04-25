from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages import base_page


class LoginPage:
    USERNAME_INPUT = (By.CSS_SELECTOR, "input[name ='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name ='password']")
    LOGIN_BTN = (By.CSS_SELECTOR, "input[name ='signon']")
    SIGN_OUT_BTN = (By.CSS_SELECTOR,   "a[href='/actions/Account.action?signoff=']")

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)
        self.BASE_PAGE = base_page.PetStore(self.browser)

    def login(self, password):
        passwd = self.browser.find_element(*self.PASSWORD_INPUT) #locating password box
        passwd.click() #clicking it
        passwd.clear() #clearing it
        passwd.send_keys(password) #entering the password in pwd text box
        login = self.browser.find_element(*self.LOGIN_BTN) #locating the "Login button"
        login.click() #clicking the login button
        self.BASE_PAGE.wait_for_element(self.SIGN_OUT_BTN) #wait for the next page "Signout link" locator at the top to load

    def verify_signout_text(self):
        sign_out_text = self.browser.find_element(*self.SIGN_OUT_BTN).text
        return sign_out_text
