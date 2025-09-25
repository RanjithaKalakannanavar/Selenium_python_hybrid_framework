from datetime import datetime

import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login_with_valid_credentials(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "input-email").clear()
        self.driver.find_element(By.ID, "input-email").send_keys("ranjithads124@gmail.com")
        self.driver.find_element(By.ID, "input-password").clear()
        self.driver.find_element(By.ID, "input-password").send_keys("Test@1234")
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        self.driver.implicitly_wait(20)
        assert self.driver.find_element(By.LINK_TEXT, "Edit your account information").is_displayed()


    def test_invalid_email_valid_password(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "input-email").clear()
        self.driver.find_element(By.ID, "input-email").send_keys(self.generate_time_stamp())
        self.driver.find_element(By.ID, "input-password").clear()
        self.driver.find_element(By.ID, "input-password").send_keys("Test@1234")
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        self.driver.implicitly_wait(20)
        warning_text = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[contains(@class,'alert-dange')]").text.__contains__(warning_text)


    def test_valid_email_invalid_password(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "input-email").clear()
        self.driver.find_element(By.ID, "input-email").send_keys("ranjithads124@gmail.com")
        self.driver.find_element(By.ID, "input-password").clear()
        self.driver.find_element(By.ID, "input-password").send_keys("Test@123674")
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        self.driver.implicitly_wait(20)
        message = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[contains(@class,'alert-dange')]").text.__eq__(message)


    def test_without_entering_values(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "input-email").clear()
        self.driver.find_element(By.ID, "input-email").send_keys("")
        self.driver.find_element(By.ID, "input-password").clear()
        self.driver.find_element(By.ID, "input-password").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        self.driver.implicitly_wait(20)
        message = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[contains(@class,'alert-dange')]").text.__contains__(message)


    def generate_time_stamp(self):
        time = datetime.now().strftime("%Y:%m:%d %H-%M-%S")
        return 'ranjitha124' + time + '@gmail.com'
