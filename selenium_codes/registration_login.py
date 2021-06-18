#registration to login page

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
    link=driver.find_element_by_xpath("//a[contains(@href,'/html/login')]")
    print("clicked on login ")
    time.sleep(2)
    link.click()
    print("navigated to login page")
    time.sleep(4)
    driver.quit()
except Exception as e:
    print("exception found",format(e))
    print("failed to navigate to login page")
    time.sleep(4)
    driver.quit()

