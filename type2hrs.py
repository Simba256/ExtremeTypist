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

print("Clicked on accept all cookies")
sleep(3)
# sign in
email_xpath = "/html/body/div[10]/main/div[2]/div[4]/form/input[1]"
email_box = driver.find_element("xpath", email_xpath)

password_xpath = "/html/body/div[10]/main/div[2]/div[4]/form/input[2]"
password_box = driver.find_element("xpath", password_xpath)

email = "your_email"
password = "your_password"

email_box.send_keys(email)
password_box.send_keys(password)

sign_in_xpath = "/html/body/div[10]/main/div[2]/div[4]/form/button"
sign_in_button = driver.find_element("xpath", sign_in_xpath)
sign_in_button.click()

sleep(10)

driver.get("https://monkeytype.com/")

sleep(5)

set_time_xpath = "/html/body/div[10]/main/div/div[1]/div/div[5]/button[5]"
set_time_button = driver.find_element("xpath", set_time_xpath)
set_time_button.click()

input_time_xpath = "/html/body/div[9]/dialog[2]/form/input"
input_time_box = driver.find_element("xpath", input_time_xpath)
input_time_box.send_keys("2h")

ok_button_xpath = "/html/body/div[9]/dialog[2]/form/button"
ok_button = driver.find_element("xpath", ok_button_xpath)
ok_button.click()

sleep(3)
print("Here starting:")
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "word")))
# find the div element with class "word" and "active"
# /html/body/div[10]/main/div/div[3]/div[7]/div[4]/div[1]
while 1:
    try:
        word_element = driver.find_element(By.CSS_SELECTOR, "div.word.active")
        pyautogui.typewrite(word_element.text, 0.3)
        pyautogui.press("space")
    except:
        try:
            wpm_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[10]/main/div/div[4]/div[1]/div[1]/div[1]/div[2]")))
            print("Your speed was",wpm_element.text,"wpm")
            break
        except:
            break


sleep(500)
driver.quit()
