from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
                                                                                                                                                               
driver=webdriver.Chrome()
driver.get("https://www.google.com")
print(driver.title)

driver.get("https://crm.skynodigital.com/auth/login")
print(driver.title)

username=driver.find_element(By.NAME, "email")
username.send_keys("sumit@skynodigital.com")

password=driver.find_element(By.NAME, "password")
password.send_keys("#Skyno@123")

button=driver.find_element(By.XPATH, "//button[@type='submit']")
button.click()

time.sleep(5)
driver.quit()