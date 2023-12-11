#!/usr/bin/env python3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
from selenium.webdriver.chrome.options import Options

load_dotenv()

headless = os.environ.get("HEADLESS")
email = os.environ.get("LOGIN_EMAIL")
password = os.environ.get("LOGIN_PASSWORD")


if headless == "YES":
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
else:
    driver = webdriver.Chrome()


driver.get("https://www.oneplay.in/dashboard/login")
print("Website opened...")

email_input = driver.find_element(By.NAME, "name")
password_input = driver.find_element(By.NAME, "password")

email_input.send_keys(email)
print("Email Entered...")

password_input.send_keys(password)
print("Password Entered...")

login_btn = driver.find_element(By.XPATH, "//input[@type='submit']")
login_btn.click()
time.sleep(5)

if (driver.current_url == "https://www.oneplay.in/dashboard/home"):
    print("Login Successful")
else:
    print("Login Failed")

driver.close()
