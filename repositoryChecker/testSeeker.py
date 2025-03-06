import os

def findTestFiles(repoPath):
    from repositoryChecker.gitignoredFiles import (getGitignorePatterns,isIgnored)

    # Finds test files and directories, excluding ignored files.
    testFiles = []
    ignoredPatterns = getGitignorePatterns(repoPath)
    
    for root, dirs, files in os.walk(repoPath):
        if isIgnored(root, ignoredPatterns):
            continue
        
        for file in files:
            if file.startswith("test"):
                filePath = os.path.join(root, file)
                if not isIgnored(filePath, ignoredPatterns):
                    testFiles.append(filePath)
        
        for directory in dirs:
            if directory.startswith("test"):
                dirPath = os.path.join(root, directory)
                if not isIgnored(dirPath, ignoredPatterns):
                    testFiles.append(dirPath)
    
    return testFiles