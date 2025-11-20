import sys
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)



if len(sys.argv) == 1:
    sys.exit(1)
user_prompt = sys.argv[1:]



messages = [
    types.Content(role="user",parts=[types.Part(text=str(user_prompt))]),
]

response = client.models.generate_content(model="gemini-2.0-flash-001",
                               contents=messages,)

prompt_token = response.usage_metadata.prompt_token_count
candidates_token = response.usage_metadata.candidates_token_count

if "--verbose" in user_prompt:
    print(f"User prompt:{user_prompt[0]}")
    print(f"Prompt tokens: {prompt_token}")
    print(f"Response tokens: {candidates_token}")

print(response.text)

