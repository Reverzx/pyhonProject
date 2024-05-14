from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

#Options
chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = 'normal'
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--window-size=1920,1080')
service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)
# Создание объекта WebDriverWait с веб-драйвером и временем ожидания 10 секунд
wait = WebDriverWait(driver, 10)

#open page
driver.get('https://devadmin.aula.city/login')
#Ввод номера телефона
phone_field = driver.find_element(By.XPATH, '//input[@id="phone"]')
phone_field.send_keys('+7-771-578-63-50')
#Ввод_пароля
password_field = driver.find_element(By.XPATH, "//input[@name='password']")
password_field.send_keys('3125')
#Вход в систему
enter_in_system = driver.find_element(By.XPATH, '//button[@id="submit"]')
enter_in_system.click()
#Открыть фильтр
open_filter = wait.until(ec.presence_of_element_located((By.XPATH, '//button[contains(@class, "no-uppercase")]')))
open_filter.click()
#Выбрать статус заявки
find_status = wait.until(ec.presence_of_element_located((By.XPATH, '//input[@placeholder="Выберите статус заявки"]')))
open_status = driver.find_element(By.XPATH, '(//div[@class="v-input__icon v-input__icon--append"])[5]')
open_status.click()
#Выбрать новые заявки
new_request = driver.find_element(By.XPATH, '(//span[@class="checkbox-square"])[1]')
new_request.click()

try:
    button = driver.find_element(By.XPATH, '//div[@aria-selected="true"]')
except NoSuchElementException:
    print("Test.py failed")
#Выбрать первую заявку и вернуться обратно на страницу
find_status = wait.until(ec.presence_of_element_located((By.XPATH, '//div[@aria-selected="true"]')))
select_first_request = driver.find_element(By.XPATH, '(//td[@class="text-start"])[1]')
select_first_request.click()
driver.back()

try:
    button = driver.find_element(By.XPATH, '//i[@class="v-icon notranslate mdi mdi-checkbox-marked theme--light"]')
    print("Test.py successful")
except NoSuchElementException:
    print("Test.py failed")
