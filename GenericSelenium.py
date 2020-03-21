from selenium import webdriver


class GenericSelenium:

    # TODO: add support for different browsers
    def __init__(self, browser='chrome'):
        if browser == 'chrome':
            self.driver = webdriver.Chrome(executable_path='drivers/chromedriver')

    def get_driver(self):
        return self.driver

    def login_by_id(self, username, password, username_element, password_element):
        u_element = self.driver.find_element_by_id(username_element)
        p_element = self.driver.find_element_by_id(password_element)
        u_element.send_keys(username)
        p_element.send_keys(password)
