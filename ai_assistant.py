import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Error: OPENAI_API_KEY is not set.")
    print("Create a .env file and add: OPENAI_API_KEY=your_key_here")
    raise SystemExit(1)

client = OpenAI(api_key=api_key)

print("=" * 55)
print("        Simple LLM API Command-Line Assistant")
print("=" * 55)
print("Type your question or instruction.")
print("Type 'exit' to close the program.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    if not user_input:
        print("Please enter a question or instruction.\n")
        continue

    try:
        response = client.responses.create(
            model="gpt-5.6-luna",
            input=user_input
        )

        print("\nAI:", response.output_text)
        print()

    except Exception as error:
        print("\nAPI Error:", error)
        print("Please check your API key, internet connection, and account access.\n")
