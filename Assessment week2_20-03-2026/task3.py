# ## Task 3
#
# ### Automation script for google.com
#
# Open Google
#
# Enter "Selenium Python"
#
# Use explicit wait for suggestions
#
# Capture all suggestions using find_elements
#
# Print them
#
# Click one suggestion


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from unicodedata import category

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
driver.get("https://www.google.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

search_bar = wait.until(EC.presence_of_element_located((By.XPATH , "//textarea[@id='APjFqb']")))
search_bar.send_keys("Selenium Python")

suggestion = wait.until(EC.presence_of_all_elements_located((By.XPATH , '//ul[@role="listbox"]//li//span')))
for items in suggestion:
    print(items.text)

click_item=wait.until(EC.element_to_be_clickable((By.XPATH,'//ul[@role="listbox"]/child::li[4]')))
click_item.click()

driver.quit()