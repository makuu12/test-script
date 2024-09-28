from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time



driver = webdriver.Chrome()
driver.execute_script("window.open('incognito');")
driver.get("https://player.quizalize.com/quiz/9581333f-e73c-45b0-8b8e-a2f51ff1a88e?&quizMode=standard&fbclid=IwAR3Sn1wvEupW9lmQWNBioaP85fck5be9Z5Lxe34KNIY4VT4IJMVD4mI9qvY")

time.sleep(3)
start = driver.find_element(By.XPATH, "//*[@id=\"container\"]/div/div/div/div/div/div/div[2]")
start.click()
time.sleep(2)
ans = "Blue"
a1 = driver.find_elements(By.XPATH, "//button[.//p[contains(text(), '" + ans + "')]]")
# a1 = driver.find_elements(By.XPATH, "//button[.//p[contains(text(), 'Blue')]]")

if a1:
    a1[0].click() 
else:
    print("No button found")
time.sleep(5)
next = driver.find_element(By.CLASS_NAME, "_2PSgLZCXVR-nlobGH6VlHf")
next.click()

a2 = driver.find_elements(By.XPATH, "//button[.//p[contains(text(), 'Flash memory')]]")
if a2:
    a2[0].click() 
else:
    print("No button found")
# username.send_keys("hello")


