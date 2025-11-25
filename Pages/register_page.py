import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterNewUser:
    def __init__(self, driver):
        self.driver=driver

    enter_name_xpath = "//input[@name='name']"
    enter_email_address = "//div[@class='signup-form']//input[@name='email']"
    signup_button = "//button[text()='Signup']"
    sign_up_form_xpath = "//div[@class='signup-form']"
    account_register_information = "//div[@class='login-form']"
    register_account_information_xpath="//form[@action='/signup']"
    register_radio_button_Mr = "//input[@value='Mr']"
    register_radio_button_Mrs = "//input[@value='Mrs']"
    register_enter_password = "//input[@id='password']"
    date_of_birth_day = "//select[@id='days']"
    date_of_birth_month = "//select[@id='months']"
    date_of_birth_year = "//select[@id='years']"
    sign_up_for_our_newsletter_xpath = "//input[@id='newsletter']"
    receive_special_offers_from_our_partners = "//label[contains(text(),'Receive special offers from ou')]"
    register_first_name_id="first_name"
    register_last_name_id="last_name"
    register_company_id="company"
    register_first_address_id="address1"
    register_second_address_id="address2"
    register_country_id="country"
    register_state_id="state"
    register_city_id="city"
    register_zipcode_id="zipcode"
    register_mobile_number_id="mobile_number"
    register_create_account_button_xpath="//button[text()='Create Account']"



    def register_for_new_user_is_present(self):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.sign_up_form_xpath)))
        new_user_signup="New User Signup!"
        assert self.driver.find_element(By.XPATH, self.sign_up_form_xpath).text.__contains__(new_user_signup)
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

    def register_radio_button(self):
        self.driver.find_element(By.XPATH, self.register_radio_button_Mr).click()

    def register_with_password(self,password):
        self.driver.execute_script("window.scrollBy(0,500)")
        self.driver.find_element(By.XPATH,self.register_enter_password).clear()
        self.driver.find_element(By.XPATH,self.register_enter_password).send_keys(password)

    def register_select_date_of_birth(self,day,month,year):
        sel_day=Select(self.driver.find_element(By.XPATH,self.date_of_birth_day))
        sel_day.select_by_value(day)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.date_of_birth_month)))
        sel_month=Select(self.driver.find_element(By.XPATH, self.date_of_birth_month))
        sel_month.select_by_visible_text(month)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.date_of_birth_year)))
        sel_year=Select(self.driver.find_element(By.XPATH,self.date_of_birth_year))
        sel_year.select_by_value(year)
        #self.driver.execute_script("arguments[0],ScrollIntoView;",(By.XPATH,self.sign_up_for_our_newsletter))

    def register_newsletter(self):
        self.driver.find_element(By.XPATH,self.sign_up_for_our_newsletter_xpath).click()
        self.driver.find_element(By.XPATH, self.receive_special_offers_from_our_partners).click()

    def register_first_name_and_last_name(self,first_name,last_name):
        self.driver.find_element(By.ID, self.register_first_name_id).clear()
        self.driver.find_element(By.ID, self.register_first_name_id).click()
        self.driver.find_element(By.ID,self.register_first_name_id).send_keys(first_name)
        self.driver.find_element(By.ID, self.register_last_name_id).clear()
        self.driver.find_element(By.ID, self.register_last_name_id).click()
        self.driver.find_element(By.ID, self.register_last_name_id).send_keys(last_name)

    def register_company_name(self,company):
        self.driver.find_element(By.ID,self.register_company_id).clear()
        self.driver.find_element(By.ID, self.register_company_id).click()
        self.driver.find_element(By.ID, self.register_company_id).send_keys(company)
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,self.register_second_address_id)))
        self.driver.execute_script("window.scrollBy(0,700);")

    def register_first_address(self,first_address):
        self.driver.execute_script("window.scrollBy(0,700);")
        self.driver.find_element(By.ID, self.register_first_address_id).clear()
        self.driver.find_element(By.ID, self.register_first_address_id).click()
        self.driver.find_element(By.ID, self.register_first_address_id).send_keys(first_address)

    def register_second_address(self,second_address):
        self.driver.find_element(By.ID,self.register_second_address_id).clear()
        self.driver.find_element(By.ID,self.register_second_address_id).click()
        self.driver.find_element(By.ID, self.register_second_address_id).send_keys(second_address)

    def select_country_from_dropdown(self,country):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID, self.register_country_id)))
        #self.driver.find_element(By.ID, self.register_country_id).click()
        sel_country=Select(self.driver.find_element(By.ID, self.register_country_id))
        sel_country.select_by_value(country)
        self.driver.execute_script("window.scrollBy(0,1000);")

    def register_enter_state_city_zipcode_mobile_number(self,state,city,zipcode,mobile_number):
        self.driver.find_element(By.ID,self.register_state_id).clear()
        self.driver.find_element(By.ID,self.register_state_id).click()
        self.driver.find_element(By.ID, self.register_state_id).send_keys(state)
        self.driver.find_element(By.ID, self.register_city_id).clear()
        self.driver.find_element(By.ID, self.register_city_id).click()
        self.driver.find_element(By.ID, self.register_city_id).send_keys(city)
        self.driver.find_element(By.ID, self.register_zipcode_id).clear()
        self.driver.find_element(By.ID, self.register_zipcode_id).click()
        self.driver.find_element(By.ID, self.register_zipcode_id).send_keys(zipcode)
        self.driver.find_element(By.ID, self.register_mobile_number_id).clear()
        self.driver.find_element(By.ID, self.register_mobile_number_id).click()
        self.driver.find_element(By.ID, self.register_mobile_number_id).send_keys(mobile_number)

    def register_create_account(self):
        self.driver.execute_script("window.scrollBy(0,1300);")
        self.driver.find_element(By.XPATH, self.register_create_account_button_xpath).click()

    def error_message_to_create_account(self):
        actual_error_message = "Please fill out this field"
        error = self.driver.find_element(By.XPATH, "//p[contains(text(), 'Street address')]")
        print(error.text)
        #print("Please fill out this field error message displaying")






