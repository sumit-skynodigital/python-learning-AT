#print every image url on the web page
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org/")

images = driver.find_elements(By.TAG_NAME, "img")
for index, image in enumerate(images, start=1):
    print(f"Image {index}: {image.get_attribute('src')}")

driver.quit()
