import requests
from openai_client import chat_with_openai

def detect_intent(prompt):
    if "weather" in prompt.lower():
        words = prompt.lower().split()
        for i, word in enumerate(words):
            if word == "in" and i + 1 < len(words):
                return {"intent": "weather_lookup", "city": words[i+1]}
    return {"intent": "unknown"}

def call_mcp(intent_data):
    response = requests.post("http://localhost:5005/resolve_context", json=intent_data)
    return response.json()

def main():
    user_prompt = input("Ask a question: ")
    intent_data = detect_intent(user_prompt)

    if intent_data["intent"] == "weather_lookup":
        context = call_mcp(intent_data)
        enriched_prompt = f"The user asked: '{user_prompt}'. The weather data is: {context['result']}."
    else:
        enriched_prompt = user_prompt

    print("\n📤 Sending to OpenAI...")
    reply = chat_with_openai(enriched_prompt)
    print("\n🤖 OpenAI says:", reply)

if __name__ == "__main__":
    main()
