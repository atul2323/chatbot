from google import genai


client = genai.Client(api_key="AQ.Ab8RN6LG_Yzqa2NCoPD-M8T8ml_Yu1ZzWT1pVXfPphR85gnGow")

while True:
    text = input("You: ")

    if text.lower() == "bye":
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=text
    )

    print("Chatbot:", response.text)