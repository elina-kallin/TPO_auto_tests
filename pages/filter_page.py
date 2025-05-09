from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class FilterPage(BasePage):
    
    PRICE_FILTER_MAX = (By.CSS_SELECTOR, 'input[data-meta-name="FilterRangeGroup__input-max"]')
    
    #PRICE_SUBMIT_BUTTON = (By.TAG_NAME, 'button')
    FORM_FILTER = (By.CSS_SELECTOR, 'div[data-meta-name="FilterListGroupsLayout"]')
    BUTTON = (By.TAG_NAME, 'button')
    PRICE_SUBMIT_BUTTON = (By.XPATH, '')
    PRODUCT_PRICES = (By.CSS_SELECTOR, 'span[data-meta-price]')

    def open_page_noutbuki(self):
        self.open("https://www.citilink.ru/catalog/noutbuki/")
    
    def filter_by_max_price(self, max_price=30000):
        wait = WebDriverWait(self.driver, 2)
        price_input = self.driver.find_element(*self.PRICE_FILTER_MAX)
        # price_input = wait.until(EC.presence_of_element_located(self.PRICE_FILTER_MAX))
        #price_input = wait.until(EC.element_to_be_clickable(self.PRICE_FILTER_MAX))

        # Прокручиваем к элементу
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", price_input)

        # Ждём, пока элемент станет интерактивным
        #wait.until(EC.element_to_be_clickable(self.PRICE_FILTER_MAX))

        # price_input.click()
        ActionChains(self.driver).move_to_element(price_input).click().send_keys(str(max_price)).perform()
        # price_input.clear()
        # price_input.send_keys(str(max_price))

        form_filter = self.driver.find_element(*self.FORM_FILTER)
        buttons = form_filter.find_elements(*self.BUTTON)
        submit_btn = buttons[1]
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)

        # Ждём, пока элемент станет интерактивным
        wait.until(EC.element_to_be_clickable(self.PRICE_SUBMIT_BUTTON))

        submit_btn.click()

    def are_all_prices_under(self, max_price=30000):
        elements = self.driver.find_elements(*self.PRODUCT_PRICES)
        for el in elements:
            price_str = el.get_attribute("data-meta-price")
            if price_str and price_str.isdigit():
                if int(price_str) > max_price:
                    return False
        return True

