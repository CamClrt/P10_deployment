from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver


firefox_options = webdriver.FirefoxOptions()
firefox_options.headless = True
firefox_options.add_argument("--window-size=1920x1080")


class ProductResearchTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_research_product_with_home_buttom(self):
        self.selenium.get("%s%s" % (self.live_server_url, "/"))
        research_input = self.selenium.find_element_by_id("home_search")
        research_input.send_keys("Nutella")
        self.selenium.find_element_by_class_name("btn").click()
