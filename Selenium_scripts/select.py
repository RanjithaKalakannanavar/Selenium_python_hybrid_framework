from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

def test_count_checkbox():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.rakuten.ca/")
    driver.find_element(By.ID,"signup-email-input").send_keys("ranjithads124@gmail.com")
    driver.find_element(By.ID,"signup_password").send_keys("Test@1234")
    driver.find_element(By.ID, "subscribed").click()
    driver.find_element(By.ID,"join-now-btn").click()
    title_rakuten=driver.title
    act_rakutentitle="Shop. Earn. Get Cash Back. | Rakuten Canada"
    assert title_rakuten.__eq__(act_rakutentitle)
    driver.find_element(By.XPATH,"//span[text()='All Stores']").click()
    check_boxs=driver.find_elements(By.XPATH,"//div[contains(@class,'f-bsr f')]//input")
    print(f"Number of checkbox:{len(check_boxs)}")
    count_clickbox =0
    for checkbox in check_boxs:
        checkbox.send_keys(Keys.SPACE)
        if checkbox.is_selected():
            count_clickbox +=1
    assert count_clickbox.__eq__(len(check_boxs))
    return len(check_boxs)