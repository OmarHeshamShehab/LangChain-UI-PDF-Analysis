
# Ask Your PDF 💬

## Overview
**Ask Your PDF** is a Streamlit web application that allows users to upload PDF documents and ask questions about their contents. The application leverages OpenAI's language models, FAISS for similarity search, and various utilities for PDF processing and question answering.

## Features
- **PDF Upload**: Upload a PDF document for querying.
- **Question Answering**: Ask questions about the PDF content and receive context-aware answers.
- **Text Embedding and Similarity Search**: Uses FAISS to retrieve relevant sections of the text for accurate answers.
- **User-Friendly Interface**: Built with Streamlit for an intuitive and interactive experience.

## Prerequisites
- **Python 3.7+**
- **Environment Variables**: Ensure you have a `.env` file containing your OpenAI API key:
  ```plaintext
  OPENAI_API_KEY=your_api_key
  ```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with your OpenAI API key:
   ```plaintext
   OPENAI_API_KEY=your_api_key
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run SinglePDF.py
   ```

2. In your browser, navigate to the displayed `localhost` URL.

3. Upload a PDF document and enter a question in the provided input box. The application will display an answer based on the content of the uploaded PDF.

## Code Structure

- **PDF Reader**: Uses `PyPDF2` to extract text from the PDF.
- **Text Splitting**: The `CharacterTextSplitter` splits extracted text into manageable chunks, optimized for embeddings and querying.
- **Embeddings and FAISS**: 
  - **OpenAIEmbeddings**: Converts text into embeddings for semantic similarity.
  - **FAISS**: Handles efficient similarity searching across text chunks.
- **Question Answering Chain**: 
  - The `load_qa_chain` from `langchain` is used to generate answers by querying the most relevant text chunks.

## Libraries Used
- `Streamlit`: Web interface framework.
- `dotenv`: For loading API keys and configuration from a `.env` file.
- `langchain`: Manages language model operations, text splitting, and QA chains.
- `PyPDF2`: PDF reading and text extraction.
- `FAISS`: Handles similarity search on embedding vectors.
- `OpenAI`: Generates embeddings and answers for the uploaded PDF's content.

## Troubleshooting
- **Environment Variables**: Ensure `.env` contains the correct `OPENAI_API_KEY`.
- **PDF Compatibility**: The app relies on `PyPDF2`, which may have limitations with certain PDF types. Ensure your PDFs are text-based.

## License
This project is licensed under the MIT License.

## Acknowledgments
- Built with [Streamlit](https://streamlit.io) and [OpenAI API](https://openai.com/).
- PDF reading functionality powered by [PyPDF2](https://pypi.org/project/PyPDF2/).
- Embedding and similarity search supported by [FAISS](https://faiss.ai/).
