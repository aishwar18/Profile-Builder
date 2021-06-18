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
    def tearDown(self):
        self.driver.close()

    def test_byname(self):
        name=self.driver.find_elements_by_id('facultySearch')
        time.sleep(1)
        name[0].send_keys("Shanmuga priya")
        time.sleep(3)
    def test_by_aoi(self):
        name=self.driver.find_elements_by_id('aoiSearch')
        time.sleep(1)
        name[0].send_keys("machine learning")
        time.sleep(3)
    def test_no_of_rows(self):
        rows=self.driver.find_element_by_id("maxRows")
        rows.click()
        time.sleep(2)
        print("5 rows checked")
        submit=self.driver.find_elements_by_xpath("//option[contains(@value ,'10')]")
        submit[0].click()
        time.sleep(2)
        print("10 rows checked")

        submit=self.driver.find_elements_by_xpath("//option[contains(@value ,'20')]")
        submit[0].click()
        time.sleep(2)
        print("20 rows checked")
        # submit=driver.find_elements_by_xpath("//option[contains(@value ,'50')]")
        # submit[0].click()
        # time.sleep(3)
        # print("50 rows checked")
        submit=self.driver.find_elements_by_xpath("//option[contains(@value ,'100')]")
        submit[0].click()
        time.sleep(2)
        print("100 rows checked")
        submit=self.driver.find_elements_by_xpath("//option[contains(@value ,'5000')]")
        submit[0].click()
        time.sleep(2)
        print("all rows checked")
    def test_next_button(self):
        for i in range(0,7):
            next=self.driver.find_element_by_id("prev")
            next.click()
            time.sleep(2)
    def test_clearfilter(self):
        name=self.driver.find_elements_by_id('facultySearch')
        name[0].send_keys("Shanmuga priya")
        time.sleep(3)
        clear_button = self.driver.find_element_by_xpath("//input[@class='filter_btn'][@type='button']")
        clear_button.click()
        time.sleep(3)
        
if __name__ == "__main__":
    unittest.main()