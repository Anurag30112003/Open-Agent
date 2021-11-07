import os
import openai
from os import getenv

api_key = getenv('API_KEY')

openai.api_key = api_key

x = input("")
if "python" in x:
  a = "#"
else:
  a = "You:"

response = openai.Completion.create(
  engine="davinci-codex",
  prompt=x,
  temperature=0,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.5,
  presence_penalty=0.0,
  stop=[a]
)

print(response.choices[0].text)
