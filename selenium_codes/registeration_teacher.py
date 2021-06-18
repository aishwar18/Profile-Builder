#from registration to teacher registration
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.maximize_window()
driver.get("http://127.0.0.1:8000/html/register")

try:
    link=driver.find_element_by_xpath("//div[contains(@onclick ,'signup_teachers_redirect()')]")
    print("clicked on signup as teacher")
    time.sleep(2)
    link.click()
    print("navigated to teacher signup page")
    time.sleep(4)
    driver.quit()
except:
    print("failed to navigate to teacher signup page")
    time.sleep(4)
    driver.quit()
