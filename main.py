import os
from url.urlChecker import *
from localPath.localPathChecker import *
from localPath.cloneLocally import *
from url.urlRepo import *

userInput = input("Please specify Github URL or local path to repository: ")

if userInput.startswith(('http://', 'https://')):
    if urlChecker(userInput) is True:
        if is_url_repo(userInput):
            print("Valid Github repository URL")
            localPathInput= input("Enter the local path to where you want the cloned repository: ")
            clone_github_repo(userInput,localPathInput)
        else:
            print("Not valid Github repository")
    else:
        print("Not a valid Github URL")

elif os.path.isdir(userInput):
    if is_git_repo(userInput):
        print(f"The directory at {userInput} is a Git repository.")

    else:
        print(f"The directory at {userInput} is not a valid Git repository")
else:
    print("Input is not a GitHub URL or a local repository")



