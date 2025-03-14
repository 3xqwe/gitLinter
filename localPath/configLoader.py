import json
import git
import os

# Load configuration from a JSON file
def loadConfig(configFile="config.json"):
    try:
        with open(configFile, "r") as file:
            config = json.load(file)
        return config.get("clonePath", "./")  # Default to current directory if not specified
    
    except Exception as e:
        print(f"Error loading config: {e}")
        return "./"
    
def configOpener():
    with open("config.json", "r") as f:
        return json.load(f)
