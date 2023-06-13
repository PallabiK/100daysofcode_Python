from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

ACCOUNT_EMAIL = YOUR LOGIN EMAIL
ACCOUNT_PASSWORD = YOUR LOGIN PASSWORD
PHONE = YOUR PHONE NUMBER

url = "Your URL"

driver = webdriver.Chrome()
driver.get(url)

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

time.sleep(5)

email_field = driver.find_element(By.ID, "username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(5)
apply_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-button__text button")
apply_button.click()

time.sleep(5)
phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
if phone.text == "":
    phone.send_keys(PHONE)

submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
submit_button.click()

