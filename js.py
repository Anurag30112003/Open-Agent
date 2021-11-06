import os
import openai

openai.api_key = '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'


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
