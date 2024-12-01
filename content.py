import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")
genai.configure(api_key=api_key)

# Function to generate sassy comments using Gemini API
def generate_sassy_comment(post_content):
    # Create the generation configuration
    generation_config = {
        "temperature": 1.9,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    # Create the model
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
        system_instruction="Based on LinkedIn post user inputs, come up with 6 short yet witty comments for the post with emojis, as a numbered list (1. ... 2. ... etc.). The tones are: Sarcastic, Passive-Aggressive, Too Real, Exaggerated Compliment, Meme-like, and Blunt and Bold. Do not add extra details, just the list of comments.\n",
    )

    # Start the chat session
    chat_session = model.start_chat(
        history=[{"role": "user", "parts": [post_content]}]
    )

    # Send the message to the model
    response = chat_session.send_message(post_content)

    # Check if response has content
    if hasattr(response, 'text') and response.text:
        comments_raw = response.text.strip()

        # Extract comments using numbered list regex
        import re
        comments_list = re.findall(r"\d\.\s*(.+)", comments_raw)

        # Clean and return the comments
        return [comment.strip() for comment in comments_list if comment.strip()]
    else:
        print("Error: No valid response from Gemini API.")
        return []
