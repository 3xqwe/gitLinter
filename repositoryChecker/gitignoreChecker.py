import os

def checkGitignore(repoPath):
    #Check if .gitignore exists and is not empty in any subdirectory.
    gitignoreFiles = []
    
    # Traverse the repository using os.walk
    for root, dirs, files in os.walk(repoPath):
        if ".gitignore" in files:
            gitignorePath = os.path.join(root, ".gitignore")
            gitignoreFiles.append(gitignorePath)
            print(f"Found .gitignore file: {gitignorePath}")
            
    if not gitignoreFiles:
        return "\U0001F7E5 - Missing .gitignore file. Create a .gitignore file to exclude unnecessary files."
    
    # Check if any .gitignore is empty
    for files in gitignoreFiles:
        with open(files,'r') as file:
            content = file.read().strip()  # Strip whitespace and check if the file is empty
            if not content:
                return "\U0001F7E8 - Empty .gitignore file/files. Some .gitignore files exist but are empty."
    
    return "\U0001F7E9 - .gitignore OK. One or more .gitignore files exist and have content."
