import streamlit as st

with st.chat_message("user"):
    st.write("Hello World!")

with st.chat_message("assisstant"):
    st.write("Hello Abhirupa!")

if prompt := st.chat_input("Let's chat!"):
    with st.chat_message("user"):
        st.write("Hi! Let's talk!")