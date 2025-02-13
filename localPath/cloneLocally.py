import git

def clone_github_repo(github_url, local_path):
    try:
        #Clone the repository
        git.Repo.clone_from(github_url, local_path)
        print(f"Repository cloned successfully to {local_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
