import time
import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
main_page_link = 'http://selenium1py.pythonanywhere.com/'   
link2 = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer' 

@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_see_login_link(self, browser):
        page = MainPage(browser, main_page_link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_go_login_page(self, browser):
        page = MainPage(browser, main_page_link)
        page.open()
        page.go_to_login_page()
        login_link = page.browser.current_url
        page = LoginPage(browser, login_link)
        page.should_be_login_page()



def test_guest_can_see_language_change_input_field(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    page.should_be_language_choose_field()

def test_guest_can_see_language_change_submit_button(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    page.should_be_go_button()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    page.should_be_basket_button()
    page.go_to_basket()
    basket_link = page.browser.current_url
    page = BasketPage(browser, basket_link)
    page.should_not_be_products_in_basket()
    page.should_be_empty_basket_message()
