from selenium.webdriver.common.by import By


class AuthorizathionnPageLocators:
    # form field

    PHONE_NUMBER = (By.XPATH, '//input[@id="phone"]')
    PASSWORD = (By.XPATH, "//input[@name='password']")
    SUBMIT = (By.XPATH, '//button[@id="submit"]')