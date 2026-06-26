from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://www.amazon.com")

driver.maximize_window() 
time.sleep(5)

print(driver.title)

driver.quit()