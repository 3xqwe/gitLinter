import os
def checkLicense(repoPath):
    from repositoryChecker.gitignoredFiles import (getGitignorePatterns,isIgnored)
    from localPath.configLoader import configOpener

    # Find all LICENSE files and check if any are empty
    licenseFile = []
    ignoredPatterns = getGitignorePatterns(repoPath)

    for root, _, files in os.walk(repoPath):
        if isIgnored(root, ignoredPatterns):
            continue
        
        for file in files:
            if file == "LICENSE":
                licensePath = os.path.join(root, "LICENSE")
                if not isIgnored(licensePath, ignoredPatterns):
                    licenseFile.append(licensePath)

    config=configOpener()

    if not licenseFile:
        if not config.get("allowFail", {}).get("license", False):
            print("\n\U0001F7E5 - Missing LICENSE file. Create a LICENSE file to define the terms of use for the project.")
            return 1
        else:
            print("\n\U0001F7E8 - Missing LICENSE file, but failure is allowed based on config.")
            return 0
    
    # Check all LICENSE files for empty content
    emptyFiles = []
    for licensePath in licenseFile:
        with open(licensePath, 'r') as file:
            content = file.read().strip()
            if not content:
                emptyFiles.append(licensePath)
    
    if emptyFiles:
        print("\n\U0001F7E8 - Empty LICENSE files. The following LICENSE files exist but are empty:")
        for empty in emptyFiles:
            print(f"{empty}")
        return 0
    
    print("\n\U0001F7E9 - LICENSE OK. LICENSE file exists and has content.")
    print("Found LICENSE file:")
    for files in licenseFile:
        print(f"{files}")
    
    return 0