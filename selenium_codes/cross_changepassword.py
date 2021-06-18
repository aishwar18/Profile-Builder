#cross in successful change password



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.maximize_window()
driver.get("http://127.0.0.1:8000/html/login#")
try:
    uname=driver.find_elements_by_name("email")
    uname[0].send_keys("adityasai0916@gmail.com")
    time.sleep(1)
    pwd=driver.find_elements_by_name("password")
    time.sleep(1)
    pwd[0].send_keys("SEproject1")
    linker=driver.find_elements_by_class_name("login_button")
    linker[0].click()
    link=driver.find_element_by_xpath("//button[contains(@class ,'dropbtn')]")
    time.sleep(2)
    link.click()
    time.sleep(1)
    cp=driver.find_element_by_xpath("//a[contains(@href ,'/html/changePassword')]")
    time.sleep(1)
    cp.click()
    time.sleep(2)
    user=driver.find_element_by_xpath("//input[contains(@class ,'input_field')]")
    user.send_keys("aditya")
    time.sleep(2)
    np=driver.find_element_by_xpath("//input[contains(@oninput ,'password_check()')]")
    np.send_keys("Aditya11")
    time.sleep(2)
    confirmp=driver.find_element_by_name("confirmPassword")
    confirmp.send_keys("Aditya11")
    time.sleep(2)
    submit=driver.find_element_by_xpath("//div[contains(@class ,'PR_button')]")
    submit.click()
    cross=driver.find_elements_by_xpath("//*[contains(@aria-label,'close')]")
    time.sleep(2)
    cross[0].click()
    time.sleep(4)
    driver.quit()
except Exception as e:
    print("exception found",format(e))
    print("failed to navigate to registration page")
    time.sleep(4)
    driver.quit()






