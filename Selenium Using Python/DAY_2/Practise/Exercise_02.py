# Exercise 2 (Easy)

# Given:

# <button>Login</button>

# Write XPath using text.

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("URL of the page containing the button element")

# XPath using text
login_button_by_xpath = driver.find_element(By.XPATH, "//button[text()='Login']")

