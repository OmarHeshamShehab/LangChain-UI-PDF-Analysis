
# README.md

## Overview
This repository contains two Python scripts, `SinglePDF_Ollama.py` and `SinglePDF_OpenAI.py`, that leverage the capabilities of the LangChain library to build question-answering systems based on the content of PDF documents. These scripts are designed to provide a web-based interface for users to ask questions about the contents of a PDF and receive answers, using different language models and embeddings.

- **SinglePDF_Ollama.py**: Uses the Ollama language model and embeddings.
- **SinglePDF_OpenAI.py**: Uses the OpenAI language model and embeddings.

Both scripts use Streamlit for building a web interface and share a similar architecture while differing in the language models and embedding techniques employed.

## Requirements
To run these scripts, you will need the following:

- Python 3.11.10
- Required Python libraries, which can be installed via `pip` (see the **Installation** section)
- A `.env` file for environment variables, particularly API keys for accessing language models

## Installation
Follow these steps to set up the environment and run the scripts:

1. **Clone the repository**:
   ```sh
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Create and activate a virtual environment**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scriptsctivate
   ```

3. **Install required dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory to store your API keys. The file should contain:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Scripts Overview

### 1. SinglePDF_Ollama.py
This script utilizes the **Ollama** language model to handle question-answering tasks related to the PDF content. It uses `OllamaEmbeddings` to generate vector embeddings, which are then used to retrieve the most relevant sections of the PDF for answering the user’s query.

#### Key Features:
- Utilizes `OllamaEmbeddings` for embedding generation.
- Supports question-answering using the `Ollama` language model.
- Provides a web interface using Streamlit, making it easy for users to interact with the document.

### 2. SinglePDF_OpenAI.py
This script makes use of the **OpenAI** language model to provide answers to questions regarding the PDF content. It employs `OpenAIEmbeddings` to create vector representations of text chunks, which are used in finding the most relevant answers.

#### Key Features:
- Utilizes `OpenAIEmbeddings` for embedding generation.
- Supports question-answering using the `OpenAI` language model.
- Provides a web interface using Streamlit.

## Usage
To run either of the scripts, use the following command:

```sh
streamlit run SinglePDF_Ollama.py  # For the Ollama-based script
# OR
streamlit run SinglePDF_OpenAI.py  # For the OpenAI-based script
```

Once you run the script, a Streamlit web interface will be available in your browser, allowing you to upload a PDF file and ask questions related to its content.

## File Structure
- **SinglePDF_Ollama.py**: Python script using Ollama for QA.
- **SinglePDF_OpenAI.py**: Python script using OpenAI for QA.
- **requirements.txt**: Lists all required Python packages for running the scripts.
- **.env**: File for storing API keys (not included in the repository for security reasons).

## Dependencies
The following Python libraries are required to run the scripts:
- **Streamlit**: For creating the web interface.
- **dotenv**: To load environment variables from `.env` files.
- **langchain**: For chaining the embeddings, LLMs, and QA systems.

Make sure all dependencies are installed by running the command:
```sh
pip install -r requirements.txt
```

## Environment Variables
SinglePDF_OpenAI script require API keys for interacting with it's respective language models. Ensure that your `.env` file is correctly set up to provide access to these keys.

## Key Differences Between Ollama and OpenAI Scripts
- **Language Model**: `SinglePDF_Ollama.py` uses Ollama, while `SinglePDF_OpenAI.py` uses OpenAI.
- **Embedding Method**: Each script uses the corresponding embedding method (`OllamaEmbeddings` or `OpenAIEmbeddings`), which impacts the vector representation of text data.