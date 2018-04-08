from selenium import webdriver
from selenium.webdriver.common.keys import Keys

brower=webdriver.Chrome()
brower.get("http://www.python.org")
element=brower.find_element_by_name("q")
element.send_keys("pycon")
element.send_keys(Keys.ENTER)
print(brower.page_source)