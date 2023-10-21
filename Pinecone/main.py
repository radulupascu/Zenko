import pinecone as pc
import pandas as pd
from langchain.document_loaders.csv_loader import CSVLoader


loader = CSVLoader(file_path='../data/FDV_TRANSN_updated.csv', csv_args={
    'delimiter': ',',
    'quotechar': '"',



})
data = loader.load()

print(data)
 
# initialize connection to pc (get API key at app.pc.io)
pc.init(
    api_key=open("../P_KEY", "r").read(),
    environment="gcp-starter"  # find next to API key in console
)
# pc.create_index('database1', dimension=1536)
# print(pc.list_indexes())
index_name = "database1"
if index_name not in pc.list_indexes():
    pc.create_index(index_name=index_name, dimension=1536, metric='euclidian')

# pc.create_index('test', dimension=2)
#index=pc.Index(index_name)



#df = pd.read_csv('../data/FDV_TRANSN_updated.csv')
#df.dropna(inplace=True)
#print(df)

# index.query(
#     queries=[2. , 3. , 4.],
#     top_k=1,
#     include_values=True
# )

