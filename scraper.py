from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import random

def get_random_linkedin_posts():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    driver.get("https://www.linkedin.com/feed/")
    
    # Simulate user browsing behavior
    post_contents = []
    try:
        post_elements = driver.find_elements(By.CSS_SELECTOR, ".feed-shared-update-v2__commentary")
        for post in random.sample(post_elements, 5):  # Random 5 posts
            post_contents.append(post.text)
    except Exception as e:
        print(f"Error scraping posts: {e}")
    finally:
        driver.quit()

    return post_contents
