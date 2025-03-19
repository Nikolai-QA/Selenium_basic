import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

@pytest.fixture
def currency_symbol():
    return "$"

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--base_url", action="store", default="http://192.168.100.49:8081/")

@pytest.fixture(scope="function")
def browser(request):
    """Фикстура для запуска браузера"""
    browser_name = request.config.getoption("--browser")
    base_url = request.config.getoption("--base_url")

    if browser_name == "chrome":
        options = ChromeOptions()
        driver = webdriver.Chrome(service=ChromeService(), options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(service=FirefoxService(), options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")


    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.base_url = base_url
    yield driver
    driver.quit()