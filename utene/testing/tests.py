from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def _logged_session(f):
    def do(self):
        #login
        self.browser.get(self.live_server_url)
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('testuser')
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('testuser')
        password_field.send_keys(Keys.RETURN)
        
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('', body.text)
        
        #function execution
        ret = f(self)
        
        #logout
        self.browser.get(self.live_server_url + '/accounts/logout/')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('You are logged out', body.text)
        return ret

    return do


class TestingTests(LiveServerTestCase):
    
    fixtures = ['utene/fixtures/test_data.json']

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
    
    @_logged_session
    def test_01_can_create_testcase(self):
        # Gertrude opens her web browser, and goes to the admin page
        self.browser.get(self.live_server_url + '/testing/test_cases/')

        # She sees the familiar 'Django administration' heading
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Test Cases', body.text)
        
        #Click to link to create a new test case
        self.browser.find_element_by_id('create_link').click()
        
        # TEXT FIELDS: Titulo, objetivo, tiempo estimado,
        #              pre-post-condiciones, steps
        self.browser.find_element_by_name('title').send_keys('Test Case for testing')
        self.browser.find_element_by_name('title').send_keys('This is my objective')
        self.browser.find_element_by_name('estimated_execution_time').send_keys(60)
        self.browser.find_element_by_name('preconditions-0-description').send_keys("First Pre-Condition")
        self.browser.find_element_by_name('postconditions-0-description').send_keys("First Post-Condition")
        self.browser.find_element_by_name('steps-0-step_number').send_keys(1)
        self.browser.find_element_by_name('steps-0-step_action').send_keys("First Step Action")
        self.browser.find_element_by_name('steps-0-step_expected_result').send_keys("First Step Expected Result")
        self.browser.find_element_by_name('description').send_keys("Revision Desripcion")
        
        self.browser.find_element_by_xpath("//select[@name='test_case_type']/option[value()='U']").click()
        self.browser.find_element_by_xpath("//select[@name='requirement']/option[text()='Requirement Test']").click()
        self.browser.find_element_by_xpath("//select[@name='execution_type']/option[value()='A']").click()
        
        self.browser.find_element_by_id('submit').click()
        
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Test Case for testing', body.text)
        
    
    @_logged_session
    def test_02_can_modify_testcase(self):
        self.browser.get(self.live_server_url + '/testing/test_cases/')

        # She sees the familiar 'Django administration' heading
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Test Cases', body.text)
        
        #Click to link to create a new test case
        self.browser.find_element_by_id('modify_1').click()
        
        self.browser.find_element_by_id('submit').click()
        
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Test Case for testing', body.text)

    
    @_logged_session
    def test_03_can_delete_testcase(self):
        self.browser.get(self.live_server_url + '/testing/test_cases/')

        # She sees the familiar 'Django administration' heading
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Test Cases', body.text)
        
        #Click to link to create a new test case
        self.browser.find_element_by_id('modify_1').click()
        
        self.browser.find_element_by_id('submit').click()
        
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Test Case for testing', body.text)
