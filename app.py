
import streamlit as st
import google.generativeai as genai

# Set your Gemini API key here
# It's recommended to use Streamlit secrets for production
# For this example, we'll use the key directly from the user's input
# You can also set it as an environment variable: st.secrets["GEMINI_API_KEY"]
GEMINI_API_KEY = "AIzaSyB2_Agj5KlfFhVQCJSw9xT0soRltapmTP4"

genai.configure(api_key=GEMINI_API_KEY)

st.title("Gemini Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response.text)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"An error occurred: {e}")
        st.session_state.messages.append({"role": "assistant", "content": f"Error: {e}"})
