from selenium import webdriver

driver=webdriver.Chrome()

driver.get("https://www.amazon.com")
print(driver.title)

driver.get("https://www.facebook.com")
print(driver.title)

driver.back()
print(driver.title)
driver.forward()
print(driver.title)
driver.quit()