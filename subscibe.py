#!/usr/bin/env python3
from modules.driver import driver_create, driver_close
from modules.login import login
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
import time

load_dotenv()

headless = os.environ.get("HEADLESS")
email = os.environ.get("LOGIN_EMAIL")
password = os.environ.get("LOGIN_PASSWORD")
subscription_hours = int(os.environ.get("SUBSCRIPTION_HOURS"))

driver = driver_create(headless)

login(driver, email, password)

driver.get("https://www.oneplay.in/subscription.html")
print("Website Opened...")

slider = driver.find_element(By.ID, "slider")

slider_values = {1 : 0, 3 : 15, 5 : 25, 10 : 50, 20 : 75, -1 : 100}
driver.execute_script("arguments[0].value = arguments[1];", slider, slider_values[subscription_hours])
driver.execute_script("arguments[0].onchange();", slider)

time.sleep(3)

driver_close(driver)
