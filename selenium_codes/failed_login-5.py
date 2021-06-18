from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.maximize_window()
driver.get("http://127.0.0.1:8000/html/login")
try:
    uname=driver.find_elements_by_name("email")
    uname[0].send_keys("aditya")
    pwd=driver.find_elements_by_name("password")
    pwd[0].send_keys("apdaid")
    link=driver.find_elements_by_class_name("login_button")
    link.click()
    time.sleep(5)
    driver.quit()
except:
    print("login failed")
    time.sleep(5)
    driver.quit()



