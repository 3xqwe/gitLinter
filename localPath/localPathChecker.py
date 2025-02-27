import os
def isGitRepo(path):
    gitDir = os.path.join(path, '.git')
    return os.path.isdir(gitDir)


