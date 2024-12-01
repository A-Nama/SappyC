import streamlit as st
import requests

# Backend URLs
GET_POSTS_URL = "http://localhost:5000/get_posts"
GENERATE_COMMENT_URL = "http://localhost:5000/generate_comment"

st.title("LinkedIn Cringe Comment Generator")

st.sidebar.header("Login")
auth_token = st.sidebar.text_input("LinkedIn Auth Token", type="password")

if auth_token:
    headers = {"Authorization": auth_token}
    response = requests.get(GET_POSTS_URL, headers=headers)
    
    if response.status_code == 200:
        posts = response.json().get("posts", [])
        for post in posts:
            st.subheader(f"Post: {post['content']}")
            if st.button(f"Generate Comment for Post {post['id']}"):
                comment_response = requests.post(GENERATE_COMMENT_URL, json={"content": post['content']})
                if comment_response.status_code == 200:
                    comment = comment_response.json().get("comment")
                    st.success(comment)
    else:
        st.error("Failed to fetch posts. Check your token.")

st.sidebar.markdown("### Made with 💻 & 💡")
