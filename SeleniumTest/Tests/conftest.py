from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pytest

HOME_URL = "https://practice.bpbonline.com/"

@pytest.fixture(autouse=True, params=["chrome"], scope="class")
def driver_Setup(request):
    """ Setup the driver for the test """
    driver = None
    if request.param == "chrome":
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service = service,options = options)
        driver.maximize_window()
        driver.get(HOME_URL)
    elif request.param == "edge":
        service = Service(EdgeChromiumDriverManager().install())
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(service = service,options = options)
        driver.maximize_window()
        driver.get(HOME_URL)
            
    return driver
