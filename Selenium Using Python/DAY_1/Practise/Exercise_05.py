# Mini Real-World Task

# Automate the following:

# Open Google
# Search "Automation Testing"
# Click first result
# Print page title
# Close browser

# This mimics a common automation task where a user searches and navigates through a website.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.get("https://www.google.com")
search_box=driver.find_element(By.NAME, "q")
search_box.send_keys("Automation Testing")
search_box.send_keys(Keys.RETURN)
first_result=driver.find_element(By.CSS_SELECTOR, "div.g a")
first_result.click()
print(driver.title)

time.sleep(5)
driver.quit()


