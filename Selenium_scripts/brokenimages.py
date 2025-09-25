import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_brokenimages():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/broken_images")
    images=driver.find_elements(By.TAG_NAME,"img")
    broken_images=[]
    for image in images:
        src=image.get_attribute('src')
        resp=requests.get(src)
        if resp.status_code!=200:
            broken_images.append(src)

    if broken_images:
        print("list of the broken images")
        for broken_image in broken_images:
            print(broken_images)
    else:
        print("no broken images")