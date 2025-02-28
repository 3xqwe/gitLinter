import os

def checkWorkflows(repoPath):
    #Check if any GitHub Actions workflow files exist.
    workflowsPath = os.path.join(repoPath, ".github", "workflows")
    if not os.path.exists(workflowsPath):
        return "\U0001F7E5 - Missing workflow folder. Create a workflow in .github/workflows."
    
    workflowFiles = [f for f in os.listdir(workflowsPath) if f.endswith(".yml") or f.endswith(".yaml")]
    if not workflowFiles:
        return "\U0001F7E8 - Workflow folder exist but there is no workflow files. Add a workflow file (e.g., a YAML/YML file)."
    
    return f"\U0001F7E9 - Workflows OK. Workflows found: {', '.join(workflowFiles)}"
