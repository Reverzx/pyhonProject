from conftest import driver
from pages.elements_page import AuthorizathionPage
from pages.base_page import BasePage
import time


class TestElements(driver):
    def test_text_box(self, driver):
        text_box_page = AuthorizathionPage(driver, "https://devadmin.aula.city/login")
        text_box_page.open()
        time.sleep(5)

