from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/checkbox")

home_element = driver.find_element(By.XPATH, "//label[@for='tree-node-home']")
home_element.click()

toggle_button = driver.find_element(By.XPATH, "//button[@aria-label='Toggle' and @title='Toggle']")
toggle_button.click()
home_element.click()



toggle_button2 = driver.find_element(By.XPATH, "//*[@id='tree-node']/ol/li/ol/li[1]/span/label/span[3]/../../button[@aria-label='Toggle' and @title='Toggle']")
toggle_button2.click()
time.sleep(20)
print("tested")




