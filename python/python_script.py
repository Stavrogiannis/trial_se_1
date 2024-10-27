import sys
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

# loading
loader = TextLoader('instruct.txt')
index = VectorstoreIndexCreator().from_loaders([loader])

# gett the query from command line arguments
query = sys.argv[1]

# querying on the indexed document
result = index.query(query)

# printing the result to to send to sever.js
print(result)