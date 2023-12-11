#!/usr/bin/env python3
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import os
import time

load_dotenv()

headless = os.environ.get("HEADLESS")
name = os.environ.get("REGISTER_NAME")
email = os.environ.get("REGISTER_EMAIL")
phone = os.environ.get("REGISTER_PHONE")
password = os.environ.get("REGISTER_PASSWORD")
gender = os.environ.get("REGISTER_GENDER")

if headless == "YES":
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
else:
    driver = webdriver.Chrome()

driver.get("https://www.oneplay.in/dashboard/register")
print("Website opened...")

name_input = driver.find_element(By.XPATH, "//input[@formcontrolname='name']")
email_input = driver.find_element(By.XPATH, "//input[@formcontrolname='email']")
phone_input = driver.find_element(By.XPATH, "//input[@formcontrolname='phone']")
password_input = driver.find_element(By.XPATH, "//input[@formcontrolname='password']")

time.sleep(3)

name_input.send_keys(name)
print("Name Entered...")

email_input.send_keys(email)
print("Email Entered...")

phone_input.send_keys(phone)
print("Phone Entered...")

password_input.send_keys(password)
print("Password Entered...")

gender_mapping = {'M' : 1, 'F' : 2, 'O' : 3}

gender_btn =  driver.find_element(By.XPATH, f"//label[@for='opt-{gender_mapping[gender]}']")
gender_btn.click()
print("Gender Selected...")

t_and_c_agree = driver.find_element(By.ID, "customCheckRegister")
t_and_c_agree.click()
print("T&C Selected...")

register_btn = driver.find_element(By.XPATH, "//input[@type='button' and @value='Create Account']")
register_btn.click()

time.sleep(3)

try:
    verify_register = driver.find_element(By.XPATH, "//a[@class='btn btn-block customLinearGradient border-0 font18 borderRadius10 font500 text-white' and @href='javascript:void(0)']")
   # verify_register = driver.find_element(By.XPATH, "//p[text()=' Please check your email to confirm your email id ']")
    verify_register.click()
    print("Registered Successfuly")
except NoSuchElementException:
    #retry_box = driver.find_element(By.XPATH, "//button[@type='button' and contains(@class, 'swal2-confirm')]")
    error_msg = driver.find_element(By.XPATH, "//div[@class='swal2-html-container' and @id='swal2-html-container']")
    print("Registration Unsuccessful becasue: ", error_msg.text)

time.sleep(3)

driver.close()
