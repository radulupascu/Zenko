import pinecone as pc
import pandas as pd
 
# initialize connection to pc (get API key at app.pc.io)
pc.init(
    api_key=open("../P_KEY", "r").read(),
    environment="gcp-starter"  # find next to API key in console
)
#pc.create_index('database1', dimension=768)
#print(pc.list_indexes())

df = pd.read_csv('../data/FDV_TRANSN_updated.csv')
#df.dropna(inplace=True)
print(df)

# index.query(
#     queries=[2. , 3. , 4.],
#     top_k=1,
#     include_values=True
# )

