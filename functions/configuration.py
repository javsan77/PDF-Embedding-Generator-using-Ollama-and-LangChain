import os

# PDF name (inside directory 'pdf')
PDF = "202510_Web_Procedure_XYZ.pdf";

# directory to store embeddings 
EMBEDDINGS_FOLDER = "embeddings";

# os.path.join for multiplatform
PDF_PATH = os.path.join("pdf", PDF) 

# Embedding modelr (previously downloaded with 'ollama pull nomic-embed-text')
EMBEDDING_MODEL = 'nomic-embed-text'

# Parameters for text splitting (chunks)
# Maximum size for each chunk
CHUNK_SIZE = 1000
# Number of characters that overlap between chunks (to maintain context)
CHUNK_OVERLAP = 200
