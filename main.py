# main.py
import streamlit as st
from scraper import scrape_posts, generate_sassy_comment
import random

# Set up a fun title with centered text
st.set_page_config(page_title="SappyC", page_icon="💬", layout="centered")

# Add a background image using CSS
st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://i.imgur.com/QTmfJ5w.jpeg");
            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


# Step 1: Welcome message and start button
if 'start' not in st.session_state:
    st.session_state.start = False

if not st.session_state.start:
    st.markdown(
        "<h1 style='text-align: center; color: #ff69b4;'>SappyC: Piss people off on LinkedIn, one sappy comment at a time! 💀</h1>", 
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
        "https://i.imgur.com/pYXEZUx.jpeg",  # meme 1
        "https://i.imgur.com/dexoU4c.jpeg",  # meme 2
        "https://i.imgur.com/HS8s8v8.jpeg",  # meme 3
        "https://i.imgur.com/HItmwIS.jpeg", # meme 4
        "https://i.imgur.com/eFtAffb.jpeg", # meme 5
        "https://i.imgur.com/r1m8dN0.jpeg", # meme 6
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
        st.session_state.pop('selected_comment', None)
        st.session_state.pop('selected_meme', None)
        st.session_state.start = False  # Reset to the start screen
        st.rerun()
