from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage(BasePage):
      
    BUTTON_ADD_TO_CART = (By.XPATH, '/html/body/div[2]/div[1]/main/section/div[3]/div/div[3]/section/div[2]/div[2]/div[1]/div/div[2]/div[8]/div[3]/div[2]/button')
    SVG_CART = (By.CSS_SELECTOR, 'a[href="/order/"]')
    NOUTS = (By.CSS_SELECTOR, 'div[data-meta-name="ProductHorizontalSnippet"]')
    PRODUCT_TITLES = (By.CSS_SELECTOR, 'div[data-meta-product-id="2002220"]')  # класс или другой селектор для товаров


    def open_page_noutbuki(self):
        self.open("https://www.citilink.ru/catalog/noutbuki/")

    def open_cart(self):
        svg_cart = self.driver.find_element(*self.SVG_CART)
        svg_cart.click()

    def add_laptop_to_cart(self):

        nouts = self.driver.find_elements(*self.PRODUCT_TITLES)
        first_nout = nouts[0]

        add_button = WebDriverWait(first_nout, 5).until(
            EC.element_to_be_clickable(self.BUTTON_ADD_TO_CART))
        self.driver.execute_script("arguments[0].click();", add_button) 