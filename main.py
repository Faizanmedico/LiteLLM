import os
from litellm import completion
from dotenv import load_dotenv

# Load the API key from .env file
load_dotenv()

def main():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("❌ Error: API key not found. Check your .env file.")
        return

    # Ask the user for a question
    user_input = input("❓ Ask anything: ").strip()

    if not user_input:
        print("⚠️ No input provided. Exiting.")
        return

    try:
        # Send prompt to Gemini
        response = completion(
            model="gemini/gemini-2.0-flash",
            api_key=api_key,
            messages=[
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )

        # Show model response
        print("\n✅ Gemini says:\n", response['choices'][0]['message']['content'])

    except Exception as e:
        print("❌ Failed to get a response.")
        print("🧵 Error:", e)

# Entry point
if __name__ == "__main__":
    main()
