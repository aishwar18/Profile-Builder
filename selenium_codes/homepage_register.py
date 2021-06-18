#homepage to registration page
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
    link=driver.find_element_by_xpath("//span[contains(@class ,'fa fa-user')]")
    print("clicked on register")
    time.sleep(2)
    link.click()
    print("successfully navigated to register page")
    time.sleep(5)
    driver.quit()
except:
    print("failed to goto register page")
    time.sleep(5)
    driver.quit()

