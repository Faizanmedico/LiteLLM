import os
import streamlit as st
from dotenv import load_dotenv
from litellm import completion

# Load .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Streamlit page config
st.set_page_config(page_title="Gemini Chat", page_icon="🤖")
st.title("💬 Gemini ChatBot 2")

# Initialize chat history in session_state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display previous chat messages
for message in st.session_state.chat_history:
    if message["role"] == "user":
        st.markdown(f"👤 **You:** {message['content']}")
    else:
        st.markdown(f"🤖 **Gemini:** {message['content']}")

# Input area
prompt = st.text_input("Type your message:")

if st.button("Send"):
    if not api_key:
        st.error("Missing API key!")
    elif not prompt.strip():
        st.warning("Please enter a question.")
    else:
        try:
            # Save user message
            st.session_state.chat_history.append({"role": "user", "content": prompt})

            # Call Gemini
            response = completion(
                model="gemini/gemini-2.0-flash",
                api_key=api_key,
                messages=[
                    {"role": msg["role"], "content": msg["content"]}
                    for msg in st.session_state.chat_history
                ]
            )

            gemini_reply = response['choices'][0]['message']['content']
            # Save Gemini reply
            st.session_state.chat_history.append({"role": "assistant", "content": gemini_reply})

            # Refresh page to show new chat
            st.experimental_rerun()

        except Exception as e:
            st.error("Failed to get a response.")
            st.code(str(e))
