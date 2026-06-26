# Exercise 1 (Easy)

# Write a script that:

# Opens Google
# Prints page title
# Prints current URL
# Closes browser


from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.google.com")

print(driver.title)
print(driver.current_url)

driver.close()

