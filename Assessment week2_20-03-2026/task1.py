## Task 1
from re import search

### Automation script for amazon.com

# Open Amazon
#
# Verify page title and current URL
#
# Locate the category dropdown (next to search bar)
#
# Select "Books" using Select class
#
# Enter "Harry Potter" in search and press Enter
#
# Use explicit wait to wait until results are visible
#
# Get all product titles using find_elements
#
# Print first 5 product names
#
# Click on the first produc
#
# ---


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
driver.get("https://www.amazon.in/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Verify page title and current URL
print(driver.title)
print(driver.current_url)

# Locate the category dropdown (next to search bar)
dropdown = wait.until(EC.presence_of_element_located((By.ID , "searchDropdownBox")))
sleep(2)
select = Select(dropdown)
select.select_by_visible_text("Books")

# Enter"Harry Potter" in search and press Enter
# Use explicit wait to wait until results are visible

search_bar = wait.until(EC.presence_of_element_located((By.ID , "twotabsearchtextbox")))
search_bar.send_keys("Harry Potter" , Keys.ENTER)

# Get all product titles using find_elements

product = wait.until(EC.presence_of_all_elements_located((By.XPATH , '//div[@class = "sg-col-4-of-4 sg-col-20-of-24 s-matching-dir sg-col-16-of-20 sg-col sg-col-12-of-12 sg-col-8-of-8 sg-col-12-of-16"]/descendant::h2')))
# product.click()
for i in product[:5]:
    print(i.text)

# Click on the first product

product[0].click()

driver.quit()