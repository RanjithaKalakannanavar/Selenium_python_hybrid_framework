import pytest

from Pages.login_page import LoginPage
from tests.BaseTest import BaseTest
from utilities import Excel_data


class TestLogin(BaseTest):
    @pytest.mark.parametrize("email_address,password",Excel_data.get_data_from_excel("ExcelFiles/Data-driven-testing.xlsx","LoginTest"))
    def test_login(self,email_address,password):
        login_page=LoginPage(self.driver)
        login_page.you_are_on_automation_exercise_page()
        login_page.signup_or_login_link_click()
        login_page.you_are_on_login_account()
        login_page.login_to_practice_application(email_address,password)
        login_page.you_are_on_automation_exercise_page()



