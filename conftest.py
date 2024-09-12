import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="Chrome",
                     help="Choose browser: Chrome or firefox")
    parser.addoption('--language', action="store", default="en-gb",
                     help="Choose language: 'en-gb' OR 'ru-ru'")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser_language = request.config.getoption("language")
    browser = None
      ##  Надстройка для Chrome
    options_chrome = Options()
    options_chrome.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
      ##  Надстройка для Firefox
    options_firefox = OptionsFirefox()
    options_firefox.set_preference("intl.accept_languages", browser_language)
    if browser_name == "Chrome":
        print("\nstart Chrome browser for test..")
        browser = webdriver.Chrome(options=options_chrome)
    elif browser_name == "Firefox":
        print("\nstart Firefox browser for test..")
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be Chrome or Firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
