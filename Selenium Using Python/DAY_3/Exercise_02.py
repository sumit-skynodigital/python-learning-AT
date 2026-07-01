# Write a script that:

# Opens a website of your choice.
# Clicks a button that loads content dynamically.
# Uses an Explicit Wait to wait for the new content.
# Prints the loaded text.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

start_button=driver.find_element(By.XPATH, "//button[text()='Start']")
start_button.click()

# Wait for the new content to load
new_content=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "finish")))

# Print the loaded text
print(new_content.text)

input("Press Enter to close the browser...")
driver.quit()
