from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from generic.config.config_loader import ConfigLoader
from pages import base_page


class CartPage:
    ADD_TO_CART_BTN = (By.CSS_SELECTOR,"#Catalog > table > tbody > tr:nth-child(7) > td > a")
    CART_PAGE_TEXT = (By.CSS_SELECTOR,"# Cart > h2")
    TOTAL_COST = (By.XPATH,'//*[@id="Cart"]/form/table/tbody/tr[last()]/td[1]')

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)
        self.BASE_PAGE = base_page.PetStore(self.browser)

    def add_one_item(self, url):
        self.browser.get(url)
        cart_button = self.browser.find_element(*self.ADD_TO_CART_BTN)  # locating the "Add to cart button"
        cart_button.click()  # clicking the Addtocart button
        #self.BASE_PAGE.wait_for_element(self.CART_PAGE_TEXT)

    def add_allitems_to_cart(self, cart_item_urls):
        for url in cart_item_urls:
            self.add_one_item(url)

    def verify_total_cost_text(self):
        cart_total = self.browser.find_element(*self.TOTAL_COST).text
        return cart_total