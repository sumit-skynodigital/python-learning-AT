# Exercise 4 (Medium)

# Open:

# https://the-internet.herokuapp.com/login

# Tasks:

# Enter username:
# tomsmith
# Enter password:
# SuperSecretPassword!
# Click Login
# Verify success message appears

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

username=driver.find_element(By.ID, "username")
username.send_keys("tomsmith")

password=driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")

login_button=driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

time.sleep(5)
success_message=driver.find_element(By.ID, "flash")
print(success_message.text)

time.sleep(5)
driver.quit()
