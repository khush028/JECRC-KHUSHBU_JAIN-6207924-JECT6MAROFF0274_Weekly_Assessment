# Description
# 1. Write a Python script using Selenium.
# 2. Navigate to https://www.wikipedia.org/
#  3. Find the search input field.
#  4. Find the "English" language.
# 5. Find the main Wikipedia logo image.
# 6. Count how many language links are present in the central block (Hint: inspect the common container and look for tags within it).Use find_elements and print the count.
#  7. Navigate back to the previous page
#  8. Navigate forward.
# 9. Refresh the page.
# 10. Print the final page title.
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.wikipedia.org/")

time.sleep(2)
search_box = driver.find_element(By.ID, "searchInput")
print("Search box found:", search_box)
english_lang = driver.find_element(By.ID, "js-link-box-en")
print("English language found:", english_lang)
logo = driver.find_element(By.CLASS_NAME, "central-featured-logo")
print("Wikipedia logo found")
languages = driver.find_elements(By.CSS_SELECTOR, ".central-featured-lang strong")
print("Total languages in central block:", len(languages))
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
time.sleep(2)
print("Final Page Title:", driver.title)
driver.quit()