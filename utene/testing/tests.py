from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PollsTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
        
    def _logged_session(f):
        def do(self):
            #login
            self.browser.get(self.live_server_url)
            username_field = self.browser.find_element_by_name('username')
            username_field.send_keys('testuser')
            password_field = self.browser.find_element_by_name('password')
            password_field.send_keys('testuser')
            password_field.send_keys(Keys.RETURN)
            
            #function execution
            ret = f(self)
            
            #logout
            self.browser.get(self.live_server_url + '/accounts/logout/')
            body = self.browser.find_element_by_tag_name('body')
            self.assertIn('You are logged out', body.text)
            return ret

        return do


    @_logged_session
    def test_can_create_testcase(self):
        # Gertrude opens her web browser, and goes to the admin page
        self.browser.get(self.live_server_url + '/testing/test_cases/')

        # She sees the familiar 'Django administration' heading
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Test Cases', body.text)
    
    def test_can_modify_testcase(self):
        # TODO: modify testcase test
        pass
    
    def test_can_delete_testcase(self):
        # TODO: delete testcase
        pass