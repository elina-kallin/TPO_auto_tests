from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CatalogPage(BasePage):

    CATALOG_ENTRANCE = (By.CSS_SELECTOR, 'a[href="/catalog/"]')
    PHONES_SELECT = (By.XPATH, '/html/body/div[4]/div/div/div/div/div/div[5]/div/div/div[2]/div/div[1]/div/div[1]/div/a[3]/div/span')
    TITLE_PRODUCTS = (By.CSS_SELECTOR, 'h1[data-meta-name="HolderLayout__title"]')

    def open_page(self):
        self.open("https://www.citilink.ru/")

    def select_techno(self):
        catalog = self.driver.find_element(*self.CATALOG_ENTRANCE)
        catalog.click()
    
    def select_phones_and_gadzhets(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(self.PHONES_SELECT))
        select = self.driver.find_element(*self.PHONES_SELECT)
        select.click()

    def has_ok_results(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.TITLE_PRODUCTS))
        title = self.driver.find_element(*self.TITLE_PRODUCTS)
        page_title = title.text
        purpose_str = 'Смартфоны и планшеты'
        return page_title == purpose_str


    