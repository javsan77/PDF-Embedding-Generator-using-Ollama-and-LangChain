import numpy as np
import json
import os
from functions.configuration import EMBEDDINGS_FOLDER

def save_results(embeddings_data):
    """Store results in numpy and JSON formats."""
    
    if not embeddings_data:
        print("No data to save.")
        return

    # Extract only the vectors to save them as an efficient NumPy array
    embeddings_array = np.array([item['embedding'] for item in embeddings_data])
    
    # Extract only texts to store them in a simple text/JSON file
    texts_list = [item['chunk_text'] for item in embeddings_data]

    # Save NumPy vectors
    np.save(os.path.join(EMBEDDINGS_FOLDER, "embeddings_vectors.npy"), embeddings_array)
    print("-> 4. Vectors saved to 'embeddings_vectors.npy'")

    # Save original texts in JSON (useful for the RAG phase)
    with open(os.path.join(EMBEDDINGS_FOLDER, "original_texts.json"), 'w', encoding='utf-8') as f:
        json.dump(texts_list, f, ensure_ascii=False, indent=4)
    print("-> 5. Original texts saved to 'original_texts.json'")
    
    print("\n--- PROCESS FINISHED SUCCESSFULLY ---")
    print(f"Total vectors saved: {embeddings_array.shape[0]}")
    print(f"Dimension of each vector: {embeddings_array.shape[1]}")