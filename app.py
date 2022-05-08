import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from GenericSelenium import GenericSelenium
from dotenv import load_dotenv

from email_creator.GmailCreator import GmailCreator
from email_creator.ProtonMailCreator import ProtonMailCreator

load_dotenv()
g = GenericSelenium()
proton = ProtonMailCreator(g.driver)
proton.launch_base()
time.sleep(10)
# WebDriverWait(proton.driver, 10).until(lambda x: x.find_element(By.ID, "username"))
userNameField: WebElement = proton.driver.find_element(by=By.ID, value='username')
passwdField: WebElement = proton.driver.find_element(by=By.ID, value='password')
confirmPasswdField: WebElement = proton.driver.find_element(by=By.ID, value='repeat-password')

userNameField.send_keys('asfasfdsfkjJdjd')
passwdField.send_keys('dkfjgjtu7.$..?fdf')
confirmPasswdField.send_keys('dkfjgjtu7.$..?fdf')
