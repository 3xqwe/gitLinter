
def detailedSummaryRepo(userInput):
    from functionsImport import (checkReadme, checkLicense, checkGitignore, checkWorkflows, findTestFiles)
    from repositoryChecker.contributors import summarizeContributors

    summarizeContributors(userInput)
    print("\n---Checking for best practices. ---")
    checkReadme(userInput)
    checkLicense(userInput)
    checkGitignore(userInput)
    checkWorkflows(userInput)
    testFiles=findTestFiles(userInput)
    
    if testFiles:
        print("\n\U0001F7E8 - Test files/folders existed.")
        print("Found test files/folders:")
        for path in testFiles:
            print(path)

    else:
        print("\n\U0001F7E8 - No test files/folders found.\n")