from functionsImport import*

print("\n-----Welcome to gitLinter-----\n")
userInput = input("Please specify Github URL or local path to repository: ")

if userInput.startswith(('http://', 'https://')):
    if urlChecker(userInput) is True:
        if is_url_repo(userInput):
            print("Valid Github repository URL")
            userInput = clone_github_repo(userInput)
        else:
            print("Not valid Github repository")
    else:
        print("Not a valid Github URL")

elif os.path.isdir(userInput):
    if is_git_repo(userInput):
        print(f"The directory at {userInput} is a Git repository.")

    else:
        print(f"The directory at {userInput} is not a valid Git repository")
else:
    print("Input is not a GitHub URL or a local repository")

print("\n---Checking for best practices. ---\n")
print(checkReadme(userInput),"\n")
print(checkLicense(userInput),"\n")
print(checkGitignore(userInput),"\n")