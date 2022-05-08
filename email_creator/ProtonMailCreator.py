from selenium.webdriver.chrome.webdriver import WebDriver

import os


class ProtonMailCreator(WebDriver):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.BASE_SIGNUP_URL = os.environ.get('BASE_SIGNUP_URL_PROTON')

    def launch_base(self):
        self.driver.get(self.BASE_SIGNUP_URL)
