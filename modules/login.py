#!/usr/bin/env python3
import time
from selenium.webdriver.common.by import By

def login(driver, email, password):

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

    time.sleep(3)

    checkbox_agree = driver.find_element(By.XPATH, "//input[@type='checkbox' and @id='inlineCheckbox1']")
    checkbox_agree.click()

    agree_and_continue_btn = driver.find_element(By.XPATH, "//button[contains(., 'Agree & Continue')]")
    agree_and_continue_btn.click()

    if (driver.current_url == "https://www.oneplay.in/dashboard/home"):
        print("Login Successful")
        return 1
    else:
        print("Login Failed")
        return 0
