import json
import random
import re

with open("./intents.json") as file:
    intents = json.load(file)

def getResponse(userInput):
    userInput = userInput.lower().strip()
    fallbackResponse = []

    for intent in intents["intents"]:
        if intent["tag"] == "fallback":
            fallbackResponse = intent["responses"]
            continue
        for pattern in intent["patterns"]:
            regex = r"\b" + re.escape(pattern.lower().strip()) + r"\b"
            if re.search(regex, userInput):
                return intent["tag"], random.choice(intent["responses"])

    return "fallback", random.choice(fallbackResponse)