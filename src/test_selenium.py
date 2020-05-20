import time
import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def wait(x):
    time.sleep(x)

class AutomatedTest(unittest.TestCase):
    baseUrl = "http://127.0.0.1:8000/"

    def setUp(self):
        self.driver = Chrome(executable_path='/opt/WebDriver/bin/chromedriver')
        self.driver.get(self.baseUrl)
        # self.driver.maximize_window()

    @unittest.SkipTest
    def test_navBar(self):
        #Arrange
        driver = self.driver

        #Act: click links in NavBar should go to corresponding page
        driver.find_element_by_xpath('//a[contains(text(), "Zero Discrimination")]').click()
        url1 = driver.current_url
        driver.find_element_by_xpath('//a[contains(text(), "Home")]').click()
        url2 = driver.current_url
        driver.find_element_by_xpath('//a[contains(text(), "About Us")]').click()
        url3 = driver.current_url
        driver.find_element_by_xpath('//a[contains(text(), "Partners")]').click()
        url4 = driver.current_url
        driver.find_element_by_xpath('//a[contains(text(), "Contact")]').click()
        url5 = driver.current_url

        #Assert
        self.assertEqual(self.baseUrl, url1, "Click navBar ZeroDiscrimination should go to index page")
        self.assertEqual(self.baseUrl, url2, "Click navBar Home should go to index page")
        self.assertEqual(self.baseUrl + "about/", url3, "Click navBar About Us should go to about page")
        self.assertEqual(self.baseUrl + "rainbow_tick/", url4, "Click navBar About Us should go to rainbow_tick page")
        self.assertEqual(self.baseUrl + "contact/", url5, "Click navBar About Us should go to contact page")

    @unittest.SkipTest
    def test_job_search_with_no_input(self):
        #Arrange
        driver = self.driver
        
        #Act: test search button without filter inputs
        driver.find_element_by_xpath("//input[@type='submit' and @value='Search']").click()
        url1 = driver.current_url

        #Assert
        self.assertEqual(self.baseUrl + "jobs/search-result/?companyname=&loc=", url1, "Click search button to show all job listings")

    @unittest.SkipTest
    def test_job_search_with_location(self):
        #Arrange:
        driver = self.driver

        #Act: 
        input_Location = driver.find_element_by_xpath("//input[@type='text' and @name='loc']")
        input_Location.send_keys('ACT')
        input_Location.send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Xero")]'))).click()
        url1 = driver.current_url
        wait(2)

        #Assert:
        self.assertEqual(self.baseUrl + "company_details/company/xero", url1, "Should navigate to Xero profile page")

    # @unittest.SkipTest
    def test_admin(self):
        #Arrange:
        driver = self.driver

        #Act:
        driver.get(self.baseUrl + "admin/")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text' and @name='username']"))).send_keys('rainbow@anu.edu.au')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password' and @name='password']"))).send_keys('123456')
        wait(1)
        driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
        driver.find_element_by_xpath('//a[contains(text(), "Comments")]').click()
        url1 = driver.current_url
        driver.back()
        driver.find_element_by_xpath('//a[contains(text(), "Companies")]').click()
        url2 = driver.current_url
        driver.back()
        driver.find_element_by_xpath('//a[contains(text(), "Recommendations")]').click()
        url3 = driver.current_url
        driver.back()
        driver.find_element_by_xpath('//a[contains(text(), "Users")]').click()
        url4 = driver.current_url
        driver.back()

        #Assert: 
        self.assertEqual(self.baseUrl + "admin/functions/comments/", url1, "By clicking Comments, should go to list of comments page")
        self.assertEqual(self.baseUrl + "admin/functions/companies/", url2, "By clicking Comments, should go to list of companies page")
        self.assertEqual(self.baseUrl + "admin/functions/recommendations/", url3, "By clicking Comments, should go to list of recommendations page")
        self.assertEqual(self.baseUrl + "admin/functions/users/", url4, "By clicking Comments, should go to list of users page")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()