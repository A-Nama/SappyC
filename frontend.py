import streamlit as st
import requests

# Backend URLs
LOGIN_URL = "http://localhost:5000/login"
GET_POSTS_URL = "http://localhost:5000/get_posts"
GENERATE_COMMENT_URL = "http://localhost:5000/generate_comment"

st.title("Welcome to SappyC: LinkedIn Sappy Comment Service")

# Sidebar for login
st.sidebar.header("Login")
username = st.sidebar.text_input("LinkedIn Username")
password = st.sidebar.text_input("LinkedIn Password", type="password")

if st.sidebar.button("Log In"):
    login_response = requests.post(LOGIN_URL, json={"username": username, "password": password})
    if login_response.status_code == 200:
        st.sidebar.success("Login successful!")
    else:
        st.sidebar.error("Login failed: " + login_response.json().get("error"))

# Fetch and display posts if logged in
if username and password:
    posts_response = requests.post(GET_POSTS_URL, json={"username": username})
    if posts_response.status_code == 200:
        posts = posts_response.json().get("posts", [])
        for post in posts:
            st.subheader(f"Post: {post['content']}")
            if st.button(f"Generate Comments for Post {post['id']}"):
                comment_response = requests.post(GENERATE_COMMENT_URL, json={"content": post['content']})
                if comment_response.status_code == 200:
                    comments = comment_response.json().get("comments", [])
                    for i, comment in enumerate(comments):
                        st.radio(f"Choose comment {i+1}:", [comment], index=0)
                else:
                    st.error("Failed to generate comments.")
    else:
        st.error("Failed to fetch posts. Please log in again.")
