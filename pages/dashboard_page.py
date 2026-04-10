import allure
from base.base_page import BasePage
from config.urls import URLS
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage(BasePage):
    PAGE_URL = URLS.DASHBOARD_PAGE
    MY_INFO_SPAN = ('xpath', "//span[text()='My Info']")

    @allure.step("Click on My Info")
    def click_my_info(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_INFO_SPAN)).click()