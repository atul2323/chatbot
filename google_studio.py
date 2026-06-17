from google import genai


client = genai.Client(api_key="AQ.Ab8RN6Jlzc8UZ_qyh_5jm9An9C2JE3BNa1T7iH-DcwiolOYLfA")

while True:
    text = input("You: ")

    if text.lower() == "bye":
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=text
    )

    print("Chatbot:", response.text)
