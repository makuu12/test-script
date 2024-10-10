from selenium import webdriver
from lib.driver_init import init_browser
from lib.take_ss import take_screenshot

import time

init_browser()
driver = webdriver.Chrome()

screenshot_path = take_screenshot(driver, folder_path = "Downloads", file_name="test_screenshotz.png")
print("Screenshot has been captured")