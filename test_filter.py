from pages.filter_page import FilterPage

def test_positive_search(browser):
    page = FilterPage(browser)
    page.open_page_noutbuki()
    page.filter_by_max_price(30000)
    page.are_all_prices_under(30000)
    
    assert page.are_all_prices_under(30000), 'есть что-то дороже поставленной цены...'