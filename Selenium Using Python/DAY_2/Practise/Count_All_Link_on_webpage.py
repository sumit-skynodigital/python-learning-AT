from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.get("https://www.wikipedia.org/")

links=driver.find_elements(By.TAG_NAME, "a")
print("Total number of links on the webpage:", len(links))

for index, link in enumerate(links, start=1):
    print(index, link.text)

time.sleep(5)
driver.quit()
