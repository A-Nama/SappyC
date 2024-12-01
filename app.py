from flask import Flask, request, jsonify
from linkedin_api import Linkedin

app = Flask(__name__)

# Login with LinkedIn credentials (hardcoded for simplicity, can be environment variables in production)
LINKEDIN_USERNAME = "your-email@example.com"
LINKEDIN_PASSWORD = "your-password"
linkedin = Linkedin(LINKEDIN_USERNAME, LINKEDIN_PASSWORD)

@app.route('/get_posts', methods=['GET'])
def get_posts():
    try:
        # Get user token from frontend (if token-based setup needed later)
        user_token = request.headers.get('Authorization')

        # Simulate fetching posts from the user's feed
        user_profile = linkedin.get_profile(LINKEDIN_USERNAME)  # Retrieve user profile to verify
        posts = linkedin.get_feed_updates(limit=5)  # Fetch the latest 5 posts from feed
        
        response = {
            "posts": [
                {"id": post['entityUrn'], "content": post.get('commentary', 'No Content')}
                for post in posts
            ]
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/generate_comment', methods=['POST'])
def generate_comment():
    data = request.json
    post_content = data.get('content')

    # Simulate GPT-Generated comment
    comment = f"This is so inspiring! 🚀🔥 - [Auto-comment on: {post_content}]"
    return jsonify({"comment": comment})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
