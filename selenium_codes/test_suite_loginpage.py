import unittest
from selenium import webdriver
import time
class login_navigations(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1:8000/html/login")
        
    def tearDown(self):
        self.driver.close()
    def test_login(self):
        uname=self.driver.find_elements_by_name("email")
        uname[0].send_keys("adityasai0916@gmail.com")
        pwd=self.driver.find_elements_by_name("password")
        time.sleep(2)
        pwd[0].send_keys("SEproject1")
        link=self.driver.find_elements_by_class_name("login_button")
        print("clicked on login")
        link[0].click()
    def test_log_register(self):
        link=self.driver.find_element_by_xpath("//a[contains(@href ,'/html/register')]")
        time.sleep(2)
        print("clicked on register from login page")
        link.click()
    def test_login_forgot(self):
        link=self.driver.find_element_by_xpath("//a[contains(@href ,'/html/forgotPassword')]")
        time.sleep(2)
        print("clicked on register from login page")
        link.click()
if __name__ == "__main__":
    unittest.main()