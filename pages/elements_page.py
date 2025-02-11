from locators.elements_page_locators import AuthorizathionnPageLocators

from pages.base_page import BasePage


class AuthorizathionPage(BasePage):
    locators = AuthorizathionnPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.PHONE_NUMBER).send_keys('+7-771-578-63-50')
        self.element_is_visible(self.locators.PASSWORD).send_keys('3125')
        self.element_is_visible(self.locators.SUBMIT).click()
