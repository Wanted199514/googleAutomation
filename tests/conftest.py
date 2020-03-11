import pytest
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture(scope="session")
def browser():
    webDriver = WebDriver(executable_path="C://Windows//System32//chromedriver.exe")
    webDriver.implicitly_wait(20)
    webDriver.maximize_window()
    yield webDriver
    webDriver.close()
    webDriver.quit()
