# ## Task 2
#
# ### Automation script for the following
#
# Open signup page `https://automationexercise.com/signup`
#
# Enter name & email
#
# Select Title (Mr/Mrs) → Radio button
#
# Select checkboxes:
# `Newsletter`
# `Special offers`
#
# Use get_attribute("checked") to verify selection


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)

driver.get('https://automationexercise.com/signup')
driver.maximize_window()

wait = WebDriverWait(driver, 5)
home=wait.until(EC.element_to_be_clickable((By.XPATH,'//i[@class="fa fa-home"]')))
home.click()
sleep(2)

signup=wait.until(EC.element_to_be_clickable((By.XPATH,'//i[@class="fa fa-lock"]')))
signup.click()
sleep(2)

name=driver.find_element(By.XPATH,'//input[@data-qa="signup-name"]')
name.send_keys("abc")
sleep(2)

email=driver.find_element(By.XPATH,'//input[@data-qa="signup-email"]')
email.send_keys("abc@gmail.com")
sleep(2)

submit=wait.until(EC.element_to_be_clickable((By.XPATH,'//button[@data-qa="signup-button"]')))
submit.click()

gender=driver.find_element(By.ID,'id_gender2')
gender.click()
sleep(2)

news=driver.find_element(By.ID,'newsletter')
news.click()
sleep(2)

offer=driver.find_element(By.ID,'optin')
offer.click()
sleep(2)

print(f'Newsletter checked:',news.get_attribute('checked'))
print(f'Offer checked:',offer.get_attribute('checked'))