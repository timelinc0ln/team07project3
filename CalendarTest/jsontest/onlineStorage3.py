import sys
import subprocess

GIT              = '/usr/bin/git'
GIT_BRANCH       = '/usr/lib/git-core/git-branch'
GIT_COMMIT       = '/usr/lib/git-core/git-commit'
GIT_CHECKOUT     = '/usr/lib/git-core/git-checkout'
GIT_CHERRY_PICK  = '/usr/lib/git-core/git-cherry-pick'

if __name__ == '__main__':

    branches = []
    git_args = []

    args = sys.argv[1:]

    while args:
        arg = args.pop(0)
        if arg in ('-b', '--branch'):
            branches.append(args.pop(0))
        elif arg.startswith('--branch='):
            branches.append(arg[9:])
        else:
            git_args.append(arg)

    # Find out the current branch
    current_branch = None
    local_branches = []
    p = subprocess.Popen([GIT_BRANCH], stdout=subprocess.PIPE)
    for line in p.stdout:
        branch = line[2:].strip()
        local_branches.append(branch)
        if line[0] != '*':
            continue
        current_branch = branch
    
    # Check to make sure that the provided branches are valid
    for branch in branches:
        if branch not in local_branches:
            sys.stderr.write('invalid branch: %s\n' % branch)
            sys.exit(1)

    # Perform the main commit
    p = subprocess.Popen([GIT_COMMIT] + git_args, stdout=subprocess.PIPE)
    if p.wait() > 0:
        sys.stdout.write(p.stdout.read())
        sys.exit(1)

    # Get the commit tag without using regex
    try:
        commit_tag = p.stdout.readline().split(' ')[1].split(']')[0]
    except:
        sys.stderr.write('unable to read commit tag\n')
        sys.exit(1)

    # Loop through the specified branches applying the commit to all of
    # them.
    for branch in branches:
        subprocess.call([GIT_CHECKOUT, branch])
        sys.stdout.write('Applying commit %s to %s\n' % (commit_tag, branch))
        subprocess.call([GIT_CHERRY_PICK, commit_tag], stdout=subprocess.PIPE)

    # Switch back to the original branch
    subprocess.call([GIT_CHECKOUT, current_branch])