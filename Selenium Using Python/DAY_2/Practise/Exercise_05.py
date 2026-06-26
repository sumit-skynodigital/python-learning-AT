# Exercise 5 (Hard)

# Open:

# https://the-internet.herokuapp.com/login

# Tasks:

# Find username using ID
# Find password using CSS
# Find Login button using XPath
# Login successfully
# Print success message

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")
login_button.click()

print("Login successful!")
# success_message = driver.find_element(By.ID, "flash")
# print(success_message.text)

time.sleep(5)
driver.quit()
