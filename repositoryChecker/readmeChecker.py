import os
def checkReadme(repoPath):
    #Check if README.md exists and is not empty in any subdirectory.
    readmeFiles = []
    
    # Traverse the repository using os.walk
    for root, dirs, files in os.walk(repoPath):
        if "README.md" in files:
            readmePath = os.path.join(root, "README.md")
            readmeFiles.append(readmePath)
            print(f"Found README file: {readmePath}")
    if not readmeFiles:
        return "Missing README.md file. Create a README.md file to provide project description and installation instructions."
    
    if len(readmeFiles) > 1:
        return "Multiple README.md files. There should be only one README.md file in the repository."


    # Check if README.md is empty
    with open(readmeFiles[0],'r') as file:
        content = file.read().strip()  # Strip whitespace and check if the file is empty
        if not content:
            return "Empty README.md file. README.md file exist but is empty. Add relevant project information."
    
    return "README.md OK. README.md file exists and has content."
