from pages.cart_page import CartPage

# def test_positive_open_cart(browser):
#     page = CartPage(browser)
#     page.open_page_noutbuki()
#     page.open_cart()

def test_add_nout(browser):
    page = CartPage(browser)
    page.open_page_noutbuki()
    page.add_laptop_to_cart()