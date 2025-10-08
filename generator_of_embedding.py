from functions.configuration import PDF_PATH
from functions.generation_embedding import generate_embeddings
from functions.extract_and_split_pdf import extract_and_split_pdf
from functions.saving_results import save_results

if __name__ == "__main__":
    
    # 1. PDF Extraction and Splitting
    document_chunks = extract_and_split_pdf(PDF_PATH)
    
    if document_chunks is None:
        exit()
        
    # 2. Embedding generation
    results = generate_embeddings(document_chunks)
    
    if results is None:
        exit()
        
    # 3. Save results
    save_results(results)
