


def test_handles_tab():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.rakuten.ca/")
    driver.find_element(By.ID, "signup-email-input").send_keys("ranjithads124@gmail.com")
    driver.find_element(By.ID, "signup_password").send_keys("Test@1234")
    driver.find_element(By.ID, "subscribed").click()
    driver.find_element(By.ID, "join-now-btn").click()
    title_rakuten = driver.title
    act_rakutentitle = "Shop. Earn. Get Cash Back. | Rakuten Canada"
    assert title_rakuten.__eq__(act_rakutentitle)