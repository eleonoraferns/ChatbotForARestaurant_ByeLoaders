#pip install streamlit
import streamlit as st
from backend_code import create_langchain_agent

st.title("Swiggy Restaurant Dataset Analysis")

# Define a Streamlit function to interact with your agent
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

# You can add more Streamlit components and interactive elements as needed

