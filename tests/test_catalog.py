from pages.catalog_page import CatalogPage

def test_open_catalog(browser):
    page = CatalogPage(browser)
    page.open_page()
    page.select_techno()
    page.select_phones_and_gadzhets()
    assert page.has_ok_results(), 'Ошибка, страница товаров не соответствует выбранной категории'