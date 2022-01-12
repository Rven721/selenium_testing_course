import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='firefox', help='You can choose chrome or firefox')
    parser.addoption('--language', action='store', default='en', help='Choose your language') 




@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('--browser_name')
    user_language = request.config.getoption('--language')
    browser = None
    if browser_name == 'chrome':
        print('\nstarting chrome browser..')
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options, executable_path='/snap/bin/chromium.chromedriver')
    elif browser_name == 'firefox':
        print('\nstarting firefox browser..')
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError('--browser_name shold be a chrome or firefox')
    yield browser
    print('\nclosing browser..')
    browser.quit()
