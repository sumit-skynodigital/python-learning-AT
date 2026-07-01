from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/login")

username=driver.find_element(By.ID, "username")
username.send_keys("tomsmith")

password=driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")

login_button=driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

success_message=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "flash")))
print(success_message.text)

input("Press Enter to close the browser...")

driver.quit()
