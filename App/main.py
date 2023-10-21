import openai

try:
  API_KEY = open("API_KEY", "r").read()
except FileNotFoundError:
  API_KEY = "default_api_key"


openai.api_key = API_KEY

response = openai.ChatCompletion.create(
  model = "gpt-3.5-turbo",
  messages = [
    {
      "role": "user", "content": "Hello, who are you?"
    },
  ]
)

print(response)
