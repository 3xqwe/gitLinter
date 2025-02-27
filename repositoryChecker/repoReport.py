
def detailedSummaryRepo(userInput):
    from functionsImport import (checkReadme, checkLicense, checkGitignore, checkWorkflows, findTestFiles, getCommitCount)

    print("\nThe number of commits in the repository:",getCommitCount(userInput),"\n")
    print("\n---Checking for best practices. ---\n")
    print(checkReadme(userInput),"\n")
    print(checkLicense(userInput),"\n")
    print(checkGitignore(userInput),"\n")
    print(checkWorkflows(userInput),"\n")
    testFiles=findTestFiles(userInput)
    
    if testFiles:
        print("Found test files/folders:")
        for path in testFiles:
            print(path)
        print("\U0001F7E9 - Test files/folders existed.")
    else:
        print("\U0001F7E8 - No test files/folders found.\n")
