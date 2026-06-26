from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()

driver.get("https://crm.skynodigital.com/auth/login")

username=driver.find_element(By.NAME, "email")
username.send_keys("sumit@skynodigital.com")

password=driver.find_element(By.NAME, "password")
password.send_keys("#Skyno@123")

login_button=driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

time.sleep(20)
