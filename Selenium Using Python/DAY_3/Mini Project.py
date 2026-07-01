# Mini Project

# Automate the login process on:

# https://the-internet.herokuapp.com/login

# Requirements:

# Open the page.
# Wait for the username field.
# Enter the username.
# Enter the password.
# Click Login.
# Wait for the success message.
# Verify that the message contains:
# You logged into a secure area!
# Print:
# Login Test Passed

# if the verification succeeds.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

username=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
username.send_keys("tomsmith")

password=driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")

login_button=driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

success_message=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "flash")))
if "You logged into a secure area!" in success_message.text:
    print("Login Test Passed")
else:
    print("Login Test Failed")

input("Press Enter to close the browser...")
driver.quit()
