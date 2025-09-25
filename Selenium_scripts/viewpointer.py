import time

from selenium import webdriver

# for set multiple view points, so write array
viewpoint=[(123,234),(414,896),(375,667),(768,1025)]
driver =webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo/")
'''driver.set_window_size("678","643")
time.sleep(5)'''
try:
    for width,height in viewpoint:
        driver.set_window_size(width,height)
        time.sleep(5)
finally:
    driver.close()
