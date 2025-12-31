

import requests


API_KEY = "AIzaSyCvvkKuAMoQNrXFxsHbpUysKwTIjj_eOhw"


url = "https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key=" + API_KEY

prompt = input(str("Chat-bot:"))

body = {
    "contents": [
        {
            "parts": [
                {"text": prompt}
            ]
        }
    ]
}

response = requests.post(url, json=body)

if response.status_code == 200:
    data = response.json()
    text = data["candidates"][0]["content"]["parts"][0]["text"]
    print("\nResponse:\n")
    print(text)
else:
    print("Error:", response.text)


# python chat bot
# using 
# google 
# gemini
# gen 
# API
#call
#postman
#python 
#chat
#bot

#gamini
#ai