import git

def getCommitCount(repoPath):
    try:
        # Open the repository using GitPython
        repo = git.Repo(repoPath)
        
        # Get the list of commits in the repository
        commits = list(repo.iter_commits())
        
        # Return the number of commits
        return len(commits)
    
    except Exception as e:
        print(f"Error: {e}")
        return 0
