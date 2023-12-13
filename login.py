from modules.driver import driver_create, driver_close
from modules.login import login
from dotenv import load_dotenv
import os

load_dotenv()

headless = os.environ.get("HEADLESS")
email = os.environ.get("LOGIN_EMAIL")
password = os.environ.get("LOGIN_PASSWORD")

driver = driver_create(headless)
login(driver, email, password)
driver_close(driver)
