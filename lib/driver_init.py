from selenium import webdriver
from lib.searchlink import search

def init_browser():
    driver = None
    driver = webdriver.Chrome()
    driver.execute_script("window.open('incognito');")
    search(driver, url = "https://www.facebook.com")
# from lib.driver_init import init_browser
# 
# driver = None
# init_browser(driver)