import os
from localPath.configLoader import configOpener

def checkReadme(repoPath):
    #Check if README.md exists and is not empty in any subdirectory.
    readmeFiles = []
    
    # Traverse the repository using os.walk
    for root, dirs, files in os.walk(repoPath):
        if "README.md" in files:
            readmePath = os.path.join(root, "README.md")
            readmeFiles.append(readmePath)
    config=configOpener()

    if not readmeFiles:
        if not config.get("allowFail", {}).get("README", False):
            print("\n\U0001F7E5 - Missing README.md file. Create a README.md file to provide project description and installation instructions.")
            return 1
        else:
            print("\n\U0001F7E8 - Missing README.md file, but failure is allowed based on config.")
            return 0
    
    if len(readmeFiles) > 1:
        print("\n\U0001F7E8 - Multiple README.md files. There should be only one README.md file in the repository.")
        for files in readmeFiles:
            print (files)
        return 0
    
    # Check if README.md is empty
    with open(readmeFiles[0],'r') as file:
        content = file.read().strip()  # Strip whitespace and check if the file is empty
        if not content:
            print("\n\U0001F7E8 - Empty README.md file. README.md file exist but is empty. Add relevant project information.")
            return 0
    
    print("\n\U0001F7E9 - README.md OK. README.md file exists and has content.")
    print(f"Found README file:\n{readmePath}")
    return 0
 
    