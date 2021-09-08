from selenium import webdriver
from getpass import getpass

username = "ruchabhosale96@gmail.com"
password = "pw_IndiaTest!"

driver = webdriver.Chrome("/Users/harshalshelar/Desktop/chromedriver")

driver.get("https://platformrc.wyscout.com/app/")

element = driver.find_element_by_id("login_username")
print(element)
element.send_keys(username)

password_textbox = driver.find_element_by_id("login_password")
print(password_textbox)
password_textbox.send_keys(password)

login_button = driver.find_element_by_id("login_button")
print(login_button)
login_button.submit()

value = driver.execute_script("window.localStorage;")
print(value)
