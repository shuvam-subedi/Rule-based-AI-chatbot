import random
from ddgs import DDGS
import re

def shortenText(text, maxSentenses=2):
    sentenses = re.split(r"(?<=[.!?])\s+", text.strip())
    return " ".join(sentenses[:maxSentenses])

def fetchFromInternet(query):
    try:
        results = list(DDGS().text(str(query), max_results=1))
        if results:
            shortBody = shortenText(results[0]["body"], maxSentenses=2)
            return f"{shortBody}\n(Source: {results[0]['href']})"
        else:
            return random.choice(["I couldn't find anything on the internet for that.", "Nothing relevant found. Please try again."])
    except Exception as e:
        print(f"Debug error: {e}")
        return random.choice(["Sorry, I am having trouble connecting to the internet right now.", "Couldn't connect to the internet.", "Internet connection failed."])
    