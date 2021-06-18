from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.maximize_window()
driver.get("http://127.0.0.1:8000/html/login")
uname=driver.find_elements_by_name("email")
uname[0].send_keys("adityasai0916@gmail.com")
pwd=driver.find_elements_by_name("password")
pwd[0].send_keys("SEproject1")
link=driver.find_elements_by_class_name("login_button")
link[0].click()
time.sleep(2)


name=driver.find_elements_by_id('facultySearch')
name[0].send_keys("Shanmuga priya")
time.sleep(3)

driver.quit()
