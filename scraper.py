from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize WebDriver
def linkedin_login(username, password):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.linkedin.com/login")

    time.sleep(2)  # Wait for the page to load

    # Enter username and password
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(2)  # Wait for login to complete
    return driver

# Fetch posts from connections' feeds
def get_connections_posts(driver):
    driver.get("https://www.linkedin.com/feed/")
    time.sleep(3)

    posts = []
    post_elements = driver.find_elements(By.CSS_SELECTOR, ".feed-shared-update-v2")

    for post in post_elements[:5]:  # Limit to 5 posts for now
        try:
            content = post.find_element(By.CSS_SELECTOR, ".feed-shared-update-v2__commentary").text
            posts.append({"content": content})
        except:
            posts.append({"content": "No content available"})

    return posts

# Close WebDriver
def close_driver(driver):
    driver.quit()
