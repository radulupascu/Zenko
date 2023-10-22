import openai
from func import get_gpt_response_content, parse_gpt_response

# Import GPT-3 API key
try:
  API_KEY = open("API_KEY", "r").read()
except FileNotFoundError:
  pass
openai.api_key = API_KEY

def main():
  # Initialize chat log
  chat_log = []
  print("Type quit to exit")
  # Get user message and generate response
  while True:
    user_message = input("ASK: ") # Replace with input from website
    if user_message.lower() == "quit":
      break
    else:
      chat_log.append({"role": "system", "content": 
                       "interpret this for me and formulate it in an helpful matter" + user_message})

      assistant_response = get_gpt_response_content(chat_log)

      print(parse_gpt_response(assistant_response)) # Replace with output on website
      chat_log.append({"role": "assistant",
                      "content": assistant_response.strip("\n").strip()})
      
if __name__ == "__main__":
  main()