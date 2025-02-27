import git
import os
import json
import base64
import time
from localPath.configLoader import loadConfig

trackingFile = "clonedRepos.json"

def loadTrackingData():
    #Load existing tracking data or return an empty dictionary.
    if os.path.exists(trackingFile):
        try:
            with open(trackingFile, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: Tracking file is corrupted, starting fresh.")
    return {}

def saveTrackingData(data):
    #Save tracking data to cloned_repos.json.
    with open(trackingFile, "w") as file:
        json.dump(data, file, indent=4)

def generateID():
    #Generate a Base64-encoded timestamp as a unique ID.
    timestamp = str(time.time()).encode("utf-8")
    return base64.urlsafe_b64encode(timestamp).decode("utf-8").rstrip("=")

def cloneGithubRepo(githubUrl):
    #Clone the repository into a unique folder and track it.
    basePath = loadConfig()  # Load base path from config file
    trackingData = loadTrackingData()

    # Generate a Base64-encoded timestamp ID for unique folder
    repoID = generateID()
    clonePath = os.path.join(basePath, f"repo_{repoID}")

    try:
        os.makedirs(clonePath, exist_ok=True)  # Ensure the directory exists
        git.Repo.clone_from(githubUrl, clonePath)
        print(f"Repository cloned successfully to {clonePath}")

        # Update tracking data with repository details
        trackingData[repoID] = {
            "repo_url": githubUrl
        ,
            "clonePath": clonePath
        }
        saveTrackingData(trackingData)

        print(f"Repository tracked under ID: {repoID}")
        return clonePath
    except Exception as e:
        print(f"An error occurred: {e}")