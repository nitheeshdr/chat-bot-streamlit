import streamlit as st
import google.generativeai as genai

# Set your Gemini API key
GEMINI_API_KEY = "AIzaSyB2_Agj5KlfFhVQCJSw9xT0soRltapmTP4"  # Use st.secrets["GEMINI_API_KEY"] in production
genai.configure(api_key=GEMINI_API_KEY)

st.title("💬 Gemini Flash 2.5 Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Clear chat button
if st.button("🧹 Clear Chat"):
    st.session_state.messages = []
    st.experimental_rerun()

# Chat input
if prompt := st.chat_input("Say something..."):
    # Show user input
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        with st.spinner("Thinking..."):
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)

        # Show response
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})

    except Exception as e:
        error_msg = f"❌ Error: {e}"
        with st.chat_message("assistant"):
            st.markdown(error_msg)
        st.session_state.messages.append({"role": "assistant", "content": error_msg})
