import openai
from transformers import BertTokenizer, BertModel
import torch

# Load pre-trained BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

def text_to_vector(text):
    # Tokenize input text
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
    
    # Get BERT embeddings
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Use the [CLS] token embedding as the representation of the text
    vector = outputs.last_hidden_state[:, 0, :].squeeze().numpy()
    
    return vector

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
    
    # vector = text_to_vector(assistant_response.strip("\n").strip())

