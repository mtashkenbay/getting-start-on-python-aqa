import time

import allure
from base.base_page import BasePage
from config.urls import URLS
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

class MyInfoPage(BasePage):
    PAGE_URL = URLS.MY_INFO

    FIRSTNAME_INPUT = ("xpath","//input[@name='firstName']")
    SAVE_BUTTON = ("xpath","(//button[@type='submit'])[1]")
    SPINNER_CONTAINER = (By.CSS_SELECTOR,'.oxd-loading-spinner-container')
    SPINNER_LOADER = (By.CSS_SELECTOR,'.oxd-loading-spinner')


    def input_firstname(self, new_name):
        with allure.step(f"Change name to '{new_name}'"):
            self.wait.until(
                EC.invisibility_of_element_located(self.SPINNER_LOADER))
            first_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRSTNAME_INPUT))
            first_name_field.send_keys(Keys.COMMAND + "A")
            first_name_field.send_keys(Keys.BACKSPACE)
            first_name_field.send_keys(new_name)
            self.name = new_name

    @allure.step("Click on save button")
    def click_save_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step("Check firstname field")
    def check_firstname_field(self, name):
        self.wait.until(
            EC.invisibility_of_element_located(self.SPINNER_LOADER))
        self.wait.until(
            EC.visibility_of_element_located(self.FIRSTNAME_INPUT))
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRSTNAME_INPUT, name))
