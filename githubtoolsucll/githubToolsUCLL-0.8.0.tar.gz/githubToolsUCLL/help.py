import sys
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path+"/..")


def main():
    print(
    """
    createToken: places the given GitHub token in the correct place
    pullIssues: pulls all issues from one repo to another
    pushIssues: pushes selected issues from one repo to all repos in an assignment
    cloneRepos: clones all GitHub repositories from an assignment to newly created correctly named local folders
    createIssue: creates a single issue in a repository
    issuesToFile: copies all issues from a repository to a YAML file
    fileToIssues: copies all issues from a YAML file to a GitHub repository
    githubToolsUcll: shows this help page
    """
    )

if __name__ == '__main__':
    main()
