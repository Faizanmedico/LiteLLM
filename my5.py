# --- Download Section ---
import json

def get_text_log():
    lines = []
    for msg in st.session_state.chat_history:
        role = "You" if msg["role"] == "user" else "Gemini"
        lines.append(f"{role}: {msg['content']}\n")
    return "\n".join(lines)

if st.session_state.chat_history:
    txt_log = get_text_log()
    json_log = json.dumps(st.session_state.chat_history, indent=2)

    col1, col2 = st.columns(2)
    with col1:
        st.download_button("⬇️ Download as TXT", txt_log, "chat_history.txt", "text/plain")
    with col2:
        st.download_button("⬇️ Download as JSON", json_log, "chat_history.json", "application/json")

    # 🧹 Clear Chat Button
    if st.button("🧹 Clear Chat"):
        st.session_state.chat_history = []
        st.experimental_rerun()
