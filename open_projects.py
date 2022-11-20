import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestProjects(unittest.TestCase):

    # initialization of webdriver
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1370, 900)
        self.driver.get("https://staging.getchainify.com")

    def open_new_project(self):
        driver = self.driver
        open_new_project = driver.find_element(By.LINK_TEXT, 'TEST123')
        open_new_project.click()

    def test_whatever(self):
        # get driver
        driver = self.driver

        # login
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/button').click()
        # self.assertEqual(select_searchbar.tag_name, 'input')

        email_address = driver.find_element(By.NAME, "username")
        email_address.send_keys('dailyinspo13@gmail.com')

        password = driver.find_element(By.NAME, 'password')
        password.send_keys('Tik1234tok' + Keys.ENTER)
        driver.implicitly_wait(10)

        open_projects_button = driver.find_element(By.LINK_TEXT, 'Open projects')
        open_projects_button.click()

        add_project = driver.find_element(By.ID, 'add-company')
        add_project.click()
        time.sleep(5)
        page_title = driver.find_element(By.CSS_SELECTOR, 'h3')
        self.assertEqual(page_title.text, "New project", "Title is wrong")
        # self.assertTrue("New project" in driver.page_source)

        details_subtitle = driver.find_element(By.CSS_SELECTOR, 'h4')
        self.assertEqual(details_subtitle.text, 'Details')
        driver.implicitly_wait(10)

        cookies_button = driver.find_element(By.ID, 'rcc-confirm-button')
        cookies_button.click()

        name_var = 'TEST123'
        name_field = driver.find_element(By.ID, 'name')
        name_field.click()
        name_field.send_keys(name_var)

        description_field = driver.find_element(By.ID, 'description')
        description_field.click()
        description_field.send_keys('TEST AAAAAAAAAAAAAAAAA')

        objectives_field = driver.find_element(By.ID, 'objectives')
        objectives_field.click()
        objectives_field.send_keys('none')

        people_solution_field = driver.find_element(By.ID, 'nr_people_using_solution')
        people_solution_field.click()
        people_solution_field.send_keys('14')

        implementation_date = driver.find_element(By.ID, 'implementation_start_date')
        implementation_date.click()
        implementation_date.send_keys('2022')

        geography_field = driver.find_element(By.ID, 'geography')
        geography_field.click()
        geography_field.send_keys('Dubai')

        budget_range = driver.find_element(By.ID, 'budget_range')
        budget_range.click()
        budget_range.send_keys('200m')
        time.sleep(5)

        save_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/div[1]/form/div[1]/div/button[1]')
        driver.execute_script("arguments[0].click();", save_button)

        toast_notif = driver.find_element(By.ID, 'notistack-snackbar')
        self.assertEqual(toast_notif.text, "Project created successfully!")


        open_projects_title = driver.find_element(By.CSS_SELECTOR, 'h3')
        self.assertEqual(open_projects_title.text, 'Open projects')

        open_new_project = driver.find_element(By.LINK_TEXT, 'TEST123')
        open_new_project.click()

        # edit_project = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/div[1]/div[1]/div/button[1]')
        # assert here
        # driver.back()
        time.sleep(5)

        # self.open_new_project()

        # submit_solution = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/div[1]/div[1]/div/button[2]')
        # submit_solution.click()
        # driver.back()

        self.assertTrue(name_var in driver.page_source)
        

















        # name_field = driver.find_element(By.ID, "name")
        # name_field.click()
        # time.sleep(5)




    # cleanup method called after every test performed
    def tearDown(self):
        self.driver.close()

# execute the script
if __name__ == "__main__":
    unittest.main()