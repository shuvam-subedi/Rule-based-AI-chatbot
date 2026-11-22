import random
import re
from loadIntents import loadIntents
import sys

def getResponse(userInput):
    intents = loadIntents("./intents.json")
    if intents == None:
        sys.exit()
    
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