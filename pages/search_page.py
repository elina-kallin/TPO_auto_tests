from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SearchPage(BasePage):
    SEARCH_INPUT = (By.NAME, "text")  # ИЛИ нужный тебе локатор для поля поиска
    PRODUCT_TITLES = (By.CSS_SELECTOR, ".product-title")  # класс или другой селектор для товаров
    EMPTY_RESULTS = (By.CSS_SELECTOR, ".catalog-empty-search-title")  # сообщение если ничего не найдено

    def open_main_page(self):
        self.open("https://www.citilink.ru/")  # сайт ситилинка

    def search(self, query):
        search_box = self.driver.find_element(*self.SEARCH_INPUT)
        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

    def has_results(self):
        products = self.driver.find_elements(*self.PRODUCT_TITLES)
        return len(products) > 0

    def is_empty_results(self):
        return self.driver.find_elements(*self.EMPTY_RESULTS)
