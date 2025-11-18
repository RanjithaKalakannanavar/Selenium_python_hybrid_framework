import time
from datetime import datetime
from time import sleep

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self,driver):
        self.driver=driver

 # New user Signup!
    practice_website_xpath = "//h2[contains(normalize-space(),'Full-Fledged practice website ')]"
    signup_login="a[href='/login']"
    sign_up_form_css=".signup-form"
    enter_name_xpath="//input[@name='name']"
    enter_email_address="//div[@class='signup-form']//input[@name='email']"
    signup_button="//button[text()='Signup']"
    account_register_information="//div[@class='login-form']"
    register_radio_button_Mr="//input[@value='Mr']"
    register_radio_button_Mrs="//input[@value='Mrs']"
    register_enter_password="//input[@id='password']"
    date_of_birth_day="//select[@id='days']"
    date_of_birth_month="//select[@id='months']"
    date_of_birth_year="//select[@id='years']"
    sign_up_for_our_newsletter="//input[@id='newsletter']"
    receive_special_offers_from_our_partners= "//label[contains(text(),'Receive special offers from ou')]"

    # Login to your account
    login_to_your_account="//div[@class='login-form']"
    Login_account_email_xpath="//div[@class='login-form']//input[@name='email']"
    login_account_password_xpath="//div[@class='login-form']//input[@name='password']"
    login_account_login_button_xpath="//button[text()='Login']"



    def you_are_on_automation_exercise_page(self):
        automation_exercise = "Full-Fledged practice website for Automation Engineers"
        assert self.driver.find_element(By.XPATH, self.practice_website_xpath).text.__contains__(automation_exercise)
        print(" Welcome to Automation Exercise practice website")


    def signup_or_login_link_click(self):
        self.driver.find_element(By.CSS_SELECTOR, self.signup_login).click()

    def register_for_new_user_is_present(self):
        new_user_signup="New User Signup!"
        assert self.driver.find_element(By.CSS_SELECTOR, self.sign_up_form_css).text.__contains__(new_user_signup)
        print("New User Signup! is displaying")

    def enter_name_for_registration_field(self,name):
       self.driver.find_element(By.XPATH, self.enter_name_xpath).clear()
       self.driver.find_element(By.XPATH, self.enter_name_xpath).send_keys(name)

    def enter_email_for_registration(self):
        self.driver.find_element(By.XPATH, self.enter_email_address).clear()
        self.driver.find_element(By.XPATH, self.enter_email_address).send_keys(self.provide_time_stamp())

    def click_signup_button_registration(self):
        self.driver.find_element(By.XPATH,self.signup_button).click()

    def register_to_create_an_account(self):
        register_account_information="ENTER ACCOUNT INFORMATION"
        assert self.driver.find_element(By.XPATH,self.account_register_information).text.__contains__(register_account_information)
        print("You are on the Account creation page")

    def provide_time_stamp(self):
        utc_time=datetime.now().strftime("%M_%D_%Y%H_%M_%S")
        return 'ranjitha'+utc_time+'@gmail.com'

    def register_with_valid_details(self):
        self.driver.find_element(By.XPATH,self.register_radio_button_Mr).click()
        self.driver.execute_script("window.scrollBy(0,500)")
        self.driver.find_element(By.XPATH,self.register_enter_password).clear()
        self.driver.find_element(By.XPATH,self.register_enter_password).send_keys("12345Test@Welcome")
        sel_day=Select(self.driver.find_element(By.XPATH,self.date_of_birth_day))
        sel_day.select_by_value('3')
        sel_month=Select(self.driver.find_element(By.XPATH, self.date_of_birth_month))
        sel_month.select_by_visible_text('August')
        sel_year=Select(self.driver.find_element(By.XPATH,self.date_of_birth_year))
        sel_year.select_by_value('1992')
        #self.driver.execute_script("arguments[0],ScrollIntoView;",(By.XPATH,self.sign_up_for_our_newsletter))
        self.driver.find_element(By.XPATH,self.sign_up_for_our_newsletter).click()
        self.driver.find_element(By.XPATH, self.receive_special_offers_from_our_partners).click()

    def you_are_on_login_account(self):
        #WebDriverWait(self.driver,10).until(EC.presence_of_element_located(*self.login_to_your_account))
        actual_login_to_your_account = "Login to your account"
        assert self.driver.find_element(By.XPATH, self.login_to_your_account).text.__contains__(actual_login_to_your_account)
        print("Login to your account is available")


    def email_address_for_login_account(self,email_address):
        self.driver.find_element(By.XPATH,self.Login_account_email_xpath).clear()
        self.driver.find_element(By.XPATH,self.Login_account_email_xpath).send_keys(email_address)

    def password_for_login_account(self,password):
        self.driver.find_element(By.XPATH, self.login_account_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.login_account_password_xpath).send_keys(password)

    def login_button_login_account(self):
        #wait=WebDriverWait(self.driver,10).until(EC.presence_of_element_located(*self.login_account_login_button_xpath))
        self.driver.find_element(By.XPATH,self.login_account_login_button_xpath).click()

    def login_to_practice_application(self,email_address,password):
        self.email_address_for_login_account(email_address)
        self.password_for_login_account(password)
        self.login_button_login_account()













