import pytest
from selenium import webdriver

from Utilities import ReadConfiguration


@pytest.fixture()
def setup_and_teardown(request):
    browser=ReadConfiguration.read_configuration("basic info","browser")
    driver = None
    if browser.__eq__("chrome"):
        driver=webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver=webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver=webdriver.Edge()
    elif browser.__eq__("ie"):
        driver=webdriver.Ie
    else:
        print("provide a valid browser name from this list chrome/firefox/edge/ie")
    driver=webdriver.Chrome()
    driver.maximize_window()
    app_url = ReadConfiguration.read_configuration("basic info","url")
    driver.get(app_url)
    request.cls.driver=driver
    yield
    driver.quit()