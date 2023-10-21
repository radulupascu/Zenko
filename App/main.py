import openai
from func import text_to_vector, get_gpt_response_content, parse_gpt_response

# Import GPT-3 API key
try:
  API_KEY = open("API_KEY", "r").read()
except FileNotFoundError:
  API_KEY = "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"
openai.api_key = API_KEY

def main():
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

      assistant_response = get_gpt_response_content(chat_log[-1]["content"])

      print(parse_gpt_response(assistant_response))
      chat_log.append({"role": "assistant",
                      "content": assistant_response.strip("\n").strip()})
      
      # vector = text_to_vector(assistant_response.strip("\n").strip())

if __name__ == "__main__":
  main()
