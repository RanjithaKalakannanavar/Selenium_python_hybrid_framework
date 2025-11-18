import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.login_page import LoginPage
from tests.BaseTest import BaseTest


class TestRegister(BaseTest):
    def register_user(self):
        login_page=LoginPage(self.driver)
        login_page.you_are_on_automation_exercise_page()
        login_page.signup_or_login_link_click()
        login_page.register_for_new_user_is_present()
        login_page.enter_name_for_registration_field("Ranjitha")
        login_page.enter_email_for_registration()
        login_page.click_signup_button_registration()
        login_page.register_to_create_an_account()

        login_page.register_with_valid_details()






