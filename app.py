from flask import Flask, request, jsonify
from scraper import linkedin_login, get_connections_posts, close_driver
from gemini_api import generate_comments

app = Flask(__name__)

sessions = {}  # Active LinkedIn sessions

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']
    
    try:
        driver = linkedin_login(username, password)
        sessions[username] = driver
        return jsonify({"message": "Logged in successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401

@app.route('/get_posts', methods=['POST'])
def get_posts():
    data = request.json
    username = data['username']
    
    driver = sessions.get(username)
    if not driver:
        return jsonify({"error": "Session expired or not valid."}), 403
    
    try:
        posts = get_connections_posts(driver)
        return jsonify({"posts": posts}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/generate_comment', methods=['POST'])
def generate_comment():
    data = request.json
    post_content = data.get('content')

    try:
        comments = generate_comments(post_content)
        return jsonify({"comments": comments}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/logout', methods=['POST'])
def logout():
    data = request.json
    username = data['username']
    
    driver = sessions.pop(username, None)
    if driver:
        close_driver(driver)
        return jsonify({"message": "Logged out"}), 200
    return jsonify({"error": "No active session found"}), 403

if __name__ == "__main__":
    app.run(debug=True, port=5000)
