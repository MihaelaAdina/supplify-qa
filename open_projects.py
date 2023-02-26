import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SUPPLIFY_USERNAME = os.environ.get("SUPPLIFY_USERNAME")
SUPPLIFY_PASSWORD = os.environ.get("SUPPLIFY_PASSWORD")

class TestProjects(unittest.TestCase):
    # initialization of webdriver
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1370, 900)
        self.driver.get("https://staging.getchainify.com")

    def go_to_project_card(self, project_title):
        driver = self.driver
        open_new_project = driver.find_element(By.LINK_TEXT, project_title)
        open_new_project.click()

    def login(self):
        driver = self.driver
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/button').click()

        email_address = driver.find_element(By.NAME, "username")
        email_address.send_keys(SUPPLIFY_USERNAME)

        password = driver.find_element(By.NAME, 'password')
        password.send_keys(SUPPLIFY_PASSWORD + Keys.ENTER)
        driver.implicitly_wait(10)

    def accept_cookie_policy(self):
        driver = self.driver
        cookies_button = driver.find_element(By.ID, 'rcc-confirm-button')
        cookies_button.click()

    def input_type_value(self, input_id, value):
        driver = self.driver
        input = driver.find_element(By.ID, input_id)
        input.click()
        input.send_keys(value)

    def edit_input_type_value(self, input_id, value):
        driver = self.driver
        input = driver.find_element(By.ID, input_id)
        input.click()
        input.send_keys(Keys.COMMAND + "a")
        input.send_keys(value)

    def create_project(self):
        driver = self.driver
        add_project = driver.find_element(By.ID, 'add-company')
        add_project.click()
        time.sleep(5)

        page_title = driver.find_element(By.CSS_SELECTOR, 'h3')
        self.assertEqual(page_title.text, "New project")

        details_subtitle = driver.find_element(By.CSS_SELECTOR, 'h4')
        self.assertEqual(details_subtitle.text, 'Details')
        driver.implicitly_wait(10)

        input_name_value = 'TEST123'
        self.input_type_value('name', input_name_value)

        input_description_value = 'TEST AAAAAAAAAAAAAAAAA'
        self.input_type_value('description', input_description_value)

        input_objectives_value = 'none'
        self.input_type_value('objectives', input_objectives_value)

        input_people_value = '14'
        self.input_type_value('nr_people_using_solution', input_people_value)

        input_implementation_value = '2022'
        self.input_type_value('implementation_start_date', input_implementation_value)

        input_geography_value = 'Dubai'
        self.input_type_value('geography', input_geography_value)

        input_budget_value = '200m'
        self.input_type_value('budget_range', input_budget_value)
        time.sleep(5)

        save_button = driver.find_element(By.XPATH,
                                          '//*[@id="__next"]/div[2]/div/div/div/div[1]/form/div[1]/div/button[1]')
        driver.execute_script("arguments[0].click();", save_button)

        toast_notif = driver.find_element(By.ID, 'notistack-snackbar')
        self.assertEqual(toast_notif.text, "Project created successfully!")

        open_projects_title = driver.find_element(By.CSS_SELECTOR, 'h3')
        self.assertEqual(open_projects_title.text, 'Open Leads')

        self.go_to_project_card('TEST123')

        time.sleep(5)

        self.assertTrue(input_name_value in driver.page_source)
        self.assertTrue(input_description_value in driver.page_source)
        self.assertTrue(input_objectives_value in driver.page_source)
        self.assertTrue(input_people_value in driver.page_source)
        self.assertTrue(input_implementation_value in driver.page_source)
        self.assertTrue(input_geography_value in driver.page_source)
        self.assertTrue(input_budget_value in driver.page_source)


    def edit_project(self):
        driver = self.driver
        edit_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/div[1]/div[1]/div/button[1]')
        edit_button.click()

        input_edit_name_value = 'project_name_edit'
        self.edit_input_type_value('name', input_edit_name_value )

        input_edit_description_value = 'description_edited'
        self.edit_input_type_value('description', input_edit_description_value)

        input_edit_objectives_value = 'objectives_edited'
        self.edit_input_type_value('objectives', input_edit_objectives_value)

        input_edit_people_value = 'people_edited'
        self.edit_input_type_value('nr_people_using_solution', input_edit_people_value)

        input_edit_implementation_value = 'implementation_edited'
        self.edit_input_type_value('implementation_start_date', input_edit_implementation_value)

        input_edit_geography_value = 'geography_edited'
        self.edit_input_type_value('geography', input_edit_geography_value)

        input_edit_budget_value = 'budget_edited'
        self.edit_input_type_value('budget_range', input_edit_budget_value)

        save_edit_button = driver.find_element(By.XPATH,
                                               '//*[@id="__next"]/div[2]/div/div/div/div[1]/form/div[1]/div/button[1]')
        save_edit_button.click()
        time.sleep(5)

        toast_notif_edited = driver.find_element(By.XPATH, '//*[@id="notistack-snackbar"]')

        self.assertEqual(toast_notif_edited.text, 'Project updated successfully!')
        self.assertTrue(input_edit_name_value in driver.page_source)
        self.assertTrue(input_edit_description_value in driver.page_source)
        self.assertTrue(input_edit_objectives_value in driver.page_source)
        self.assertTrue(input_edit_people_value in driver.page_source)
        self.assertTrue(input_edit_implementation_value in driver.page_source)
        self.assertTrue(input_edit_geography_value in driver.page_source)
        self.assertTrue(input_edit_budget_value in driver.page_source)

    def test_whatever(self):
        driver = self.driver

        self.login()
        self.accept_cookie_policy()

        open_projects_button = driver.find_element(By.LINK_TEXT, 'Open Leads')
        open_projects_button.click()
        driver.implicitly_wait(10)

        self.create_project()

        highlights_sub_title = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/div[1]/div[4]/div[2]/div/div/div/div[1]/h4')
        self.assertEqual(highlights_sub_title.text, "Highlights")

        main_objectives_presence = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/div[1]/div[4]/div[1]/div/div/div/div[1]/h4')
        self.assertEqual(main_objectives_presence.text, 'Main objectives to accomplish')

        solution_presence = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/div[1]/div[4]/div[2]/div/div/div/div[2]/h2[1]')
        self.assertEqual(solution_presence.text, "How many people would use the solution?")

        budget_presence = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/div[1]/div[4]/div[2]/div/div/div/div[2]/h2[4]')
        self.assertEqual(budget_presence.text, "What is your budget range?")

        self.edit_project()

    # cleanup method called after every test performed
    def tearDown(self):
        self.driver.close()

# execute the script
if __name__ == "__main__":
    unittest.main()