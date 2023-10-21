import openai


def get_gpt_response(user_message):
  # Get GPT responses to messages
  response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
      {"role": "user", "content": user_message}
    ]
  )
  return response["choices"][0]["message"]["content"]


# Import GPT-3 API key
try:
  API_KEY = open("API_KEY", "r").read()
except FileNotFoundError:
  API_KEY = "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"

openai.api_key = API_KEY

# Initialize chat log
chat_log = []
print("Type quit to exit")
# Get user message and generate response
while True:
  user_message = input("ASK: ")
  if user_message.lower() == "quit":
    break
  else:
    chat_log.append({"role": "user", "content": user_message})

    assistant_response = get_gpt_response(chat_log[-1]["content"])

    print("Alt-Shift:", assistant_response.strip("\n").strip())
    chat_log.append({"role": "assistant",
     "content": assistant_response.strip("\n").strip()})

