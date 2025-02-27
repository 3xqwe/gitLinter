import os

def checkLicense(repoPath):
    #Check if exactly one LICENSE file exists and is not empty in any subdirectory.
    licenseFile = []
    
    # Traverse the repository using os.walk
    for root, dirs, files in os.walk(repoPath):
        for file in files:
            if file=="LICENSE":
                licensePath = os.path.join(root, "LICENSE")
                licenseFile.append(licensePath)
                print(f"Found LICENSE file: {licensePath}")  

    # 
    # Check if no LICENSE file exists
    if not licenseFile:
        return "\U0001F7E5 - Missing LICENSE file. Create a LICENSE file to define the terms of use for the project."

    # Check if there is more than one LICENSE file
    if len(licenseFile) > 1:
        return "\U0001F7E8 - Multiple LICENSE files. There should be only one LICENSE file in the repository."

    # Check if the LICENSE file is empty
    with open(licenseFile[0], 'r') as file:
        content = file.read().strip()  # Strip whitespace and check if the file is empty
        if not content:
            return "\U0001F7E8 - Empty LICENSE file. The LICENSE file exists but is empty. Add the appropriate licensing terms (e.g. MIT)."

    return "\U0001F7E9 - LICENSE OK. LICENSE file exists and has content."
