# Mini Project

# Automate:

# Open Google
# Search "Python Selenium"
# Capture all search result links
# Print first 10 result titles
# Close browser

# This introduces working with multiple elements, a very common real-world Selenium task.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()  # Maximize the browser window for better visibility
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python Selenium")
search_box.send_keys(Keys.ENTER)

time.sleep(30)

# Capture all search result links
results = driver.find_elements(By.CSS_SELECTOR, "h3")  # Using CSS selector to find all h3 elements which are typically the titles of search results')

# Print first 10 result titles
for index, result in enumerate(results[:10]):  # Loop through the first 10 results
    print(f"Result {index + 1}: {result.text}")  # Print the text of each result

time.sleep(30)
driver.quit()  # Close the browser