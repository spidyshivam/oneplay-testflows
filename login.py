#!/usr/bin/env python3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()

email = os.environ.get("LOGIN_EMAIL")
password = os.environ.get("LOGIN_PASSWORD")

driver = webdriver.Firefox()
driver.get("https://www.oneplay.in/dashboard/login")

email_input = driver.find_element(By.NAME, "name")
password_input = driver.find_element(By.NAME, "password")

email_input.send_keys(email)
password_input.send_keys(password)

login_btn = driver.find_element(By.XPATH, "//input[@type='submit']")
login_btn.click()

time.sleep(5)


driver.close()
