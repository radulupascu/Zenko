import pinecone as pc
import pandas as pd
import 
# initialize connection to pc (get API key at app.pc.io)
pc.init(
    api_key=open("../P_KEY", "r").read(),
    environment="gcp-starter"  # find next to API key in console
)

i_name = "name1" #index name
if i_name in pc.list_indexes():
    pc.delete_index(i_name)

dim = 3
pc.create_index(name=i_name, dimension=dim)
index = pc.Index(index_name=i_name)

data_fr=pd.DataFrame(
    data={
        "id": ['A' , 'B'] ,
        "vector": [[1. , 2. , 3.], [3. , 4. , 5.]]

    }
)
data_fr

index.upsert(vectors=zip(data_fr.id,data_fr.vector))

index.query(
    queries=[2. , 3. , 4.],
    top_k=1,
    include_values=True
)

