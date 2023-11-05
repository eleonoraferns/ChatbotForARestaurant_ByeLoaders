import streamlit as st
from backend_code import create_csv_agent

st.title("RestoBot")

# Create a text input box to enter the URL
url = st.text_input("Enter a URL")

# Check if the URL is not empty
if url:
   ## st.write("You entered the following URL:")
    st.write(url)
    def ask_question(question, agent):
    response = agent.run(question)
    return response

# User input
user_question = st.text_input("Ask a question:")

# Button to trigger the question and get the answer
if st.button("Ask"):
    if user_question:
        agent = create_langchain_agent()  # Create a new agent for each question (you can optimize this)
        answer = ask_question(user_question, agent)
        st.write(f"Answer: {answer}")