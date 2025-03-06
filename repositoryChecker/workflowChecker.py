import os

def checkWorkflows(repoPath):
    #Check if any GitHub Actions workflow files exist.
    workflowsPath = os.path.join(repoPath, ".github", "workflows")
    if not os.path.exists(workflowsPath):
        print("\n\U0001F7E5 - Missing workflow folder. Create a workflow in .github/workflows.")
        return workflowsPath
    
    workflowFiles = [f for f in os.listdir(workflowsPath) if f.endswith(".yml") or f.endswith(".yaml")]
    if not workflowFiles:
        print ("\n\U0001F7E8 - Workflow folder exist but there is no workflow files. Add a workflow file (e.g., a YAML/YML file).")
        return workflowsPath
    
    print(f"\n\U0001F7E9 - Workflows OK. Workflow folder exists and has content.\nFound workflow file: {', '.join(workflowFiles)}")
    return workflowsPath
