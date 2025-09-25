from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_iframe():
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")
    time.sleep(3) # Give time for the page to load

    # --- Switching to an iframe ---

    # Method 1: Using the iframe's name or ID (if available)
    # driver.switch_to.frame("packageListFrame")

    # Method 2: Using the iframe's index (0-based)
    # driver.switch_to.frame(0)

    # Method 3: Using a WebElement for the iframe (most robust)
    try:
        # Find the iframe element
        iframe_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "packageListFrame")) # Or By.ID, By.XPATH, By.CSS_SELECTOR #
         )
        driver.switch_to.frame(iframe_element)

        # Now you can interact with elements inside the iframe
        # For example, click a link inside the iframe
        link_inside_iframe = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "org.openqa.selenium.opera"))
        )
        link_inside_iframe.click()
        print("Clicked element inside iframe.")

    except Exception as e:
        print(f"Error switching to or interacting with iframe: {e}")

    # --- Switching back to the main content or parent frame ---

    # To switch back to the main document (default content)
    driver.switch_to.default_content()
    print("Switched back to default content.")

    # If you need to switch to a parent iframe from a nested iframe
    # driver.switch_to.parent_frame()

    # Close the browser
    driver.quit()