
def detailedSummaryRepo(userInput):
    from functionsImport import (checkReadme, checkLicense, checkGitignore, checkWorkflows, findTestFiles)
    from repositoryChecker.contributors import summarizeContributors

    summarizeContributors(userInput)
    print("\n---Checking for best practices. ---")
   
    # Collect the exit codes
    exitCode = 0
    
    # Run checks and updates the exit code if necessary
    exitCode|=checkReadme(userInput)
    exitCode|=checkLicense(userInput)
    exitCode|=checkGitignore(userInput)
    exitCode|=checkWorkflows(userInput)
    exitCode|=findTestFiles(userInput)
    
    return exitCode