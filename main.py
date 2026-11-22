from getResponse import getResponse

print("Bot: Hi! Type 'bye' to exit.")
while True:
    userInput = input("You: ")
    tag, reply = getResponse(userInput)
    print(f"Bot: {reply}")
    if tag == "exit":
        break