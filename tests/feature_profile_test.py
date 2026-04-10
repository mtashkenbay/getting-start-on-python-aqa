import time

from base.base_test import BaseTest
import random
import allure
import pytest
@allure.feature("Profile Test")
@allure.story("Profile Test")
class TestProfileFeature(BaseTest):
    @allure.title('Profile change test')
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_profile_name(self):
        edited_name = f"edited name {random.randint(1, 100)}"

        self.login_page.open()
        self.login_page.input_username(self.data.USERNAME)
        self.login_page.input_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info()
        self.my_info_page.is_opened()
        self.my_info_page.input_firstname(edited_name)
        self.my_info_page.click_save_button()
        self.my_info_page.check_firstname_field(edited_name)
        self.my_info_page.make_screenshot('make_screenshot.png')