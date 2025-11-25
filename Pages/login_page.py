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

    practice_website_xpath = "//h2[contains(normalize-space(),'Full-Fledged practice website ')]"
    signup_login="//a[text()=' Signup / Login']"
    login_to_your_account="//div[@class='login-form']"
    Login_account_email_xpath="//div[@class='login-form']//input[@name='email']"
    login_account_password_xpath="//div[@class='login-form']//input[@name='password']"
    login_account_login_button_xpath="//button[text()='Login']"



    def you_are_on_automation_exercise_page(self):
        automation_exercise = "Full-Fledged practice website for Automation Engineers"
        assert self.driver.find_element(By.XPATH, self.practice_website_xpath).text.__contains__(automation_exercise)
        print(" Welcome to Automation Exercise practice website")

    def signup_or_login_link_click(self):
        self.driver.find_element(By.XPATH, self.signup_login).click()

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
        self.you_are_on_automation_exercise_page()













