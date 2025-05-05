from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage(BasePage):
      
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, 'button[data-meta-name="Snippet__cart-button"]')
    SVG_CART = (By.CSS_SELECTOR, 'a[href="/order/"]')
    NOUTS = (By.CSS_SELECTOR, 'div[data-meta-name="ProductHorizontalSnippet"]')


    def open_page_noutbuki(self):
        self.open("https://www.citilink.ru/catalog/noutbuki/")

    def open_cart(self):
        svg_cart = self.driver.find_element(*self.SVG_CART)
        svg_cart.click()

    def add_laptop_to_cart(self):

        nouts = self.driver.find_elements(*self.NOUTS)
        first_nout = nouts[1]
        # add_nout_button = first_nout.find_element(*self.BUTTON_ADD_TO_CART)

        add_button = WebDriverWait(first_nout, 10).until(
            EC.element_to_be_clickable(self.BUTTON_ADD_TO_CART))
        add_button.click()

        # add_nout_button.click()