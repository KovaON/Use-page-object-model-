import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import pytest
from selenium import webdriver

# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()

def pytest_addoption(parser):
    """ В терминал подаем параметр вида '--language="es"'
    По умолчанию передается параметр с английским языком
    """
    parser.addoption('--language', action='store', default='en', help='Choose language')


@pytest.fixture(scope="function")
def browser(request):
    # задаем user_language
    user_language = request.config.getoption('language')
    print(user_language)
    # Создаем опции браузера
    options = Options()
    # В опции вебдрайвера передаем user_language
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()

