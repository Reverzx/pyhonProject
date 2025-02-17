from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://parsinger.ru/selenium/3/3.2.4/index.html'
browser = webdriver.Chrome()
browser.get(url)
c = browser.find_element("id", "secret-key-button")
c.click()
print(c.get_attribute("data"))

"""
tom_c = browser.find_element("id", "text1").text
browser.find_element("id", "userInput").send_keys(tom_c)
browser.find_element("id", "checkBtn").click()
tom_answ = browser.find_element("id", "text2").text
time.sleep(10)
"""
time.sleep(10)
browser.quit()

