import os

def findTestFiles(repoPath):
    from repositoryChecker.gitignoredFiles import (getGitignorePatterns,isIgnored)
    from localPath.configLoader import configOpener
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
    
    config=configOpener()

    if not testFiles:
        if not config.get("allowFail", {}).get("test", False):
            print("\n\U0001F7E5 - Missing test file. It is required to have test files.")
            return 1  
        else:
            print("\n\U0001F7E8 - Missing test file, but failure is allowed based on config.")
            return 0  

    else:
        print("\n\U0001F7E9 - Test files/folders existed.")
        print("Found test files/folders:")
        for path in testFiles:
            print(path)
        return 0