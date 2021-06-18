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
print("clicked on login")
link[0].click()
print("login successful")
dropdown=driver.find_element_by_class_name("dropbtn")   
print("found dropdown button")
dropdown.click()
time.sleep(1)
print("dropdown opened successfully")
toggle=driver.find_element_by_xpath("//a[@href='/html/favourites']")
toggle.click()
time.sleep(2)
see=driver.find_element_by_xpath("//div[@onclick='favourites_insert()'][@class='overlay']")
see.click()
time.sleep(2)
select=driver.find_element_by_xpath("//select[@name='aoi'][@class='form-control']")
select.send_keys('cloud computing')
time.sleep(2)
add=driver.find_element_by_id("submit_btn")
add.click()
time.sleep(2)
driver.quit()
    