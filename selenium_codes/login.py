#checking if all login fields are working
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
    uname[0].send_keys("adityasai0916@gmail.com")
    pwd=driver.find_elements_by_name("password")
    time.sleep(2)
    pwd[0].send_keys("SEproject1")
    link=driver.find_elements_by_class_name("login_button")
    print("clicked on login")
    link[0].click()
    time.sleep(3)
    print("login successful")
    time.sleep(3)
    driver.quit()
except Exception as e:  
    print("exception found",format(e))
    print("login failed")
    time.sleep(3)
    driver.quit()



