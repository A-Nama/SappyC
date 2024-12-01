import requests

def generate_comments(post_content):
    # Replace with actual Gemini API endpoint and key
    GEMINI_API_URL = "https://api.gemini.com/generate_comment"
    API_KEY = "your_gemini_api_key"

    payload = {
        "content": post_content,
        "max_comments": 3  # Number of comment suggestions
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(GEMINI_API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json().get('comments', [])
    else:
        raise Exception(f"Gemini API error: {response.status_code} - {response.text}")
