from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage(BasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[type="search"]')  # ИЛИ нужный тебе локатор для поля поиска
    PRODUCT_TITLES = (By.CSS_SELECTOR, 'div[data-meta-product-id="2002220"]')  # класс или другой селектор для товаров
    EMPTY_RESULTS = (By.CSS_SELECTOR, ".catalog-empty-search-title")  # сообщение если ничего не найдено

    def open_main_page(self):
        self.open("https://www.citilink.ru/")  # сайт ситилинка

    def search(self, query):
        search_box = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located(self.SEARCH_INPUT))
        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

    def has_results(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.PRODUCT_TITLES))
        products = self.driver.find_elements(*self.PRODUCT_TITLES)
        return len(products) > 0

    def is_empty_results(self):
        return self.driver.find_elements(*self.EMPTY_RESULTS)
