import streamlit as st

with st.chat_message("user"):
    st.write("Hello, world!")

with st.chat_message("assistant"):
    st.write("Hello, Abhirupa!")

if prompt := st.chat_input("Let's Talk!"):
    with st.chat_message("user"):
        st.markdown(prompt)
    #Maintaining a Chat History
    st.session_stte.messages.append({"role": "user", "content": prompt})