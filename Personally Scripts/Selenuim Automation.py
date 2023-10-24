from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from time import sleep

# find the xpath and use return to enter what you want to search
driver = webdriver.Chrome()
driver.get("https://google.com")
elem = driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
time.sleep(5)
elem.clear()
elem.send_keys('Python')
elem.send_keys(Keys.RETURN)
time.sleep(5)

# Click instead of enter
elem = driver.find_element(By.PARTIAL_LINK_TEXT, 'Downloads')
time.sleep(2)
elem.click()
time.sleep(7)

# Close the browser
driver.quit()