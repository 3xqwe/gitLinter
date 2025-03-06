import os

def getGitignorePatterns(repoPath):
    # Reads .gitignore and returns a set of ignored patterns.
    gitignorePath = os.path.join(repoPath, ".gitignore")
    ignoredPatterns = set()
    
    if os.path.exists(gitignorePath):
        with open(gitignorePath, "r") as f:
            for line in f:
                pattern = line.strip()
                if pattern and not pattern.startswith("#"):  # Ignore comments
                    ignoredPatterns.add(pattern)
    
    return ignoredPatterns

def isIgnored(path, ignoredPatterns):
    # Checks if a path matches any .gitignore pattern.
    for pattern in ignoredPatterns:
        if pattern in path:
            return True
    return False