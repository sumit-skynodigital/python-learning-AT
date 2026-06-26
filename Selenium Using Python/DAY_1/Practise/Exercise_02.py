# Exercise 2 (Easy)

# Write a script that:

# Opens Amazon
# Maximizes browser
# Prints title
# Refreshes page
# Closes browser

from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://www.amazon.com")

driver.maximize_window()
print(driver.title)

driver.refresh()
time.sleep(5)

driver.quit()
