from .pages.main_page import MainPage
from .pages.login_page import LoginPage
main_page_link = 'http://selenium1py.pythonanywhere.com/'   
link2 = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer' 

def test_guest_can_see_login_link(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    page.should_be_login_link()

def test_guest_can_see_language_change_input_field(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    page.shold_be_language_choose_field()

def test_guest_can_see_language_change_submit_button(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    page.shold_be_go_button()


def test_guest_can_go_go_login_page(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    page.go_to_login_page()
    login_link = page.browser.current_url
    page = LoginPage(browser, login_link)
    page.should_be_login_page()

