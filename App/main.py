import openai

try:
  API_KEY = open("API_KEY", "r").read()
except FileNotFoundError:
  API_KEY = "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"

openai.api_key = API_KEY

chat_log = []

print("Type quit to exit")
while True:
  user_message = input("ASK: ")
  if user_message.lower() == "quit":
    break
  else:
    chat_log.append({"role": "user", "content": user_message})

    response = openai.ChatCompletion.create(
      model = "gpt-3.5-turbo",
      messages = [
        chat_log[-1]
      ]
    )
    assistant_response = response["choices"][0]["message"]["content"]
    print("Alt-Shift:", assistant_response.strip("\n").strip())
    chat_log.append({"role": "assistant",
     "content": assistant_response.strip("\n").strip()})

