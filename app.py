from flask import Flask, request, jsonify
from linkedin_api import Linkedin

app = Flask(__name__)

# Store active LinkedIn sessions (username as key)
active_sessions = {}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    try:
        # Authenticate with LinkedIn
        linkedin = Linkedin(username, password)
        active_sessions[username] = linkedin  # Save session in memory
        return jsonify({"message": "Login successful!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401

@app.route('/get_posts', methods=['POST'])
def get_posts():
    data = request.json
    username = data.get('username')

    linkedin = active_sessions.get(username)
    if not linkedin:
        return jsonify({"error": "Invalid session. Please log in again."}), 403

    try:
        posts = linkedin.get_feed_updates(limit=5)
        response = {
            "posts": [
                {"id": post['entityUrn'], "content": post.get('commentary', 'No Content')}
                for post in posts
            ]
        }
        return jsonify(response), 200
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
