from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

# 2. Username field → tag + name attribute
username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")

# 3. Password field → tag + id attribute
password = driver.find_element(By.CSS_SELECTOR, "input#password")

# 4. Login button → tag + type attribute
login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

# 5. Footer link → descendant selector
footer_link = driver.find_element(By.CSS_SELECTOR, "div#page-footer a")

print(username)
print(password)
print(login_btn)
print(footer_link)

driver.quit()