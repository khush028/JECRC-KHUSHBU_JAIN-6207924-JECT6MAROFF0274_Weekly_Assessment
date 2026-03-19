from selenium import webdriver
from time import sleep

# Open browser
driver = webdriver.Chrome()

# List of websites
websites = [
    "https://www.thesouledstore.com",
    "https://www.nike.com",
    "https://www.amazon.in",
    "https://www.bbc.com",
    "https://www.python.org"
]

# Open each website one by one
for site in websites:
    driver.get(site)
    sleep(3)
    print("Title:", driver.title)

# Close browser
driver.quit()