import os, subprocess

def summarizeContributors(repoPath):
    try:
        # Run "git shortlog" to get a summary of contributors
        command = ["git", "shortlog", "-s", "-n"]  # -s for count, -n for sorting by commit count
        result = subprocess.run(command, cwd=repoPath, capture_output=True, text=True)

        if result.returncode == 0:
            print("\n--- Git Contributors Summary ---")
            print("Number of commits - Git name")
            contributors = result.stdout.strip().splitlines()
            for contributor in contributors:
                print(contributor)

        else:
            print("Failed to retrieve contributors.")

    except Exception as e:
        print(f"An error occurred while retrieving contributors: {e}")