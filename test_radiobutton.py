from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib.take_ss import take_screenshot
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/radio-button")
yes_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[2]//*[contains(@id, "yesRadio")]')
driver.execute_script("arguments[0].checked = true;", yes_button)

print(yes_button.is_selected())  
time.sleep(10)

screenshot_path = take_screenshot(driver , folder_path = "Downloads", file_name="test_radiobutton.png")