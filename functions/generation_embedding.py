from functions.configuration import EMBEDDING_MODEL
import ollama

def generate_embeddings(chunks: list[str]):
    """Generate embeddings for each chunk using the Ollama API."""
    print(f"-> 3. Generating embeddings with model '{EMBEDDING_MODEL}'...")
    embeddings_data = []
    
    for i, chunk in enumerate(chunks):
        try:
            # Calls the Ollama service to generate the vector
            response = ollama.embeddings(
                model=EMBEDDING_MODEL,
                prompt=chunk
            )
            
            # Stores the original text and its embedding vector
            embeddings_data.append({
                'chunk_index': i,
                'chunk_text': chunk,
                'embedding': response['embedding']
            })
            
            # Shows simple progress
            if (i + 1) % 50 == 0 or i == len(chunks) - 1:
                print(f"   - Progress: {i+1}/{len(chunks)} embeddings generated.")

        except Exception as e:
            # Error handling (e.g., if Ollama is not active or the model does not exist)
            print(f"\nFATAL ERROR processing chunk {i+1}. Is Ollama active? ({e})")
            return None
            
    print("✅ Complete embedding generation.")
    return embeddings_data
