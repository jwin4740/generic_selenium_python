from selenium.webdriver.chrome.webdriver import WebDriver

import os


class GmailCreator(WebDriver):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.BASE_SIGNUP_URL = os.environ.get('BASE_GMAIL_SIGNUP_URL')

    def launch_base(self):
        self.driver.get(self.BASE_SIGNUP_URL)

    # def page_one(self):
    #     gmailCreator = GmailCreator(g.driver)
    #     gmailCreator.launch_base()
    #     firstNameField: WebElement = gmailCreator.driver.find_element(by=By.ID, value='firstName')
    #     lastNameField: WebElement = gmailCreator.driver.find_element(by=By.ID, value='lastName')
    #     userNameField: WebElement = gmailCreator.driver.find_element(by=By.ID, value='username')
    #     passwdField: WebElement = gmailCreator.driver.find_element(by=By.NAME, value='Passwd')
    #     confirmPasswdField: WebElement = gmailCreator.driver.find_element(by=By.NAME, value='ConfirmPasswd')
    #     phoneNumberVerifyField: WebElement = gmailCreator.driver.find_element(by=By.ID, value='phoneNumberId')
    #     firstNameField.send_keys('James')
    #     lastNameField.send_keys('Winkle')
    #     time.sleep(0.5)
    #     userNameField.send_keys('asfasfdsfkjJdjd')
    #     passwdField.send_keys('dkfjgjtu7.$..?fdf')
    #     confirmPasswdField.send_keys('dkfjgjtu7.$..?fdf')

