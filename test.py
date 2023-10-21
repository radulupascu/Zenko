from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(openai_api_key = open("API_KEY", "r").read())
text = "This is a test document."
query_result = embeddings.embed_query(text)
print(query_result[:5])