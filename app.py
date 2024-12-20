from urllib import response
import streamlit as st
from search import reply

st.title("💬 Chatbot")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi! How can I assist you today?"}]

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
if prompt := st.chat_input():
    # Append user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    mes = reply(prompt).response
    st.session_state.messages.append({"role": "assistant", "content": mes})
    st.chat_message("assistant").write(mes)

# Add a sidebar with a list of text items
st.sidebar.title("Sidebar")
st.sidebar.write("This is the sidebar content")
sidebar_items = ["Item 1", "Item 2", "Item 3"]
for item in sidebar_items:
    st.sidebar.write(item)
