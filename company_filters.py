import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestFilters(unittest.TestCase):

    # initialization of webdriver
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1370, 900)
        self.driver.get("https://staging.getchainify.com")

    def apply_filter(self):
        save_option = self.driver.find_element(By.ID, "Save")
        save_option.click()

    def select_industry_filter(self):
        # get driver
        driver = self.driver

        industries_dropdown = driver.find_element(By.XPATH, '//*[@id="Industries"]/button')
        industries_dropdown.click()
        driver.implicitly_wait(5)

        search_field = driver.find_element(By.XPATH, '//*[@id="fade-menu"]/div[3]/ul/form/div[1]/div/input')
        search_field.click()
        driver.implicitly_wait(5)
        search_field.send_keys('advertising')
        time.sleep(2)

        first_result = driver.find_element(By.XPATH, '//*[@id="fade-menu"]/div[3]/ul/form/div[2]/label/span[1]')
        first_result.click()

        self.apply_filter()

    # Test case method. It should always start with test_
    def test_negative_scenarios(self):
        # get driver
        driver = self.driver

        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/button').click()
        # self.assertEqual(select_searchbar.tag_name, 'input')

        email_address = driver.find_element(By.NAME, "username")
        email_address.send_keys('dailyinspo13@gmail.com')

        password = driver.find_element(By.NAME, 'password')
        password.send_keys('Tik1234tok' + Keys.ENTER)
        driver.implicitly_wait(5)

        results_total_text = driver.find_element(By.XPATH, "//div[@data-testid='companies-found-text']").text

        self.select_industry_filter()

        new_results_total_text = driver.find_element(By.XPATH, "//div[@data-testid='companies-found-text']").text
        self.assertNotEqual(new_results_total_text, results_total_text)

        # select second filter and chose an option
        estimated_revenue = driver.find_element(By.XPATH, '//*[@id="EstimatedRevenue"]/button')
        estimated_revenue.click()
        select_option = driver.find_element(By.XPATH, '//*[@id="fade-menu"]/div[3]/ul/form/div[2]/label[1]/span[1]')
        driver.implicitly_wait(5)
        select_option.click()
        self.apply_filter()
        second_results_total_text = driver.find_element(By.XPATH, "//div[@data-testid='companies-found-text']").text
        self.assertNotEqual(second_results_total_text, select_option)

        delete_filter = driver.find_element(By.ID, "clearAllFilters")
        delete_filter.click()
        time.sleep(5)




    # cleanup method called after every test performed
    def tearDown(self):
        self.driver.close()

# execute the script
if __name__ == "__main__":
    unittest.main()

