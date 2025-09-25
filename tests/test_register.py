from datetime import datetime

import pytest
from selenium.webdriver.common.by import By



@pytest.mark.usefixtures("setup_and_teardown")
@pytest.mark.smoke
class TestRegister:

    def test_register_with_mandatory_field (self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        register_account = "Register Account"
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__contains__(register_account)
        self.driver.find_element(By.ID, "input-firstname").send_keys("Kavana145")
        self.driver.find_element(By.ID, "input-lastname").send_keys("premaer")
        self.driver.find_element(By.ID, "input-email").send_keys(self.generate_time_stamp())
        self.driver.find_element(By.ID, "input-telephone").send_keys("1234567896")
        self.driver.find_element(By.ID, "input-password").send_keys("Test@12345")
        self.driver.find_element(By.ID, "input-confirm").send_keys("Test@12345")
        self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        self.driver.implicitly_wait(20)
        success_message = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(success_message)

    #@pytest.mark.skip
    def test_register_all_field(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        register_account = "Register Account"
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__contains__(register_account)
        self.driver.find_element(By.ID, "input-firstname").send_keys("Kavana145")
        self.driver.find_element(By.ID, "input-lastname").send_keys("premaer")
        self.driver.find_element(By.ID, "input-email").send_keys(self.generate_time_stamp())
        self.driver.find_element(By.ID, "input-telephone").send_keys("1234567896")
        self.driver.find_element(By.ID, "input-password").send_keys("Test@12345")
        self.driver.find_element(By.ID, "input-confirm").send_keys("Test@12345")
        self.driver.find_element(By.XPATH, "//label[@class='radio-inline'][1]").click()
        self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        self.driver.implicitly_wait(20)
        success_message = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(success_message)
    #@pytest.mark.xfail
    def test_register_with_same_emialid(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        register_account = "Register Account"
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__contains__(register_account)
        self.driver.find_element(By.ID, "input-firstname").send_keys("Kavana145")
        self.driver.find_element(By.ID, "input-lastname").send_keys("premaer")
        self.driver.find_element(By.ID, "input-email").send_keys("ranjithads1424@gmail.com")
        self.driver.find_element(By.ID, "input-telephone").send_keys("1234567896")
        self.driver.find_element(By.ID, "input-password").send_keys("Test@12345")
        self.driver.find_element(By.ID, "input-confirm").send_keys("Test@12345")
        self.driver.find_element(By.XPATH, "//label[@class='radio-inline'][1]").click()
        self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        self.driver.implicitly_wait(20)
        alrt_message = "Warning: E-Mail Address is already registered!"
        assert self.driver.find_element(By.XPATH, "//div[contains(@class,'alert-danger')]").text.__eq__(alrt_message)
        assert False

    def test_without_entering_anyfield(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        register_account = "Register Account"
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__contains__(register_account)
        self.driver.find_element(By.ID, "input-firstname").send_keys("")
        self.driver.find_element(By.ID, "input-lastname").send_keys("")
        self. driver.find_element(By.ID, "input-email").send_keys("")
        self.driver.find_element(By.ID, "input-telephone").send_keys("")
        self.driver.find_element(By.ID, "input-password").send_keys("")
        self.driver.find_element(By.ID, "input-confirm").send_keys("")
        self.driver.find_element(By.XPATH, "//label[@class='radio-inline'][1]").click()
        self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        self.driver.implicitly_wait(20)
        first_name_error = "First Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-firstname']//parent::div").text.__contains__(
            first_name_error)
        last_name_error = "Last Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-lastname']//parent::div").text.__contains__(
            last_name_error)
        email_error = "E-Mail Address does not appear to be valid!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-email']//parent::div").text.__contains__(email_error)
        telephone_error = "Telephone must be between 3 and 32 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-telephone']//parent::div").text.__contains__(
            telephone_error)
        password_error = "Password must be between 4 and 20 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-password']//parent::div").text.__contains__(password_error)


    def generate_time_stamp(self):
            present_time=datetime.now().strftime("%Y_%M_%D%H_%M_%S")
            return 'premaer'+present_time+'@gmail.com'
