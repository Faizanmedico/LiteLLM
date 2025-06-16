import json

# Add a horizontal line
st.markdown("---")

# Convert chat history to plain text
def get_text_log():
    lines = []
    for msg in st.session_state.chat_history:
        role = "You" if msg["role"] == "user" else "Gemini"
        lines.append(f"{role}: {msg['content']}\n")
    return "\n".join(lines)

# Create download buttons
if st.session_state.chat_history:
    txt_log = get_text_log()
    json_log = json.dumps(st.session_state.chat_history, indent=2)

    col1, col2 = st.columns(2)
    with col1:
        st.download_button(
            label="⬇️ Download as TXT",
            data=txt_log,
            file_name="chat_history.txt",
            mime="text/plain"
        )
    with col2:
        st.download_button(
            label="⬇️ Download as JSON",
            data=json_log,
            file_name="chat_history.json",
            mime="application/json"
        )
