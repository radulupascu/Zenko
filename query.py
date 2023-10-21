from langchain.embeddings import OpenAIEmbeddings
import pinecone


#### openai
embeddings = OpenAIEmbeddings(openai_api_key = open("API_KEY", "r").read())

#### pinecone init

pinecone.init(
    api_key=
    environment= 
)
index = pinecone.Index('INDEX')


def ask(question):
    embed = embeddings.embed_query(question)
    print(embed)
    
    return index.query(
        vector=embed,
        top_k=3,
        include_vlaues=False
    ) 

print(ask('voiture'))
