import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
@pytest.fixture(scope = "class")
def setup(request):
    service_obj = Service("C:\\Users\\ALAGU SUNDARI\\Downloads\\chromedriver_win32 (4)\\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://dev.talentfind.io/ohr")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

