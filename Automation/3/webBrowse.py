from selenium import webdriver
driver = webdriver.Chrome
driver = webdriver.Chrome(r'C:\Users\robin\linkedin\Python Automation\3\chromedriver.exe')
driver.get("https://www.saucedemo.com")
usernameField = driver.find_element_by_xpath('//*[@id="user-name"]')
usernameField.send_keys('standard_user')
passwordField = driver.find_element_by_xpath('//*[@id="password"]')
passwordField.send_keys('secret_sauce')
loginButton = driver.find_element_by_xpath('//*[@id="login-button"]')
loginButton.click()