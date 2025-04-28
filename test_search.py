from pages.search_page import SearchPage

def test_positive_search(browser):
    page = SearchPage(browser)
    page.open_main_page()
    page.search("ноутбук")
    assert page.has_results(), "Товары не найдены при поиске 'ноутбук'!"

def test_negative_search(browser):
    page = SearchPage(browser)
    page.open_main_page()
    page.search("сухарики")
    assert page.is_empty_results(), "Нашлись какие-то товары на запрос 'сухарики', а не должно было!"
