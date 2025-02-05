from dotenv import load_dotenv
import os
# from openai import OpenAI
# Load the .env file
load_dotenv()

# Access environment variables
api_key = os.getenv("HELLO")
print(api_key)
