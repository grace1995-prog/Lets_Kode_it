from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from Login_Locators.Login_Locator_Test import Login_Locator_Test


class Login_Page_Test:

    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def email_field(self, email_field):
        enter_email = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Login_Locator_Test.ENTER_EMAIL))
        enter_email.send_keys(email_field)

    def password_field(self, password_field):
        enter_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Login_Locator_Test.ENTER_PASSWORD))
        enter_password.send_keys(password_field)

    def click_button(self):
        button_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Login_Locator_Test.BUTTON))
        button_field.click()
