import os
import openai
import json
from flask import Flask , render_template ,request
# from dotenv import load_dotenv
from os import getenv



app = Flask(__name__)
#take api from .env file
api_key = getenv('API_KEY')

openai.api_key = api_key
# n =f'What are some key points I should know when studying about India ?\n\n1.'
# response = openai.Completion.create(
#   engine="davinci-instruct-beta",
#   prompt=n,
#   temperature=1,
#   max_tokens=64,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )


# #get only specific data from json
# data = response.choices[0]['text']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/note',methods = ['GET','POST'])
def note():
  if request.method == 'POST':
    data = request.form['name']
    data1 = f'What are some key points I should know when studying about {data} ?'
    response = openai.Completion.create(
      engine="davinci-instruct-beta",
      prompt=data1,
      temperature=1,
      max_tokens=64,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    data = response.choices[0]['text']
    return render_template('note.html',data = data)
  else:
    return render_template('note.html')
    
@app.route('/js',methods = ['GET','POST'])
def js():
  if request.method == 'POST':
    data = request.form['name']
    if "python" in data:
      a = "#"
    else:
      a = "You:"
    response = openai.Completion.create(
      engine="davinci-codex",
      prompt=data,
      temperature=0,
      max_tokens=60,
      top_p=1.0,
      frequency_penalty=0.5,
      presence_penalty=0.0,
      stop=[a]
    )

    data = response.choices[0]['text']
    if "#" in data:
      data = data.replace("#",'<br>')
    if "python" in data:
       data = data.add("<br>")
    return render_template('js.html',data = data)
  else:
    return render_template('js.html')

@app.route('/simple',methods = ['GET','POST'])
def simple():
  if request.method == 'POST':
    data = request.form['name']
    response = openai.Completion.create(
      engine="davinci",
      prompt=data,
      temperature=0.5,
      max_tokens=100,
      top_p=1,
      frequency_penalty=0.2,
      presence_penalty=0,
      stop=["\"\"\""]
)
    data = response.choices[0]['text']
    return render_template('simple.html',data = data)
  else:
    return render_template('simple.html')                                                                       

  return render_template('simple.html',data = data)


if __name__ == '__main__':
  app.run(debug=True) 