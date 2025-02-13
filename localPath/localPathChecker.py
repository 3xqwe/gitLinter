import os
def is_git_repo(path):
    git_dir = os.path.join(path, '.git')
    return os.path.isdir(git_dir)


