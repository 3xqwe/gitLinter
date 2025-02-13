import requests

def is_url_repo(url):
    
    # Remove the https://github.com/ prefix to extract the user/repo path
    repo_path = url[len('https://github.com/'):]

    # Split the path into user and repository name
    parts = repo_path.split('/')
    if len(parts) != 2:
        return False

    user = parts[0]
    repo = parts[1]

    # Construct the API URL
    api_url = f'https://api.github.com/repos/{user}/{repo}'

    # Send a GET request to the GitHub API
    response = requests.get(api_url)

    # Check if the repository exists
    if response.status_code == 200:
        return True
    else:
        return False