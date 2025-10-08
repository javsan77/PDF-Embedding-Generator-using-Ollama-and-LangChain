import pypdf
from functions.configuration import CHUNK_SIZE, CHUNK_OVERLAP
from langchain_text_splitters import RecursiveCharacterTextSplitter

def extract_and_split_pdf(pdf_path: str):
    """Extracts text from the PDF and divides it into chunks."""
    print(f"-> 1. Extracting text from: {pdf_path}")
    full_text = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = pypdf.PdfReader(file)
            for page in reader.pages:
                # Extract text and add an optional page separator
                full_text += page.extract_text() + "\n--- END OF PAGE ---\n"
    except FileNotFoundError:
        print(f"ERROR: the file '{pdf_path}' was not found. Please check the name.")
        return None
    except Exception as e:
        print(f"ERROR reading the PDF: {e}")
        return None

    # Initializes the text divider
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len
    )
    
    # Divide the text into chunks
    print(f"-> 2. Dividing the text into chunks of {CHUNK_SIZE} characters...")
    chunks = text_splitter.split_text(full_text)
    print(f"✅ Text divided into {len(chunks)} chunks.")
    return chunks