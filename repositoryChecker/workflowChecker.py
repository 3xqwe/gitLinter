import os

def check_workflows(repoPath):
    #Check if any GitHub Actions workflow files exist.
    workflowsPath = os.path.join(repoPath, ".github", "workflows")
    if not os.path.exists(workflowsPath):
        return "Missing workflow. Create a workflow in .github/workflows."
    
    workflowFiles = [f for f in os.listdir(workflowsPath) if f.endswith(".yml") or f.endswith(".yaml")]
    if not workflowFiles:
        return "No workflow files", "Add a workflow file (e.g., a YAML/YML file)."
    
    return f"Workflows OK. Workflows found: {', '.join(workflowFiles)}"
