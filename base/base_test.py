import pytest
from config.data import Data
from pages.login_page import LoginPage
from pages.my_info_page import MyInfoPage
from pages.dashboard_page import DashboardPage

class BaseTest:
    data: Data
    login_page: LoginPage
    my_info_page: MyInfoPage
    dashboard_page: DashboardPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.login_page = LoginPage(driver)
        request.cls.my_info_page = MyInfoPage(driver)
        request.cls.dashboard_page = DashboardPage(driver)