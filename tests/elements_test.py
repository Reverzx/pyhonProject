from conftest import driver
from pages.elements_page import AuthorizathionPage
from pages.base_page import BasePage
import time


class TestElements(driver):
    def test(self, driver):
        page = AuthorizathionPage(driver, "https://devadmin.aula.city/login")
        page.open()
        time.sleep(5)

