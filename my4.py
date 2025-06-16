import os
import streamlit as st
from dotenv import load_dotenv
from litellm import completion

# Load the .env API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

st.set_page_config(page_title="Gemini Q&A", page_icon="🤖")
st.title("💬 Ask Gemini Anything 4")

# Input prompt from user
prompt = st.text_input("Enter your question:")

if st.button("Ask Gemini"):
    if not api_key:
        st.error("API key not found. Please check your .env file.")
    elif not prompt.strip():
        st.warning("Please enter a valid question.")
    else:
        try:
            # Send request to Gemini
            response = completion(
                model="gemini/gemini-2.0-flash",
                api_key=api_key,
                messages=[{"role": "user", "content": prompt}]
            )
            answer = response['choices'][0]['message']['content']
            st.success("✅ Gemini says:")
            st.markdown(answer)

        except Exception as e:
            st.error("❌ Error communicating with Gemini.")
            st.code(str(e))
