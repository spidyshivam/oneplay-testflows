from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def driver_create(headless):
    if headless == "YES":
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options)
        return driver
    else:
        driver = webdriver.Chrome()
        return driver

def driver_close(driver):
   driver.close()
