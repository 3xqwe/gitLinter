import os
from localPath.configLoader import configOpener

def checkWorkflows(repoPath):
    #Check if any GitHub Actions workflow files exist.
    workflowsPath = os.path.join(repoPath, ".github", "workflows")
    config=configOpener()
    
    if not os.path.exists(workflowsPath):
        if not config.get("allowFail", {}).get("workflow", False):
            print("\n\U0001F7E5 - Missing workflow. Create a workflow in .github/workflows.")
            return 1
        else:
            print("\n\U0001F7E8 - Missing workflow, but failure is allowed based on config.")
            return 0
        
    workflowFiles = [f for f in os.listdir(workflowsPath) if f.endswith(".yml") or f.endswith(".yaml")]
    if not workflowFiles:
        print ("\n\U0001F7E8 - Workflow folder exist but there is no workflow files. Add a workflow file (e.g., a YAML/YML file).")
        return 0
    
    print(f"\n\U0001F7E9 - Workflows OK. Workflow folder exists and has content.\nFound workflow file: {', '.join(workflowFiles)}")
    return 0
