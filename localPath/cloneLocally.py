import git
import os
import json
import base64
import time
from localPath.configFigLoader import load_config

trackingFile = "clonedRepos.json"

def load_tracking_data():
    #Load existing tracking data or return an empty dictionary.
    if os.path.exists(trackingFile):
        try:
            with open(trackingFile, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: Tracking file is corrupted, starting fresh.")
    return {}

def save_tracking_data(data):
    #Save tracking data to cloned_repos.json.
    with open(trackingFile, "w") as file:
        json.dump(data, file, indent=4)

def generate_id():
    #Generate a Base64-encoded timestamp as a unique ID.
    timestamp = str(time.time()).encode("utf-8")
    return base64.urlsafe_b64encode(timestamp).decode("utf-8").rstrip("=")

def clone_github_repo(github_url):
    #Clone the repository into a unique folder and track it.
    base_path = load_config()  # Load base path from config file
    tracking_data = load_tracking_data()

    if not github_url:
        print("Error: No repository URL provided.")
        return

    # Generate a Base64-encoded timestamp ID for unique folder
    repo_id = generate_id()
    clone_path = os.path.join(base_path, f"repo_{repo_id}")

    try:
        os.makedirs(clone_path, exist_ok=True)  # Ensure the directory exists
        git.Repo.clone_from(github_url, clone_path)
        print(f"Repository cloned successfully to {clone_path}")

        # Update tracking data with repository details
        tracking_data[repo_id] = {
            "repo_url": github_url,
            "clone_path": clone_path
        }
        save_tracking_data(tracking_data)

        print(f"Repository tracked under ID: {repo_id}")
        return clone_path
    except Exception as e:
        print(f"An error occurred: {e}")