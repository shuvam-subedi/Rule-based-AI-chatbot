import random
from loadIntents import loadIntents
from preProcessing import preProcessing
import sys
from rapidfuzz import fuzz
from fetch import fetchFromInternet

def getResponse(userInput):
    intents = loadIntents("./intents.json")
    if intents is None:
        sys.exit()
    
    userInput = preProcessing(userInput)
    fallbackResponse = []

    bestScore = 0
    bestIntent = None

    for intent in intents["intents"]:
        if intent["tag"] == "fallback":
            fallbackResponse = intent["responses"]
            continue

        for pattern in intent["patterns"]:
            score = fuzz.WRatio(userInput, pattern)
            if score > bestScore:
                bestScore = score
                bestIntent = intent

    if bestIntent and bestScore >= 70:
        if bestIntent["tag"] == "internetTrigger":
            for pattern in bestIntent["patterns"]:
                userInput = userInput.replace(preProcessing(pattern), "").strip()
            return bestIntent["tag"], fetchFromInternet(userInput)
        
        return bestIntent["tag"], random.choice(bestIntent["responses"])

    return "fallback", random.choice(fallbackResponse)