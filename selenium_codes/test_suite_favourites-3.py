import unittest
from selenium import webdriver
import time
class favourites(unittest.TestCase):
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


    def test_view(self):
        dropdown=self.driver.find_element_by_class_name("dropbtn")
        print("found dropdown button")
        dropdown.click()
        time.sleep(3)
        print("dropdown opened successfully")
        toggle=self.driver.find_element_by_xpath("//a[@href='/html/favourites']")
        toggle.click()
        time.sleep(3)
        see=self.driver.find_element_by_xpath("//div[@onclick='favourites_view()'][@class='overlay']")
        see.click()
    def test_add(self):
        dropdown=self.driver.find_element_by_class_name("dropbtn")
        print("found dropdown button")
        dropdown.click()
        time.sleep(1)
        print("dropdown opened successfully")
        toggle=self.driver.find_element_by_xpath("//a[@href='/html/favourites']")
        toggle.click()
        time.sleep(2)
        see=self.driver.find_element_by_xpath("//div[@onclick='favourites_insert()'][@class='overlay']")
        see.click()
        time.sleep(2)
        select=self.driver.find_element_by_xpath("//select[@name='aoi'][@class='form-control']")
        select.send_keys('cloud computing')
        time.sleep(2)
        add=self.driver.find_element_by_id("submit_btn")
        add.click()
        time.sleep(2)
    def test_delete(self):
        dropdown=self.driver.find_element_by_class_name("dropbtn")
        print("found dropdown button")
        dropdown.click()
        print("dropdown opened successfully")
        toggle=self.driver.find_element_by_xpath("//a[@href='/html/favourites']")
        toggle.click()
        time.sleep(1)
        see=self.driver.find_element_by_xpath("//div[@onclick='favourites_delete()'][@class='overlay']")
        see.click()
        time.sleep(2)
        check=self.driver.find_element_by_id("aoi+")
        check.click()
        time.sleep(2)
        delete=self.driver.find_element_by_id('submit_btn')
        delete.click()
        time.sleep(2)
        see=self.driver.find_element_by_xpath("//div[@onclick='favourites_view()'][@class='overlay']")
        see.click()
        time.sleep(2)
        

    def test_filterproject(self):
        dropdown=self.driver.find_element_by_class_name("dropbtn")
        print("found dropdown button")
        dropdown.click()

        print("dropdown opened successfully")
        toggle=self.driver.find_element_by_xpath("//a[@href='/html/favourites']")
        toggle.click()
        time.sleep(3)
        see=self.driver.find_element_by_xpath("//div[@onclick='favourites_project()'][@class='overlay']")
        see.click()
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()