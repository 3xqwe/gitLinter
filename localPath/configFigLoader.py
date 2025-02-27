import json
import git

# Load configuration from a JSON file
def load_config(config_file="config.json"):
    try:
        with open(config_file, "r") as file:
            config = json.load(file)
        return config.get("clone_path", "./")  # Default to current directory if not specified
    except Exception as e:
        print(f"Error loading config: {e}")
        return "./"