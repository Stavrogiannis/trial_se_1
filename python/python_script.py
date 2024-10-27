from langchain_community.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.embeddings import OpenAIEmbeddings  

# loading the document
loader = TextLoader('instruct.txt')

# embedding staff
embedding = OpenAIEmbeddings()  

# index with  embedding
index = VectorstoreIndexCreator(embedding=embedding).from_loaders([loader])

#query from command line arguments
query = sys.argv[1]


result = index.query(query)

# result to send to server.js
print(result)