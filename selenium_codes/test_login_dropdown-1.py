import unittest
from selenium import webdriver
import time
class register_navigations(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1:8000/html/login")
        uname=self.driver.find_elements_by_name("email")
        uname[0].send_keys("adityasai0916@gmail.com")
        time.sleep(1)
        pwd=self.driver.find_elements_by_name("password")
        time.sleep(1)
        pwd[0].send_keys("SEproject1")
        linker=self.driver.find_elements_by_class_name("login_button")
        linker[0].click()
    def test_logout(self):
        
        link=self.driver.find_element_by_xpath("//button[contains(@class ,'dropbtn')]")
        time.sleep(2)
        link.click()
        time.sleep(1)
        logout=self.driver.find_element_by_xpath("//a[contains(@href ,'/html/logout')]")
        time.sleep(1)
        logout.click()
        home=self.driver.find_element_by_xpath("//a[contains(@href ,'/')]")
        time.sleep(2)
        home.click()
    def test_togglemode(self):
        dropdown=self.driver.find_element_by_class_name("dropbtn")
        print("found dropdown button")
        dropdown.click()
        time.sleep(3)
        print("dropdown opened successfully")
        toggle=self.driver.find_element_by_xpath("//a[contains(@onclick,'mybutton()')]")

        toggle.click()
        time.sleep(3)
    def test_favourites(self):
        dropdown=self.driver.find_element_by_class_name("dropbtn")
        print("found dropdown button")
        dropdown.click()
        time.sleep(3)
        print("dropdown opened successfully")
        toggle=self.driver.find_element_by_xpath("//a[@href='/html/favourites']")
        toggle.click()
        time.sleep(3)
    def test_myprofile(self):
        dropdown=self.driver.find_element_by_class_name("dropbtn")
        print("found dropdown button")
        dropdown.click()
        time.sleep(3)
        print("dropdown opened successfully")
        toggle=self.driver.find_element_by_xpath("//a[@href='/html/myProfile']")
        toggle.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()