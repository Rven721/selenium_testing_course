import pytest
from .pages .product_page import ProductPage
link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
#link2 = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear2019'
#links = [f'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer{number}' for number in range(10)] 


#@pytest.mark.parametrize('link', links)
def test_guest_can_add_prduct_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.should_be_price()
    page.should_be_book_name()
    page.add_product_to_basket()
    page.book_price_check()
    page.book_title_check()

@pytest.mark.xfail(reason="I knew it had to fell")
def test_guest_cant_see_success_message_after_adding_product_to_baskent(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.no_success_message_check()

def test_guest_cant_seesuccess_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.no_success_message_check()

@pytest.mark.xfail(reason="Message is not able to disapear")
def test_message_dissapeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.success_message_is_disapeared()
