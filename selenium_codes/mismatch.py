#forgot password change password password not satisfying the criteria 
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
    
    link=driver.find_element_by_xpath("//a[contains(@href ,'/html/forgotPassword')]")
    time.sleep(2)
    print("clicked on the forgot password page")
    link.click()
    username=driver.find_elements_by_name("username")
    time.sleep(2)
    username[0].send_keys("aditya")
    time.sleep(2)
    submit=driver.find_elements_by_xpath("//div[contains(@class ,'PR_button')]")
    time.sleep(2)
    submit[0].click()
    time.sleep(2)
    print("entered security question page")
    answer=driver.find_elements_by_name("answer")
    answer[0].send_keys("percy jackson")
    sub=driver.find_elements_by_xpath("//div[contains(@class ,'PR_button')]")
    time.sleep(2)
    sub[0].click()
    newp=driver.find_elements_by_name("newPassword")
    time.sleep(2)
    newp[0].send_keys("Qwerty")
    confirmp=driver.find_elements_by_name("confirmPassword")
    time.sleep(2)
    confirmp[0].send_keys("Aditya")
    sub=driver.find_elements_by_xpath("//div[contains(@class ,'PR_button')]")
    sub[0].click()

    time.sleep(4)
    driver.quit()

except Exception as e:
    print("exception found",format(e))
    print("failed to navigate to registration page")
    time.sleep(4)
    driver.quit()
