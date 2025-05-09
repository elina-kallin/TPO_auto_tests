from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage(BasePage):
      
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, 'button[data-meta-name="Snippet__cart-button"]')



    def open_page_noutbuki(self):
        self.open("https://www.citilink.ru/catalog/noutbuki/")

    def add_laptop_to_cart():
        