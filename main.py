from functionsImport import *

print("\n-----Welcome to gitLinter-----\n")
validInput=False

while not validInput:

    userInput = input("Please specify Github URL or local path to repository: ")
    if userInput.startswith(('http://', 'https://')):
        if urlChecker(userInput) is True:
            if isUrlRepo(userInput):
                print("Valid Github repository URL")
                userInput = cloneGithubRepo(userInput)
                validInput = True
            else:
                print("Not valid Github repository, try again.")
        else:
            print("Not a valid Github URL, try again.")

    elif os.path.isdir(userInput):
        if isGitRepo(userInput):
            print(f"The directory at {userInput} is a Git repository")
            validInput = True

        else:
            print(f"The directory at {userInput} is not a valid Git repository, try again.")

    else:
        print("Input is not a GitHub URL or a local repository, try again.")

detailedSummaryRepo(userInput)
print("\n-----Run complete-----\n")