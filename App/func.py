from transformers import BertTokenizer, BertModel
import torch
import openai

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

def get_gpt_response_content(user_message):
  # Get GPT responses to messages
  response = openai.ChatCompletion.create(
    model = "gpt-4",
    messages = 
      user_message
  )
  return response["choices"][0]["message"]["content"]

def parse_gpt_response(response):
  # Parse GPT response
  response = response.strip("\n").strip()
  response = response.replace("Alt-Shift:", "")
  return response
