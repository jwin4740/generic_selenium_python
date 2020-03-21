from GenericSelenium import GenericSelenium

g = GenericSelenium()
g.driver.get("https://github.com/login")
g.login_by_id('jwin4740@gmail.com', '47@Bughouse', 'login_field', 'password')
g.driver.close()
