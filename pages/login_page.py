import allure
from base.base_page import BasePage
from config.urls import URLS
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    PAGE_URL = URLS.LOGIN_PAGE

    USERNAME_FIELD = ("xpath","//input[@name='username']")
    PASSWORD_FIELD = ("xpath","//input[@name='password']")
    SUBMIT_BUTTON = ("xpath","//button[@type='submit']")

    @allure.step("Enter username")
    def input_username(self,login):
        (self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD))
         .send_keys(login))
    @allure.step("Enter password")
    def input_password(self, password):
        (self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD))
         .send_keys(password))

    @allure.step("Click on submit")
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()