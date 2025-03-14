import subprocess
from localPath.configLoader import configOpener

def run_gitleaks(repo_path):
    print("\n-----Starting Gitleaks scan on repository-----")
    
    # Print what secrets Gitleaks will check for
    print("\nGitleaks is checking for the following types of secrets:")
    print("- API Keys")
    print("- Passwords")
    print("- Tokens (OAuth, etc.)")
    print("- SSH Keys")
    print("- Private Keys")
    print("- Database credentials\n")

    # Full path to gitleaks
    gitleaks_path = "/usr/local/bin/gitleaks"

    try:
        # Run the Gitleaks command with verbose flag for detailed output
        result = subprocess.run(
            [gitleaks_path, "detect", "--source", repo_path, "--no-color", "--no-banner", "--verbose"],
            capture_output=True,
            text=True
        )
        config=configOpener()
        
        # Print standard output (the Gitleaks results)
        if result.stdout:
            if not config.get("allowFail", {}).get("secrets", False):
                print("\U0001F7E5 - GitLeaks found the following secrets: \n")
                print(result.stdout)
                return 1
            else:
                print("\U0001F7E8 - GitLeaks found secrets but failure is allowed based on config.\n")
                print(result.stdout)
                return 0
        
        else:
            print("\U0001F7E9 - GitLeaks did not find anything")
            return 0
            
    except Exception as e:
        print(f"Error running Gitleaks: {e}")

