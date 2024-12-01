# scraper.py
import requests
from bs4 import BeautifulSoup
import random

# Your Gemini API Key
GEMINI_API_KEY = "your-gemini-api-key-here"  # Replace with your actual Gemini API key

# Scraping LinkedIn posts (using BeautifulSoup)
def scrape_posts():
    # For demonstration, we're using a random sample of posts from LinkedIn (you can replace this with actual scraping logic)
    # We'll attempt to scrape a few public LinkedIn posts
    urls = [
        "https://www.linkedin.com/feed/hashtag/success/",  # Sample URL
        "https://www.linkedin.com/feed/hashtag/career/",   # Sample URL
    ]

    posts = []
    
    for url in urls:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        # Send a GET request to LinkedIn (this might be blocked by LinkedIn)
        response = requests.get(url, headers=headers)
        
        # Check for successful response
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find post contents (you may need to adapt these selectors to fit actual LinkedIn HTML structure)
            post_elements = soup.find_all('div', class_="feed-shared-update-v2__description")  # Update based on LinkedIn's HTML structure
            for post in post_elements:
                content = post.get_text(strip=True)
                if content:  # Add post to list if content is found
                    posts.append({"content": content})

    # If no posts were scraped, return some mock data (replace with real scraping logic)
    if not posts:
        posts = [
            {"content": "Just got promoted to Senior Developer at XYZ Corp! #grateful #career"},
            {"content": "Feeling so blessed to be part of this amazing project with my team! #teamwork #success"},
            {"content": "Excited to attend the new tech conference next week! #innovation #learning"},
        ]
    
    return random.sample(posts, len(posts))  # Shuffle and return posts

# Function to generate sassy comments using Gemini API
def generate_sassy_comment(post_content):
    # Make an API request to Gemini to generate comments based on post content
    url = "https://api.gemini.com/v1/completion"  # Example endpoint; you may need to replace this based on Gemini docs
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Gemini API prompt (Customize this as needed for your sassy vibe)
    prompt = f"Generate three sassy comments for this LinkedIn post: {post_content}"

    data = {
        "model": "text-davinci-003",  # Example model; check with Gemini documentation for exact model
        "prompt": prompt,
        "max_tokens": 100,
        "n": 3,  # Number of comments to generate
    }
    
    # Send a POST request to Gemini API
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        response_data = response.json()
        comments = [choice['text'].strip() for choice in response_data.get('choices', [])]
        return comments
    else:
        print("Error with Gemini API:", response.status_code)
        return [
            "Wow, look at you go! 🚀 #LivingTheDream",
            "Slaying the career game, love it! 😎🔥",
            "Yassss, CEO energy!! Keep climbing! 👑",
        ]

