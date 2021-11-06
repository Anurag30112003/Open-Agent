import os
import openai
import json

openai.api_key = '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'
s = input()
n =f'What are some key points I should know when studying about {s} ?\n\n1.'
response = openai.Completion.create(
  engine="davinci-instruct-beta",
  prompt=n,
  temperature=1,
  max_tokens=64,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
# data = response.json()
h = response['choices']['text']
print(h)