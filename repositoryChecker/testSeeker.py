import os

def findTestFiles(repoPath):
    testFiles = []

    # Traverse all subdirectories
    for root, dirs, files in os.walk(repoPath):
        # Skip virtual environment files and then check for files starting with "test"
        #if "myenv" in root:  
            #continue

        for file in files:
            if file.startswith("test"):
                testFiles.append(os.path.join(root, file))
        
        # Check for directories named "test"
        for directory in dirs:
            if directory.startswith("test"):
                testFiles.append(os.path.join(root, directory))

    return testFiles