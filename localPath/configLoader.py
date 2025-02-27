import json
import git

# Load configuration from a JSON file
def loadConfig(configFile="config.json"):
    try:
        with open(configFile, "r") as file:
            config = json.load(file)
        return config.get("clone_path", "./")  # Default to current directory if not specified
    
    except Exception as e:
        print(f"Error loading config: {e}")
        return "./"