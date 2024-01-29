import streamlit as st
import os

# Load environment variables from .env file (optional)
from dotenv import load_dotenv


# Retrieve secret key from the environment variable
secret_key = os.getenv("SECRET_KEY")

if secret_key is None:
    st.error("Please provide a secret key in the advanced settings.")
else:
    # Continue with your code using the secret key
    import pickle
    import time
    import langchain
    from langchain_openai import OpenAI
    from langchain.chains import RetrievalQAWithSourcesChain
    from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    from langchain_community.document_loaders import UnstructuredURLLoader
    from langchain_openai import OpenAIEmbeddings
    from langchain.vectorstores.faiss import FAISS
    import threading
    from dotenv import load_dotenv

    load_dotenv()  # take environment variables from .env and load

    llm = OpenAI(temperature=0.9, max_tokens=500)
    st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
                font-weight:bold;}
    body {
        color: #fff;
        background-color: #19E8E6;
    }
          
    </style>
    """, unsafe_allow_html=True)
    st.title("           Questy - A Research Buddy 🤖")
    left_co, cent_co,last_co = st.columns(3)
    with left_co:
        st.image("1.png",width=240)
    with cent_co:
        st.image("2.png",width=240)
    with last_co:
        st.image("4.png",width=240)
    st.sidebar.title("News Article URLs")

    urls = []
    for i in range(3):
        url = st.sidebar.text_input(f"URL {i+1}")
        urls.append(url)

    process_url_clicked = st.sidebar.button("Process URLs")
    file_path = "faiss_store_openai.pkl"

    main_placeholder = st.empty()
    llm = OpenAI(temperature=0.9, max_tokens=500)

    if process_url_clicked:
        loader = UnstructuredURLLoader(urls=urls)
        main_placeholder.text("Data Loading...Started...✅✅✅")
        data = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(
            separators=['\n\n', '\n', '.', ','],
            chunk_size=4000
        )
        main_placeholder.text("Text Splitter...Started...✅✅✅")
        docs = text_splitter.split_documents(data)
        embeddings = OpenAIEmbeddings()
        vectorstore_openai = FAISS.from_documents(docs, embeddings)
        main_placeholder.text("Embedding Vector Started Building...✅✅✅")
        time.sleep(2)

        # Save the FAISS index to a pickle file
        vectorstore_openai.save_local("newstool")

    query = main_placeholder.text_input("Type your Question Here")
    if query:
        vectorstore=FAISS.load_local("newstool", OpenAIEmbeddings())        
        chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
        result = chain({"question": query}, return_only_outputs=True)
        # result will be a dictionary of this format --> {"answer": "", "sources": [] }
        st.markdown('<p class="big-font">Answer</p>', unsafe_allow_html=True)
        st.write(result["answer"])

        # Display sources, if available
        sources = result.get("sources", "")
        if sources:
            st.subheader("Sources:")
            sources_list = sources.split("\n")  # Split the sources by newline
            for source in sources_list:
                st.write(source)
