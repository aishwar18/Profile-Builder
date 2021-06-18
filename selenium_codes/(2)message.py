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

name=driver.find_element_by_link_text("Dr. Bhagavathi Sivakumar P.")
name.click()
time.sleep(2)
message=driver.find_element_by_xpath("//button[@type='button'][@class='btn btn-primary']")
message.click()
time.sleep(2)
text=driver.find_element_by_id('message-text')
text.send_keys("Good Morning")
time.sleep(2)
final=driver.find_element_by_xpath("//button[@type='button'][@onclick='sendEmail()']")
final.click()
time.sleep(3)

driver.quit()
# close=driver.find_element_by_xpath("//button[@type='button'][@class='btn btn-secondary']")
# close.click()
# time.sleep(2)
# driver.quit()