import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser():
    # Настройки для браузера
    options = Options()
    options.add_argument("--start-maximized")  # открыть окно на весь экран
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    
    # Указываем путь к chromedriver, если нужно (если он у тебя в PATH, можно не указывать)
    service = Service()

    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
