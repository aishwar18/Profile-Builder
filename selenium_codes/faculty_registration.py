#faculty registration
#mail id and username should be unique
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.maximize_window()
driver.get("http://127.0.0.1:8000/html/signup_teachers")
#first_name=input("firstname:")
#last_name=input("lastname:")
#mail_id=input("mail id")
#user_name=input("username:")
#pwd=input("paswword:")
#confirm_pwd=input("confirm password")
#security_answer=input("security answer")

   
# profile=driver.find_element_by_xpath("//*[contains(@aria-hidden,'true')][contains(@class,'fa fa-camera upload-button')]")
# driver.implicitly_wait(10)
# profile.click()
camera=driver.find_element_by_xpath("//*[@id='ptimg']")
driver.implicitly_wait(10)
camera.send_keys("C:\\Users\\adiytya\\Desktop\\teacher.jpg")
time.sleep(3)
firstname = driver.find_element_by_name("first_name")
firstname.send_keys("hello")
time.sleep(2)
  
lastname = driver.find_element_by_name("last_name")
lastname.send_keys("world")
    
time.sleep(2)
college_field = driver.find_element_by_xpath("//*[@id='col']")
college_field.send_keys("Indian Institute of Tachnology")
  
time.sleep(2)
state_field = driver.find_element_by_xpath("//*[@id='sts']")
state_field.send_keys("Tamil Nadu")
time.sleep(2)
city_field = driver.find_element_by_xpath("//*[@id='state']")
city_field.send_keys("Coimbatore")
time.sleep(2)
mail = driver.find_element_by_name("mail_id")
mail.send_keys("hello07@gmail.com")
time.sleep(2)
username = driver.find_element_by_name("username")
username.send_keys("hello07")
time.sleep(2)
password = driver.find_element_by_name("password")
password.send_keys("Hello123")
time.sleep(2)
confirm_password = driver.find_element_by_name("confirm_password")
confirm_password.send_keys("Hello123")
time.sleep(2)
sqn_field = driver.find_element_by_xpath("//*[@id='sqn']")
sqn_field.send_keys("What Is your favorite book?")
time.sleep(2)
sqna_field = driver.find_element_by_xpath("//*[@id='securityanswer']")
sqna_field.send_keys("Alchemist")
time.sleep(2)
terms_and_conditions = driver.find_element_by_xpath("//*[@id='exampleCheck1']")
terms_and_conditions.click()
time.sleep(2)
sign_up = driver.find_element_by_xpath("//*[@id='submit_btn']")
time.sleep(2)
sign_up.click()
      
    #self.assertTrue("monish@cse" in driver.find_element_by_name("email"))
print('Registration Successful...!!')
time.sleep(3)
driver.quit()
