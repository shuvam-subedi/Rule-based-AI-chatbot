import random
from loadIntents import loadIntents
from preProcessing import preProcessing
import sys
from rapidfuzz import fuzz

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

    if bestIntent and bestScore >= 0.7:
        return bestIntent["tag"], random.choice(bestIntent["responses"])

    return "fallback", random.choice(fallbackResponse)