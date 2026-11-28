import random
from ddgs import DDGS


def fetchFromInternet(query):
    try:
        results = list(DDGS().text(str(query), max_results=1))
        if results:
            return f"{results[0]['body']} (Source: {results[0]['href']})"
        else:
            return random.choice(["I couldn't find anything on the internet for that.", "Nothing relevant found. Please try again."])
    except Exception as e:
        print(f"Debug error: {e}")
        return random.choice(["Sorry, I am having trouble connecting to the internet right now.", "Couldn't connect to the internet.", "Internet connection failed."])
    