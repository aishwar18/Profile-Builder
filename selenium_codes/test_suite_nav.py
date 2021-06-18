import unittest
from selenium import webdriver
import time
class register_navigations(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1:8000/html/register")
    def tearDown(self):
        self.driver.close()


    def test_teacher(self):
        link=self.driver.find_element_by_xpath("//div[contains(@onclick ,'signup_teachers_redirect()')]")
        time.sleep(2)
        link.click()
        print("navigated from register page to teacher registration page")
    def test_login(self):
        link=self.driver.find_element_by_xpath("//a[contains(@href,'/html/login')]")
        time.sleep(2)
        link.click()
        print("navigated from register page to login page")
    def test_student(self):
        link=self.driver.find_element_by_xpath("//div[contains(@onclick ,'signup_students_redirect()')]")
        time.sleep(2)
        link.click()
        print("navigated to student signup page from register page")
    def test_home(self):
        link=self.driver.find_element_by_xpath("//span[contains(@class ,'fa fa-home')]")
        time.sleep(2)
        link.click()
        print("successfully navigated to home page from register page")




if __name__ == "__main__":
    unittest.main()