def preProcessing(text):
    shortcuts = {
        "u": "you",
        "r": "are",
        "ur": "your",
        "urself": "yourself",
        "thx": "thanks",
        "im": "i am",
        "pls": "please",
        "idk": "i do not know",
        "i'm": "i am"
    }
    punctuation = ".,!?;:"
    result = []

    for word in text.lower().split():
        cleanWord = word.rstrip(punctuation)
        trailingPunctuation = word[len(cleanWord) : ]
        expandedWord = shortcuts.get(cleanWord, cleanWord) + trailingPunctuation
        result.append(expandedWord)

    return " ".join(result)