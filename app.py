st.subheader("🎤 Voice Input")

if st.button("🎙️ Record from Microphone"):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("Listening... Speak now!")
        audio = r.listen(source, phrase_time_limit=5)

    try:
        prompt = r.recognize_google(audio)
        st.success(f"Recognized: {prompt}")
    except sr.UnknownValueError:
        st.error("Sorry, I couldn’t understand your voice.")
        prompt = ""
    except sr.RequestError:
        st.error("Voice recognition service unavailable.")
        prompt = ""
else:
    # If no voice, show regular input
    prompt = st.text_input("Type your message:")
