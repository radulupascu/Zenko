# This is a sample Python script.
import os
import openai
from fastapi import FastAPI, requests
from func import get_gpt_response_content, parse_gpt_response
from pydantic import BaseModel
import random
from fastapi.middleware.cors import CORSMiddleware
try:
  API_KEY = open("API_KEY", "r").read()
except FileNotFoundError:
  pass
openai.api_key = API_KEY

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # This allows all origins. Be more specific in production.
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],
)

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
chat_log=[]
@app.get('/')
async def root():
    return {'example':'This is an example','data':0}
class ChatRequest(BaseModel):
    prompt: str
    model: str
    max_tokens: int


@app.post('/chatbot')
async def chatbot(request: ChatRequest):
    user_message = request.prompt
    print(user_message)
    if user_message.lower() == "quit" or user_message.lower() == '':
        # reset chat log
        return ({"response": "Session ended"})

    chat_log.append({"role": "user", "content": user_message})
    assistant_response = get_gpt_response_content(chat_log[-1]["content"])

    parsed_response = parse_gpt_response(assistant_response)
    chat_log.append({"role": "assistant", "content": assistant_response.strip("\n").strip()})

    return ({
        "assistant_response": assistant_response.strip("\n").strip()
    })


@app.get('/random')
async def get_random():
    rm: int = random.randint(0,100)
    return {'number':rm, 'limit':100}
# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
