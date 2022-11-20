import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestForms(unittest.TestCase):

    # initialization of webdriver
    def setUp(self):
        self.driver = webdriver.Chrome()

    # Test case method. It should always start with test_
    def test_looking_to_invest(self):
        # get driver
        driver = self.driver
        # get python.org using selenium
        driver.get("https://staging.getchainify.com")

        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/button').click()
        # self.assertEqual(select_searchbar.tag_name, 'input')

        email_address = driver.find_element(By.NAME, "username")
        email_address.send_keys('dailyinspo13@gmail.com')

        password = driver.find_element(By.NAME, 'password')
        password.send_keys('Tik1234tok' + Keys.ENTER)
        driver.implicitly_wait(5)

        looking_invest = driver.find_element(By.ID, "looking-to-invest")
        looking_invest.click()
        self.assertTrue("Looking to invest?" in driver.page_source)

        first_field = driver.find_element(By.NAME, "solution")
        first_field.click()
        first_field.send_keys("accounting")

        second_field = driver.find_element(By.NAME, "funding_round")
        second_field.click()
        second_field.send_keys(2)
        #a = second_field.get_attribute('value')
        self.assertEqual(second_field.get_attribute('value'), "2")

        third_field = driver.find_element(By.NAME, "available_investing_capital")
        third_field.click()
        third_field.send_keys(2.2)

        forth_field = driver.find_element(By.NAME, "kpi")
        third_field.click()
        forth_field.send_keys("Growth in Revenue")

        accept_cookies = driver.find_element(By.XPATH, '//*[@id="rcc-confirm-button"]')
        accept_cookies.click()

        fifth_field = driver.find_element(By.NAME, "startup_revenue")
        fifth_field.click()
        fifth_field.send_keys("500")
        self.assertEqual(fifth_field.get_attribute('value'), "500")

        sixth_field = driver.find_element(By.NAME, "startup_clients")
        sixth_field.click()
        sixth_field.send_keys("Whales")

        seventh_field = driver.find_element(By.NAME, "startup_industry")
        seventh_field.click()
        seventh_field.send_keys("corporate law")

        eight_field = driver.find_element(By.NAME, "startup_constraints")
        eight_field.click()
        eight_field.send_keys("no")

        tenth_field = driver.find_element(By.NAME, "geographic_interests")
        tenth_field.click()
        tenth_field.send_keys("Zurich")

        submit_button = driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/div/div/div/form/div/div/div[3]/button")
        submit_button.click()

    def test_need_tech_solution(self):
        # get driver
        driver = self.driver
        # get python.org using selenium
        driver.get("https://staging.getchainify.com")

        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/button').click()
        # self.assertEqual(select_searchbar.tag_name, 'input')

        email_address = driver.find_element(By.NAME, "username")
        email_address.send_keys('dailyinspo13@gmail.com')

        password = driver.find_element(By.NAME, 'password')
        password.send_keys('Tik1234tok' + Keys.ENTER)
        driver.implicitly_wait(5)

        looking_invest = driver.find_element(By.ID, "looking-to-invest")
        looking_invest.click()
        self.assertTrue("Looking to invest?" in driver.page_source)

        first_field = driver.find_element(By.NAME, "solution")
        first_field.click()
        first_field.send_keys("accounting")

        second_field = driver.find_element(By.NAME, "funding_round")
        second_field.click()
        second_field.send_keys(2)
        #a = second_field.get_attribute('value')
        self.assertEqual(second_field.get_attribute('value'), "2")

        third_field = driver.find_element(By.NAME, "available_investing_capital")
        third_field.click()
        third_field.send_keys(2.2)

        forth_field = driver.find_element(By.NAME, "kpi")
        third_field.click()
        forth_field.send_keys("Growth in Revenue")

        accept_cookies = driver.find_element(By.XPATH, '//*[@id="rcc-confirm-button"]')
        accept_cookies.click()

        fifth_field = driver.find_element(By.NAME, "startup_revenue")
        fifth_field.click()
        fifth_field.send_keys("500")
        self.assertEqual(fifth_field.get_attribute('value'), "500")

        sixth_field = driver.find_element(By.NAME, "startup_clients")
        sixth_field.click()
        sixth_field.send_keys("Whales")

        seventh_field = driver.find_element(By.NAME, "startup_industry")
        seventh_field.click()
        seventh_field.send_keys("corporate law")

        eight_field = driver.find_element(By.NAME, "startup_constraints")
        eight_field.click()
        eight_field.send_keys("no")

        tenth_field = driver.find_element(By.NAME, "geographic_interests")
        tenth_field.click()
        tenth_field.send_keys("Zurich")

        submit_button = driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/div/div/div/form/div/div/div[3]/button")
        submit_button.click()

    # cleanup method called after every test performed
    def tearDown(self):
        self.driver.close()

# execute the script
if __name__ == "__main__":
    unittest.main()

