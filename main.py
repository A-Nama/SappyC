# main.py
import streamlit as st
from scraper import scrape_posts, generate_sassy_comment
import random

# Set up a fun title with centered text
st.set_page_config(page_title="SappyC", page_icon="💬", layout="centered")

# Step 1: Welcome message and start button
if 'start' not in st.session_state:
    st.session_state.start = False

if not st.session_state.start:
    st.markdown(
        "<h1 style='text-align: center; color: #ff69b4;'>Welcome to SappyC: Your favorite sappy comment generator for the hellish landscape of LinkedIn! 💀</h1>", 
        unsafe_allow_html=True
    )
    if st.button("START THE CHAOS"):
        st.session_state.start = True
        st.rerun()

# Step 2: Show LinkedIn posts and generate sassy comments after "Start"
if st.session_state.start:
    # Fetch posts using scraper (now using real scraping logic)
    posts = scrape_posts()

    # Randomly select a post to display
    post = random.choice(posts)
    st.subheader(f"Post: {post['content']}")

    # Generate 3 sassy comments
    comments = generate_sassy_comment(post['content'])
    
    # Show the comment options and memes
    memes = [
        "https://i.pinimg.com/originals/a2/84/7a/a2847a02c6c04660d4a0cc1f9cc12a13.jpg",  # meme 1
        "https://i.pinimg.com/originals/39/f1/f9/39f1f9b67cfedfdedb849547b2881c69.jpg",  # meme 2
        "https://i.pinimg.com/originals/8b/cd/4d/8bcd4dcd253a04054c87fd6fa58d9a50.jpg",  # meme 3
    ]
    
    selected_meme = random.choice(memes)
    
    st.write("Here are your sassy comment suggestions:")
    
    for i, comment in enumerate(comments):
        if st.button(f"Comment {i+1}: {comment}"):
            st.session_state.selected_comment = comment
            st.session_state.selected_meme = selected_meme
            st.rerun()

# Step 3: Show the selected meme and comment
if 'selected_comment' in st.session_state:
    st.markdown(
        "<h2 style='text-align: center; color: #ff69b4;'>You chose: {}</h2>".format(st.session_state.selected_comment), 
        unsafe_allow_html=True
    )
    st.image(st.session_state.selected_meme, use_container_width=True)
    st.markdown(
        "<h3 style='text-align: center; color: #ff69b4;'>POST IT IF YOU DARE! 😜🔥</h3>", 
        unsafe_allow_html=True
    )
    if st.button("Retry?"):
        st.session_state.start = False
        st.rerun()
