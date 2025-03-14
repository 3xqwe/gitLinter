import os
import subprocess

def summarizeContributors(repoPath):
    try:
        # First check if the repository has any commits by running git log
        command = ["git", "log", "--oneline", "-n", "1"]  # Just get the first commit
        result = subprocess.run(command, cwd=repoPath, capture_output=True, text=True)

        # Check if repository is empty
        if result.returncode != 0:
            print("No commits found. The repository is empty or has no commits.")
            return
        
        # Get total number of commits
        command = ["git", "rev-list", "--count", "HEAD"]
        result = subprocess.run(command, cwd=repoPath, capture_output=True, text=True)

        if result.returncode == 0:
            totalCommits = int(result.stdout.strip())
        else:
            print("Failed to retrieve total commits.")
            return

        # If there are commits, proceed to summarize contributors
        command = ["git", "shortlog", "-s", "-n"]  # -s for count, -n for sorting by commit count
        result = subprocess.run(command, cwd=repoPath, capture_output=True, text=True)

        if result.returncode == 0:
            # Process the output of git shortlog if successful
            if result.stdout.strip():
                print("\n--- Git Contributors Summary ---")
                print(f"Total number of commits: {totalCommits}\n")
                print("Number of commits - Git name")
                contributors = result.stdout.strip().splitlines()
                for contributor in contributors:
                    print(contributor)
        else:
            print("Failed to retrieve contributors.")

    except Exception as e:
        print(f"An error occurred while retrieving contributors: {e}")
