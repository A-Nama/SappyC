import streamlit as st
from content import generate_sassy_comment
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

# Welcome message and start button
if 'start' not in st.session_state:
    st.session_state.start = False

if not st.session_state.start:
    st.markdown("<h1 style='text-align: center; color: #68056d; font-family: 'Orbitron'>SappyC: Piss people off on LinkedIn, one sappy comment at a time! 😈</h1>",unsafe_allow_html=True)
    if st.button("START THE CHAOS"):
        st.session_state.start = True
        st.rerun()

# Allow user to upload their own post
if st.session_state.start:
    st.subheader("Upload your LinkedIn post here:")

    uploaded_post = st.text_area("Enter your LinkedIn post here:")

    if uploaded_post:
        st.session_state.post_content = uploaded_post
    else:
        st.warning("Please enter a LinkedIn post to generate sassy comments.")

    # Button to trigger comment generation
    if uploaded_post and st.button("Generate Comments"):
        comments = generate_sassy_comment(st.session_state.post_content)

        if comments:
            memes = [
                "https://i.imgur.com/pYXEZUx.jpeg",  # meme 1
                "https://i.imgur.com/dexoU4c.jpeg",  # meme 2
                "https://i.imgur.com/HS8s8v8.jpeg",  # meme 3
                "https://i.imgur.com/HItmwIS.jpeg",  # meme 4
                "https://i.imgur.com/eFtAffb.jpeg",  # meme 5
                "https://i.imgur.com/r1m8dN0.jpeg",  # meme 6
            ]
            selected_meme = random.choice(memes)

            st.session_state.comments = comments
            st.session_state.selected_meme = selected_meme
            st.session_state.show_comments = True
            st.rerun()
        else:
            st.error("Failed to generate comments. Please try again.")

# Display comments only if generated
if 'show_comments' in st.session_state and st.session_state.show_comments:
    st.write("Here are your sassy comment suggestions:")

    for i, comment in enumerate(st.session_state.comments):
        if st.button(f"Comment {i+1}: {comment}"):
            st.session_state.selected_comment = comment
            st.session_state.show_comments = False
            st.rerun()

# Show selected meme and comment
if 'selected_comment' in st.session_state:
    st.markdown(
        f"<h2 style='text-align: center; color: #68056d;'>You chose: {st.session_state.selected_comment}</h2>",
        unsafe_allow_html=True
    )
    st.image(st.session_state.selected_meme, use_container_width=True)
    st.markdown(
        "<h3 style='text-align: center; color: #68056d;'>POST IT IF YOU DARE! 😜🔥</h3>",
        unsafe_allow_html=True
    )

    if st.button("Go Back to Homepage"):
        for key in ['comments', 'selected_comment', 'selected_meme', 'show_comments']:
            st.session_state.pop(key, None)
        st.session_state.start = False
        st.rerun()
