import streamlit as st
import requests

st.set_page_config(page_title="HR Resource Chatbot", page_icon="🤖")
st.title("HR Resource Query Chatbot 🤖")
st.write("Ask your resource or allocation queries below:")

if "history" not in st.session_state:
    st.session_state.history = []

query = st.text_input("Your query:", "")

if st.button("Ask") and query:
    with st.spinner("Thinking..."):
        resp = requests.post(
            "http://localhost:8000/chat", json={"query": query}
        ).json()
        st.session_state.history.append((query, resp["answer"]))

# Conversation history
for user, bot in st.session_state.history:
    st.markdown(f"**You:** {user}")
    st.markdown(f"**Assistant:** {bot}")

st.write("---")
st.write("Sample queries: Find Python devs with 3+ years; Who has worked on healthcare projects?; Suggest people for a React Native project")
