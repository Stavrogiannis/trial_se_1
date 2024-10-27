import sys
from langchain_community.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from sentence_transformers import SentenceTransformer

# Load the Sentence Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')  # You can choose other models as well
embedding_model = SentenceTransformerEmbedding(model)

# Loading
loader = TextLoader('instruct.txt')
index = VectorstoreIndexCreator(embedding=embedding_model).from_loaders([loader])

# Get the query from command line arguments
query = sys.argv[1]

# Querying on the indexed document
result = index.query(query)

# Printing the result to send to server.js
print(result)