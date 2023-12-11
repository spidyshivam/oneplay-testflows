#!/usr/bin/env python3
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException


load_dotenv()

headless = os.environ.get("HEADLESS")
email = os.environ.get("LOGIN_EMAIL")
password = os.environ.get("LOGIN_PASSWORD")
password_change = os.environ.get("CHANGE_PASSWORD")


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
time.sleep(3)

if (driver.current_url == "https://www.oneplay.in/dashboard/home"):
    print("Login Successful")
else:
    print("Login Failed")

checkbox_agree = driver.find_element(By.XPATH, "//input[@type='checkbox' and @id='inlineCheckbox1']")
checkbox_agree.click()

agree_and_continue_btn = driver.find_element(By.XPATH, "//button[contains(., 'Agree & Continue')]")
agree_and_continue_btn.click()

time.sleep(1)

#driver.get("https://www.oneplay.in/dashboard/home")
#print("Website opened...")

dropdown_menu = driver.find_element(By.XPATH, "//a[@href='javascript:void(0)' and @role='button' and @ngbdropdowntoggle=''][@class='dropdown-toggle nav-link p-0 br50'][@aria-expanded='false']")
dropdown_menu.click()

settings_option = driver.find_element(By.XPATH, "//a[@href='javascript:void(0)' and @routerlinkactive='active' and @class='dropdown-item' and contains(span, 'Settings')]")
settings_option.click()

login_and_security_option = driver.find_element(By.XPATH, "//a[contains(@href, '/dashboard/settings/security')]")
login_and_security_option.click()

change_password_option = driver.find_element(By.XPATH, "(//img[@src='assets/img/singup-login/Group (1).svg'])[3]")
change_password_option.click()

time.sleep(3)

current_password = driver.find_element(By.XPATH, "//input[@type='password' and @placeholder='Enter your current Password' and @formcontrolname='oldPassword']")
current_password.send_keys(password)
print("Current Password entered...")

change_password = driver.find_element(By.XPATH, "//input[@type='password' and @placeholder='Enter your New Password' and @formcontrolname='password']")
change_password.send_keys(password_change)
print("New Password entered...")

change_password_confirm = driver.find_element(By.XPATH, "//input[@type='password' and @placeholder='Re-enter your New Password' and @formcontrolname='confirmPassword']")
change_password_confirm.send_keys(password_change)
print("New Password re-entered...")

confirm_btn = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-block') and contains(@class, 'customLinearGradient') and contains(@class, 'text-white') and contains(@class, 'customBorder0') and contains(@class, 'borderRadiusCustom') and contains(@class, 'mt-4')]")
confirm_btn.click()

time.sleep(3)

try:
    verify_btn = driver.find_element(By.XPATH, "//button[contains(@class, 'swal2-confirm') and contains(@class, 'swal2-styled')]")
    verify_btn.click()
    print("Password Changed Successfuly")
except NoSuchElementException:
    print("Something is wrong when changing password")
driver.close()
