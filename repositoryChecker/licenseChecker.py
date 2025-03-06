import os
def checkLicense(repoPath):
    from repositoryChecker.gitignoredFiles import (getGitignorePatterns,isIgnored)

    # Check if exactly one LICENSE file exists and is not empty in any subdirectory.
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
    
    if not licenseFile:
        print("\n\U0001F7E5 - Missing LICENSE file. Create a LICENSE file to define the terms of use for the project.")
        return licenseFile
    
    with open(licenseFile[0], 'r') as file:
        content = file.read().strip()
        if not content:
            print("\n\U0001F7E8 - Empty LICENSE file. The LICENSE file exists but is empty. Add the appropriate licensing terms (e.g. MIT).")
            return licenseFile
    
    print("\n\U0001F7E9 - LICENSE OK. LICENSE file exists and has content.")
    print("Found LICENSE file:")
    for files in licenseFile:
        print(f"{files}")
    
    return licenseFile