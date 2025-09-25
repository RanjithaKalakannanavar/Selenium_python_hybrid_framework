import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_broken_links():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://jqueryui.com/")
    '''driver.get("https://www.rakuten.ca/")
    driver.find_element(By.ID, "signup-email-input").send_keys("ranjithads124@gmail.com")
    driver.find_element(By.ID, "signup_password").send_keys("Test@1234")
    driver.find_element(By.ID, "subscribed").click()
    driver.find_element(By.ID, "join-now-btn").click()
    title_rakuten = driver.title
    act_rakutentitle = "Shop. Earn. Get Cash Back. | Rakuten Canada"
    assert title_rakuten.__eq__(act_rakutentitle)'''
    all_links=driver.find_elements(By.TAG_NAME,"a")
    print(f"count all links:{len(all_links)}")

    for link in all_links:
        href =link.get_attribute('href')
        response= requests.get(href)
        if response.status_code>=400:
            print(f"broken link :{href} (status code:{response.status_code})")
    driver.quit()



