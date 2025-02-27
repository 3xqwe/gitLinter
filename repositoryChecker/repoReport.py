from functionsImport import getCommitCount
from functionsImport import checkReadme
from functionsImport import checkLicense
from functionsImport import checkGitignore
from functionsImport import checkWorkflows

def detailedSummaryRepo(userInput):

    print("\nThe number of commits in the repository:",getCommitCount(userInput),"\n")
    print("\n---Checking for best practices. ---\n")
    print(checkReadme(userInput),"\n")
    print(checkLicense(userInput),"\n")
    print(checkGitignore(userInput),"\n")
    print(checkWorkflows(userInput),"\n")