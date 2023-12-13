#!/usr/bin/env python3
import time
import os
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from selenium.common.exceptions import NoSuchElementException
from modules.driver import driver_create, driver_close
from modules.login import login

load_dotenv()

headless = os.environ.get("HEADLESS")
email = os.environ.get("LOGIN_EMAIL")
password = os.environ.get("LOGIN_PASSWORD")
password_change = os.environ.get("CHANGE_PASSWORD")

driver = driver_create(headless)

login(driver, email, password)

time.sleep(1)

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
    try:
        verify_txt = driver.find_element(By.XPATH, "(//h2[normalize-space()='Password Changed!'])[1]")
        print("Password Changed Successfuly")
    except NoSuchElementException:
        print("Password entered was the same as the current password")
except NoSuchElementException:
    print("Something is wrong when changing password")

driver_close(driver)
