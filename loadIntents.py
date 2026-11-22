import json

def loadIntents(filepath = "./intents.json"):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: Could not find File at location: '{filepath}'.")
        return None
    except json.JSONDecodeError:
        print(f"Error: 'Location :'{filepath}' contains invalid JSON.")
        return None