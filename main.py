import streamlit as st
from scraper import get_random_linkedin_posts
import requests

# Gemini API URL (mocked, replace with real endpoint)
GEMINI_API_URL = "https://api.example.com/generate-comment"

st.title("💬 SappyC: The Ultimate Sassy Comment Generator")
st.markdown("### Piss people off, one sappy comment at a time 🚀")

# Step 1: Fetch random LinkedIn posts
if st.button("Get Random LinkedIn Posts"):
    st.info("Fetching random posts...")
    posts = get_random_linkedin_posts()
    
    if posts:
        for idx, post in enumerate(posts):
            st.subheader(f"Post #{idx+1}")
            st.write(post)

            if st.button(f"Generate Comments for Post #{idx+1}", key=idx):
                response = requests.post(GEMINI_API_URL, json={"content": post})
                if response.status_code == 200:
                    suggestions = response.json().get("comments", [])
                    st.write("**Sappy Suggestions:**")
                    for comment in suggestions:
                        st.write(f"- {comment}")
                else:
                    st.error("Failed to generate comments.")
    else:
        st.error("Couldn't fetch posts. Try again.")
