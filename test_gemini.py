
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing from .env")

# Initialize Gemini
client = genai.Client(api_key=api_key)

# Test the AI model
response = client.models.generate_content(
    model=model,
    contents="Write a short B2B outreach email for an AI automation company."
)

print(response.text)
