# Exercise 3 (Medium)

# Write a script that:

# Open Google
# Search for "Selenium Python"
# Print page title after search
# Close browser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.get("https://www.google.com")

search_box=driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")

search_box.send_keys(Keys.ENTER)

time.sleep(20)
print(driver.title)

driver.quit()