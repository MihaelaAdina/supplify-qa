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

    def go_to_project_card(self, project_title):
        driver = self.driver
        open_new_project = driver.find_element(By.LINK_TEXT, project_title)
        open_new_project.click()

    def login(self):
        driver = self.driver
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/button').click()

        email_address = driver.find_element(By.NAME, "username")
        email_address.send_keys('dailyinspo13@gmail.com')

        password = driver.find_element(By.NAME, 'password')
        password.send_keys('Tik1234tok' + Keys.ENTER)
        driver.implicitly_wait(10)

    def accept_cookie_policy(self):
        driver = self.driver
        cookies_button = driver.find_element(By.ID, 'rcc-confirm-button')
        cookies_button.click()

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

        name_variable = 'TEST123'
        name_field = driver.find_element(By.ID, 'name')
        name_field.click()
        name_field.send_keys(name_variable)

        description_variable = 'TEST AAAAAAAAAAAAAAAAA'
        description_field = driver.find_element(By.ID, 'description')
        description_field.click()
        description_field.send_keys(description_variable)

        objectives_variable = 'none'
        objectives_field = driver.find_element(By.ID, 'objectives')
        objectives_field.click()
        objectives_field.send_keys(objectives_variable)

        # nu am mai pus send.keys, am creat o variabila si i-am dat atribut valoarea ce va fi introdusa in campuri
        people_variable = '14'
        people_solution_field = driver.find_element(By.ID, 'nr_people_using_solution')
        people_solution_field.click()
        people_solution_field.send_keys(people_variable)

        implementation_variable = '2022'
        implementation_date = driver.find_element(By.ID, 'implementation_start_date')
        implementation_date.click()
        implementation_date.send_keys(implementation_variable)

        geography_variable = 'Dubai'
        geography_field = driver.find_element(By.ID, 'geography')
        geography_field.click()
        geography_field.send_keys(geography_variable)

        budget_variable = '200m'
        budget_range = driver.find_element(By.ID, 'budget_range')
        budget_range.click()
        budget_range.send_keys(budget_variable)
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

        self.assertTrue(name_variable in driver.page_source)
        self.assertTrue(description_variable in driver.page_source)
        self.assertTrue(objectives_variable in driver.page_source)
        self.assertTrue(people_variable in driver.page_source)
        self.assertTrue(implementation_variable in driver.page_source)
        self.assertTrue(geography_variable in driver.page_source)
        self.assertTrue(budget_variable in driver.page_source)

    def edit_project(self):
        driver = self.driver
        edit_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/div[1]/div[1]/div/button[1]')
        edit_button.click()

        project_name_variable = 'project_name_edit'
        project_name_edit = driver.find_element(By.ID, 'name')
        project_name_edit.send_keys(Keys.COMMAND + "a")
        project_name_edit.send_keys(project_name_variable)

        description_edited_variable = 'description_edited'
        description_edited = driver.find_element(By.ID, 'description')
        description_edited.send_keys(Keys.COMMAND + 'a')
        description_edited.send_keys(description_edited_variable)

        objectives_edited_var = 'objectives_edited'
        objectives_edited = driver.find_element(By.ID, 'objectives')
        objectives_edited.send_keys(Keys.COMMAND + 'a')
        objectives_edited.send_keys(objectives_edited_var)

        people_edited_var = 'people_edited'
        people_edited = driver.find_element(By.ID, 'nr_people_using_solution')
        people_edited.send_keys(Keys.COMMAND + 'a')
        people_edited.send_keys(people_edited_var)

        implementation_edited_var = 'implementation_edited'
        implementation_edited = driver.find_element(By.ID, 'implementation_start_date')
        implementation_edited.send_keys(Keys.COMMAND + 'a')
        implementation_edited.send_keys(implementation_edited_var)

        geography_edited_var = 'geography_edited'
        geography_edited = driver.find_element(By.ID, 'geography')
        geography_edited.send_keys(Keys.COMMAND + 'a')
        geography_edited.send_keys(geography_edited_var)

        budget_edited_var = 'budget_edited'
        budget_edited = driver.find_element(By.ID, 'budget_range')
        budget_edited.send_keys(Keys.COMMAND + 'a')
        budget_edited.send_keys(budget_edited_var)

        save_edit_button = driver.find_element(By.XPATH,
                                               '//*[@id="__next"]/div[2]/div/div/div/div[1]/form/div[1]/div/button[1]')
        save_edit_button.click()
        time.sleep(5)

        toast_notif_edited = driver.find_element(By.XPATH, '//*[@id="notistack-snackbar"]')

        self.assertEqual(toast_notif_edited.text, 'Project updated successfully!')
        self.assertTrue(project_name_variable in driver.page_source)
        self.assertTrue(description_edited_variable in driver.page_source)
        self.assertTrue(objectives_edited_var in driver.page_source)
        self.assertTrue(people_edited_var in driver.page_source)
        self.assertTrue(implementation_edited_var in driver.page_source)
        self.assertTrue(geography_edited_var in driver.page_source)
        self.assertTrue(budget_edited_var in driver.page_source)

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