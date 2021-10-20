from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[1]/input')
    first_name.send_keys('xxxxx')
    last_name = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[2]/input')
    last_name.send_keys("xxxxx")
    email = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[3]/input')
    email.send_keys("xxxx")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:

    time.sleep(10)
    browser.quit()




