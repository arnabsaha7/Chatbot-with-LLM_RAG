import streamlit as st
import os
import faiss
import numpy as np
import json
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory.buffer import ConversationBufferMemory
from langchain.embeddings import OpenAIEmbeddings

# Set up your OpenAI API key
os.environ["OPENAI_API_KEY"] = "your api key"
openai_api_key = os.environ["OPENAI_API_KEY"]
llm = OpenAI()
memory = ConversationBufferMemory()


# Load FAISS index and documents with metadata
index = faiss.read_index("faiss_index_1")
with open("documents.json", "r") as f:
    documents = json.load(f)

# Initialize embeddings model
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

# Function to perform document retrieval
def retrieve_documents(query):
    query_embedding = embeddings.embed_query(query)
    distances, indices = index.search(np.array([query_embedding]), k=5)
    retrieved_docs = [documents[i] for i in indices[0]]
    return retrieved_docs

# Create the conversation chain
conversation_chain = ConversationChain(
    llm=llm,
    memory=memory
)

# Streamlit app
st.title("Welcome to the Chatbot! 🤖")


# Load custom CSS from a file
with open("styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# Initialize session state variables
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []
    st.session_state.memory = memory


# Display conversation history
st.write('<div class="chat-container">', unsafe_allow_html=True)
if "conversation_history" in st.session_state:
    for speaker, message in st.session_state.conversation_history:
        bubble_class = "user-bubble" if speaker == "You" else "bot-bubble"
        st.markdown(f'<div class="chat-bubble {bubble_class}"><b>{speaker}:</b> {message}</div>', unsafe_allow_html=True)
st.write('</div>', unsafe_allow_html=True)


# Input container with reset button, text input, and send button
st.markdown('<div class="input-container">', unsafe_allow_html=True)
reset_button_clicked = st.button("Reset Conversation", key="reset_button")
user_input = st.text_input("You: ", key="input")
send_button_clicked = st.button("Send", key="send_button")
st.markdown('</div>', unsafe_allow_html=True)


# Process user input and generate response
if send_button_clicked and user_input:
    retrieved_docs = retrieve_documents(user_input)
    context = "\n".join([f"{doc['content']} (Source: {doc['source']}, Year: {doc['year']}, Published in: {doc['published_in']})" for doc in retrieved_docs])
    st.session_state.memory.save_context(inputs={"user_input": user_input}, outputs={"context": context})
    response = conversation_chain.run(user_input)
    st.session_state.conversation_history.append(("You", user_input))
    st.session_state.conversation_history.append(("Rem", response))
    st.session_state.memory = memory

# Handle reset conversation
if reset_button_clicked:
    st.session_state.conversation_history = []
    st.session_state.memory.clear()
    st.success("Conversation history cleared!")