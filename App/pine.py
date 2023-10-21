import pinecone

# initialize connection to pinecone (get API key at app.pinecone.io)
pinecone.init(
    api_key=open("P_KEY", "r").read(),
    environment="YOUR_ENV"  # find next to API key in console
)

# check if 'openai' index already exists (only create index if not)
if 'openai' not in pinecone.list_indexes():
    pinecone.create_index('openai', dimension=len(embeds[0]))
# connect to index
index = pinecone.Index('openai')
print("merge")