# 🧠 PDF Embedding Generator using Ollama and LangChain

This project extracts text from a PDF document, splits it into manageable chunks, generates embeddings using **Ollama**, and saves both the embeddings and the original text for later use (for example, in a RAG-based application).

---

## 🚀 Overview

The application performs the following main steps:

1. **Extract text** from a PDF file using [`pypdf`](https://pypi.org/project/pypdf/).  
2. **Split the text** into overlapping chunks with [`langchain-text-splitters`](https://python.langchain.com/).  
3. **Generate embeddings** for each chunk using the **Ollama API** and the `nomic-embed-text` model.  
4. **Save results** in two formats:
   - A NumPy `.npy` file containing all embedding vectors.
   - A JSON file containing the corresponding text chunks.

The goal is to prepare data for use in **Retrieval-Augmented Generation (RAG)** or any semantic search pipeline.

---

## 🧩 Project Structure

```

.
├── generator_of_embedding.py
└── functions/
├── configuration.py
├── extract_and_split_pdf.py
├── generation_embedding.py
└── saving_results.py

````

### Description of Key Files

| File | Purpose |
|------|----------|
| `generator_of_embedding.py` | Main entry point of the program; runs extraction, embedding, and saving steps. |
| `functions/configuration.py` | Central configuration file (PDF path, model name, chunk size, etc.). |
| `functions/extract_and_split_pdf.py` | Extracts text from a PDF and divides it into overlapping chunks. |
| `functions/generation_embedding.py` | Calls Ollama to generate vector embeddings for each text chunk. |
| `functions/saving_results.py` | Saves embeddings and original texts to disk. |

---

## ⚙️ Requirements

### 1. Python Dependencies

Install required packages:

```bash
pip install numpy pypdf langchain-text-splitters ollama
````

### 2. Ollama Setup

You must have **Ollama** installed and running locally.
Download the embedding model before execution:

```bash
ollama pull nomic-embed-text
```

### 3. Folder Structure

The project expects the following directories:

```
pdf/                # Folder containing the input PDF file
embeddings/         # Output folder for .npy and .json files
functions/          # Python helper modules
```

Make sure the PDF file specified in `functions/configuration.py` exists in the `pdf/` directory.

---

## ▶️ Usage

Run the main script:

```bash
python generator_of_embedding.py
```

The process will:

1. Read and split your PDF.
2. Generate embeddings chunk by chunk.
3. Save the results to:

   ```
   embeddings/embeddings_vectors.npy
   embeddings/original_texts.json
   ```

---

## 📦 Output Example

After execution, you’ll have:

```
embeddings/
├── embeddings_vectors.npy     # 2D NumPy array with embeddings
└── original_texts.json        # List of text chunks
```

Each vector corresponds to one text chunk from the original PDF.

---

## 🧠 Example Flow

```
-> 1. Extracting text from: pdf/202510_Web_Procedure_XYZ.pdf
-> 2. Dividing the text into chunks of 1000 characters...
✅ Text divided into 47 chunks.
-> 3. Generating embeddings with model 'nomic-embed-text'...
   - Progress: 47/47 embeddings generated.
✅ Complete embedding generation.
-> 4. Vectors saved to 'embeddings_vectors.npy'
-> 5. Original texts saved to 'original_texts.json'

--- PROCESS FINISHED SUCCESSFULLY ---
Total vectors saved: 47
Dimension of each vector: 768
```

---

## 🧰 Configuration

Modify the following variables in `functions/configuration.py` as needed:

```python
PDF = "202510_Web_Procedure_XYZ.pdf"
EMBEDDINGS_FOLDER = "embeddings"
EMBEDDING_MODEL = "nomic-embed-text"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
```

---

## 🧩 Potential Use Cases

* RAG (Retrieval-Augmented Generation) pipelines
* Document semantic search
* Vector database ingestion (e.g., Pinecone, FAISS, Qdrant)
* Text clustering and similarity analysis

---

## 🧑‍💻 Author

Developed by **Javier Sanchez Ayte**
🇵🇪 Backend Developer — Python | Java | LLM Engineering

---

## 🪪 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
