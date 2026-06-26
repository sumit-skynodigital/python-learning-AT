# Exercise 4 (Medium)

# Given:

# <input name="password">

# Write:

# Name Locator
# XPath Locator
# CSS Locator

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("URL of the page containing the input element")

# Name Locator
input_element = driver.find_element(By.NAME, "password")

# XPath Locator
input_element = driver.find_element(By.XPATH, "//input[@name='password']")

# CSS Locator
input_element = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
