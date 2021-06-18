#from homepage to login page
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.maximize_window()
driver.get("http://127.0.0.1:8000/")

try:
    link=driver.find_element_by_xpath("//span[contains(@class ,'fa fa-sign-in-alt')]")
    print("clicked on login")
    time.sleep(2)
    link.click()
    print("going to login page")
    time.sleep(5)
    driver.quit()
except:
    print("failed to goto login page")
    time.sleep(5)
    driver.quit()

