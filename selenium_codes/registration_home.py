#from registration to homepage
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
    link=driver.find_element_by_xpath("//span[contains(@class ,'fa fa-home')]")
    print("clicked on home button from registration page")
    time.sleep(2)
    link.click()

    print("successfully navigated to home page")
    time.sleep(4)
    driver.quit()
except:
    print("failed to goto home page")
    time.sleep(4)
    driver.quit()

