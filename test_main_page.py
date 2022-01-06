from .pages.main_page import MainPage

def test_guest_can_see_login_link(browser):
    link = 'http://selenium1py.pythonanywhere.com/'   
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_see_language_change_input_field(browser):
    link = 'http://selenium1py.pythonanywhere.com/'   
    page = MainPage(browser, link)
    page.open()
    page.shold_be_language_choose_field()

def test_guest_can_see_language_change_submit_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/'   
    page = MainPage(browser, link)
    page.open()
    page.shold_be_go_button()


def test_guest_can_go_go_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()


