from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pyautogui
driver = webdriver.Chrome()

driver.get("https://monkeytype.com/login")

# click on accept all button
accept_all_cookies_xpath = "/html/body/div[9]/dialog[2]/div[2]/div[2]/div[2]/button[1]"
accept_all_cookies_button = driver.find_element("xpath", accept_all_cookies_xpath)
accept_all_cookies_button.click()

# sign in
email_xpath = "/html/body/div[10]/main/div[2]/div[4]/form/input[1]"
email_box = driver.find_element("xpath", email_xpath)

password_xpath = "/html/body/div[10]/main/div[2]/div[4]/form/input[2]"
password_box = driver.find_element("xpath", password_xpath)

email = "your_username"
password = "your_password"

email_box.send_keys(email)
password_box.send_keys(password)

sign_in_xpath = "/html/body/div[10]/main/div[2]/div[4]/form/button"
sign_in_button = driver.find_element("xpath", sign_in_xpath)
sign_in_button.click()

sleep(10)

driver.get("https://monkeytype.com/")

element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "word")))

while True:
    try:
        word_element = driver.find_element(By.CSS_SELECTOR, "div.word.active")
        pyautogui.typewrite(word_element.text)
        pyautogui.press("space")
    except:
        break

print("You can screenshot your result now")
sleep(100)
driver.quit()
