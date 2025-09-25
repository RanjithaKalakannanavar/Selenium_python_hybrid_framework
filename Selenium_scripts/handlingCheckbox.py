import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
driver =webdriver.Chrome()
driver.maximize_window()
driver.get("https://mail.google.com/")
driver.find_element(By.XPATH,"//input[@type='email']").send_keys("ranjithads.ca@gmail.com")
driver.find_element(By.XPATH,"//span[text()='Next']").click()
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("Thanish@7")
driver.find_element(By.XPATH,"//span[text()='Next']").click()
driver.find_element(By.ID,"gs_lc50").send_keys("solid starts")
driver.find_element(By.ID,"gs_lc50").send_keys(Keys.ENTER)
checkboxes=driver.find_elements()
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
'''.execute_script(...): This method allows you to run raw JavaScript inside the browser that Selenium controls.
"window.scrollTo(0, document.body.scrollHeight);": This is the JavaScript code being executed.
window.scrollTo(x, y): Scrolls the page to a specific location.
x = 0: horizontal scroll is set to the far left.
y = document.body.scrollHeight: vertical scroll is set to the maximum height of the page, which effectively scrolls the page all the way to the bottom.'''
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)
check_count=0
expected_checkCount=driver.coun
for checkbox in checkboxes:
    if checkbox.is_selected():
        check_count+=1
assert check_count.__eq__(expected_checkCount)

