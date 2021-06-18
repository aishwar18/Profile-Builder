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
uname[0].send_keys("test@gmail.com")
pwd=driver.find_elements_by_name("password")

pwd[0].send_keys("SEproject1")
link=driver.find_elements_by_class_name("login_button")
print("clicked on login")
link[0].click()
dropdown=driver.find_element_by_class_name("dropbtn")
print("found dropdown button")
dropdown.click()

toggle=driver.find_element_by_xpath("//a[@href='/html/myProfile']")
toggle.click()
time.sleep(1)
add=driver.find_element_by_xpath("//a[@href='/html/faculty_detail']")
add.click()
time.sleep(2)
final=driver.find_element_by_xpath("//input[@class='form-control'][@name='pos']")
final.send_keys("Associate Professor")
time.sleep(1)
dept=driver.find_element_by_xpath("//input[@class='form-control'][@name='dept']")
dept.send_keys("Computer Science Engineering, School of Engineering")
time.sleep(1)
dept=driver.find_element_by_xpath("//input[@class='form-control'][@name='loc']")
dept.send_keys("Coimbatore")
time.sleep(1)
bio=driver.find_element_by_xpath("//textarea[@class='form-control'][@name='bio']")
bio.send_keys("Amrita Vishwa Vidyapeetham ")
time.sleep(1)
aoi=driver.find_element_by_xpath("//textarea[@class='form-control'][@name='aoi']")
aoi.send_keys("Data Mining")
time.sleep(1)
sub=driver.find_element_by_xpath("//input[@class='btnContact'][@name='btnSubmit']")
sub.send_keys("Data Mining")
time.sleep(1)
driver.quit()
