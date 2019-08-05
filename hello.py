from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user = "demoassignment7@gmail.com"
pwd = "jaishree123"
driver = webdriver.Chrome(executable_path="/Users/Jaishree.Bawaskar/Desktop/chromedriver_win32/chromedriver.exe")
driver.get('https://www.facebook.com')
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
# driver.close()