# Write a script that:

# Opens Google.
# Waits until the page title contains "Google".
# Prints the title.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://www.google.com")

title=WebDriverWait(driver, 10).until(EC.title_contains("Google"))
print(driver.title)

input("Press Enter to close the browser...")
driver.quit()
