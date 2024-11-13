from itertools import chain

import streamlit as st  # Streamlit for creating the web interface
from dotenv import load_dotenv  # To load environment variables from a .env file
from langchain.callbacks import get_openai_callback  # Callback for OpenAI operations
from langchain.chains.question_answering import (  # QA chain for handling questions
    load_qa_chain,
)
from langchain.embeddings.openai import OpenAIEmbeddings  # OpenAI embeddings for text
from langchain.llms import OpenAI  # OpenAI language model
from langchain.text_splitter import (  # To split text into manageable chunks
    CharacterTextSplitter,
)
from langchain.vectorstores import FAISS  # FAISS for efficient similarity search
from PyPDF2 import PdfReader  # To read PDF files


def main():
    # Load environment variables from .env file
    load_dotenv()

    # Set up the Streamlit page configuration
    st.set_page_config(page_title="Ask your PDF")

    # Display the header of the app
    st.header("Ask your PDF 💬")

    # File uploader widget for uploading PDF files
    pdf = st.file_uploader("Upload your PDF", type="pdf")

    # Process the uploaded PDF file
    if pdf is not None:
        # Initialize the PDF reader
        pdf_reader = PdfReader(pdf)
        text = ""

        # Extract text from each page of the PDF
        for page in pdf_reader.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text += extracted_text

        # Initialize the text splitter with specified parameters
        text_splitter = CharacterTextSplitter(
            separator="\n",  # Split text at newline characters
            chunk_size=1000,  # Maximum size of each chunk
            chunk_overlap=200,  # Overlap between chunks to maintain context
            length_function=len,  # Function to calculate the length of text
        )

        # Split the extracted text into chunks
        chunks = text_splitter.split_text(text)

        # Create OpenAI embeddings for the text chunks
        embeddings = OpenAIEmbeddings()

        # Initialize the FAISS vector store with the text chunks and their embeddings
        knowledge_base = FAISS.from_texts(chunks, embeddings)

        # Input field for the user to ask a question about the PDF
        user_question = st.text_input("Ask a question about your PDF:")

        # If the user has entered a question
        if user_question:
            # Perform a similarity search to find relevant chunks from the knowledge base
            docs = knowledge_base.similarity_search(user_question)

            # Initialize the OpenAI language model
            llm = OpenAI()

            # Load the question-answering chain with the language model
            chain = load_qa_chain(llm, chain_type="stuff")

            # Use the OpenAI callback to monitor the process
            with get_openai_callback() as cb:
                # Run the QA chain with the retrieved documents and the user's question
                response = chain.run(input_documents=docs, question=user_question)

                # Print callback information (e.g., token usage)
                print(cb)

            # Display the response to the user
            st.write(response)


# Entry point of the script
if __name__ == "__main__":
    main()
