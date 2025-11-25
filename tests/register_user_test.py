import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.login_page import LoginPage
from Pages.register_page import RegisterNewUser
from tests.BaseTest import BaseTest


class TestRegister(BaseTest):
    def test_register_user_with_valid_inputs(self):
        login_page=LoginPage(self.driver)
        register_page= RegisterNewUser(self.driver)
        login_page.you_are_on_automation_exercise_page()
        login_page.signup_or_login_link_click()
        register_page.register_for_new_user_is_present()
        register_page.enter_name_for_registration_field("Ranjitha")
        register_page.enter_email_for_registration()
        register_page.click_signup_button_registration()
        register_page.register_to_create_an_account()
        register_page.register_radio_button()
        register_page.register_with_password("ranjitha@2025Welcome!")
        register_page.register_select_date_of_birth('3','August',"2020")
        register_page.register_newsletter()
        register_page.register_first_name_and_last_name('ranjitha','kalakannanavar')
        register_page.register_company_name('currentlighting')
        register_page.register_first_address('623,raccine avenue')
        register_page.register_second_address('point clair')
        register_page.select_country_from_dropdown('Canada')
        register_page.register_enter_state_city_zipcode_mobile_number('Ontario', "Toronto", 'M4B 3E9', '1234567891')
        register_page.register_create_account()

    def test_register_user_without_selecting_date_of_birth(self):
        login_page = LoginPage(self.driver)
        register_page = RegisterNewUser(self.driver)
        login_page.you_are_on_automation_exercise_page()
        login_page.signup_or_login_link_click()
        register_page.register_for_new_user_is_present()
        register_page.enter_name_for_registration_field("Ranjitha")
        register_page.enter_email_for_registration()
        register_page.click_signup_button_registration()
        register_page.register_to_create_an_account()
        register_page.register_radio_button()
        register_page.register_with_password("ranjitha@2025Welcome!")
        #register_page.register_select_date_of_birth('7', 'August', "2020")
        #register_page.register_newsletter()
        register_page.register_first_name_and_last_name('ranjitha', 'kalakannanavar')
        register_page.register_company_name('currentlighting')
        register_page.register_first_address('623,raccine avenue')
        register_page.register_second_address('point clair')
        register_page.select_country_from_dropdown('Canada')
        register_page.register_enter_state_city_zipcode_mobile_number('Ontario', "Toronto", 'M4B 3E9', '1234567891')
        register_page.register_create_account()

    def test_register_without_selecting_company_address2(self):
        login_page=LoginPage(self.driver)
        register_page= RegisterNewUser(self.driver)
        login_page.you_are_on_automation_exercise_page()
        login_page.signup_or_login_link_click()
        register_page.register_for_new_user_is_present()
        register_page.enter_name_for_registration_field("Ranjitha")
        register_page.enter_email_for_registration()
        register_page.click_signup_button_registration()
        register_page.register_to_create_an_account()
        register_page.register_radio_button()
        register_page.register_with_password("ranjitha@2025Welcome!")
        register_page.register_select_date_of_birth('25','December',"2009")
        register_page.register_newsletter()
        register_page.register_first_name_and_last_name('ranjitha','kalakannanavar')
        #register_page.register_company_name('currentlighting')
        register_page.register_first_address('623,raccine avenue')
        #register_page.register_second_address('point clair')
        register_page.select_country_from_dropdown('Canada')
        register_page.register_enter_state_city_zipcode_mobile_number('Ontario', "Toronto", 'M4B 3E9', '1234567891')
        register_page.register_create_account()

    '''def test_register_user_invalid_input_error_check(self):
        login_page = LoginPage(self.driver)
        register_page = RegisterNewUser(self.driver)
        login_page.you_are_on_automation_exercise_page()
        login_page.signup_or_login_link_click()
        register_page.register_for_new_user_is_present()
        register_page.enter_name_for_registration_field("Ranjitha")
        register_page.enter_email_for_registration()
        register_page.click_signup_button_registration()
        register_page.register_to_create_an_account()
        register_page.register_radio_button()
        register_page.register_with_password("")
        #register_page.register_select_date_of_birth('25', 'December', "2024")
        register_page.register_newsletter()
        register_page.register_first_name_and_last_name('', '')
        register_page.register_company_name('currentlighting')
        register_page.register_first_address('')
        register_page.register_second_address('')
        #register_page.select_country_from_dropdown('')
        register_page.register_enter_state_city_zipcode_mobile_number('', "", '', '')
        register_page.register_create_account()
        register_page.error_message_to_create_account()'''



