from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class BaseTestCase(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver()
        super(BaseTestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(BaseTestCase, cls).tearDownClass()
        cls.driver.quit()


class TestCasesTestCase(BaseTestCase):
    
    fixtures = 'test_data.json'

    def test(self):
        self.driver.get(self.live_server_url)

    def test_case_create(self):
        self.driver.get(self.live_server_url + '/polls/')
        poll = self.driver.find_element_by_link_text('ShiningPanda is a...')
        poll.click()
        time.sleep(2)    # Should use accurate WebDriverWait
        choices = self.driver.find_elements_by_name('choice')
        self.assertEquals(3, len(choices))
        choices[2].click()
        choices[2].submit()
        lis = self.driver.find_elements_by_tag_name('li')
        self.assertEquals(3, len(lis))
        self.assertEquals('Hosted CI service? -- 0 votes', lis[0].text)
        self.assertEquals('Consulting firm? -- 0 votes', lis[1].text)
        self.assertEquals('Both! -- 1 vote', lis[2].text)
