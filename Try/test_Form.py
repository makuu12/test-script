from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time



driver = webdriver.Chrome()
# driver.execute_script("window.open('incognito');")
driver.get("https://demoqa.com/text-box")

# choose_header = driver.find_element(By.CLASS_NAME, "pr1")
first_element_group = driver.find_element(By.ID, "userName")
first_element_group.send_keys("hello")
first_element_group.click()
time.sleep(50)