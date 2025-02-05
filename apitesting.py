from dotenv import load_dotenv
import os
from openai import OpenAI
# Load the .env file
load_dotenv()

# Access environment variables
api_key = os.getenv("api_key")

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)