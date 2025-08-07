import streamlit as st
from models.llm import generate_response
from models.embeddings import create_vector_store, query_vector_store
from utils.rag_utils import load_pdf_text
from utils.web_search import search_web

st.set_page_config(page_title="NeoStats AI Chatbot", layout="wide")
st.title("NeoStats AI Chatbot")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
query = st.text_input("Ask a question")
mode = st.radio("Select Response Mode", ["concise", "detailed"])

use_web = st.checkbox("Use Web Search if needed")

if uploaded_file:
    file_path = f"temp/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("File uploaded successfully")

    with st.spinner("Preparing knowledge base..."):
        chunks = load_pdf_text(file_path)
        index, texts, vectors = create_vector_store(chunks)

if st.button("Get Response") and query:
    st.info("Processing your query...")
    
    rag_context = ""
    if uploaded_file:
        top_chunks = query_vector_store(query, index, texts, vectors)
        rag_context = "\n".join(top_chunks)

    web_context = ""
    if use_web:
        web_context = search_web(query)

    full_prompt = f"Context:\n{rag_context}\n\nWeb Info:\n{web_context}\n\nQuestion: {query}"
    answer = generate_response(full_prompt, mode=mode)
    st.success("Response:")
    st.write(answer)
