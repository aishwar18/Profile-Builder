#from login to registration page
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
    
    #link=driver.find_elements_by_partial_link_text("register")
    link=driver.find_element_by_xpath("//a[contains(@href ,'/html/register')]")
    time.sleep(2)
    print("clicked on register from login page")
    link.click()
    
    print("successfully navigated to registration page")
    time.sleep(4)
    driver.quit()
except:
    print("failed to navigate to registration page")
    time.sleep(4)
    driver.quit()



