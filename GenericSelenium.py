from selenium import webdriver
import selenium
import os


class GenericSelenium:

    # TODO: add support for different browsers
    def __init__(self, browser='chrome'):
        self.options = selenium.webdriver.ChromeOptions()
        self.options.accept_untrusted_certs = True
        self.options.assume_untrusted_cert_issuer = True
        # chrome configuration
        # More: https://github.com/SeleniumHQ/docker-selenium/issues/89
        # And: https://github.com/SeleniumHQ/docker-selenium/issues/87
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-impl-side-painting")
        self.options.add_argument("--disable-setuid-sandbox")
        self.options.add_argument("--disable-seccomp-filter-sandbox")
        self.options.add_argument("--disable-breakpad")
        self.options.add_argument("--disable-client-side-phishing-detection")
        self.options.add_argument("--disable-cast")
        self.options.add_argument("--disable-cast-streaming-hw-encoding")
        self.options.add_argument("--disable-cloud-import")
        self.options.add_argument("--disable-popup-blocking")
        self.options.add_argument("--ignore-certificate-errors")
        self.options.add_argument("--disable-session-crashed-bubble")
        self.options.add_argument("--disable-ipv6")
        self.options.add_argument("--allow-http-screen-capture")
        self.options.add_argument("--start-maximized")

        if browser == 'chrome':
            self.driver = webdriver.Chrome(executable_path='drivers/chromedriver')

    def get_driver(self):
        return self.driver

    def login_by_id(self, username, password, username_element, password_element):
        u_element = self.driver.find_element_by_id(username_element)
        p_element = self.driver.find_element_by_id(password_element)
        u_element.send_keys(username)
        p_element.send_keys(password)
