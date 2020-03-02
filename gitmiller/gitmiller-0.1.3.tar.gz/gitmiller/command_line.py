import argparse
import base64
import getpass
import itertools
import json
import os
import re
import shutil
import sys
import tempfile
import urllib
import yaml

from pathlib import Path
from tqdm import tqdm

import papermill as pm

import github


def get_from_github(
    repo_url, 
    username, 
    password, 
    notebook, 
    output_path, 
    config):

    # these are parameters that need to be injected by papermill
    papermill_parameters = {}

    # load config file 
    if config:
        with open(config) as file:
            # load config file
            pars = yaml.load(file, Loader=yaml.FullLoader)
            # load repo_url, username, password, notebook,
            # output_path and papermill parameters
            repo_url = pars.get('repository') or repo_url
            username = pars.get('username') or username
            password = pars.get('password') or password
            notebook = pars.get('notebook') or notebook
            output_path = pars.get('output') or output_path
            papermill_parameters = pars.get('papermill', {})

    # handle github repo by url
    parsed_url = urllib.parse.urlparse(repo_url)
    split_path = [x for x in parsed_url.path.split('/') if x != '']
    target_repo = '/'.join(split_path[0:2])

    # checking for single file downloading
    if len(split_path) > 2 and split_path[2] == 'blob':
        msg = 'You are trying to download a single file from a repository.\n' + \
            'Please select the entire repository, or a repository folder.'
        print(msg)
        return False

    # login and find repo
    g = github.Github(username, password)

    # access repo
    repo = False 
    try:
        repo = g.get_repo(target_repo)
    except github.GithubException as e:
        msg = 'There is a problem with Github repo {}\nMessage: {}.'.format(
            repo_url, 
            e.data['message']
        )
        print(msg)
        return False

    # maybe this is about a different branch, and/or a subfolder
    branches = [b.name for b in repo.get_branches()]
    # contents defaults: everything from master-branch
    contents_path = '.'
    branch = 'master'
    # try to match /tree/.../ in repo url to check if we need 
    # special stuff
    try:
        branch = re.search(r'\/tree\/(.+?)\/', repo_url).group(1)
        if branch in branches:
            # change branche
            contents_path = '/'.join(split_path[4:])
    except:
        pass

    # copy them in correct dir-structure in tmp
    sys_temp = tempfile.gettempdir()
    root_path = Path(sys_temp).joinpath(target_repo)

    # collect the -names- of the repo tree
    all_files = []
    contents = repo.get_contents(contents_path, ref=branch)
    while contents:
        file_content = contents.pop(0)
        if file_content.type == 'dir':
            contents.extend(repo.get_contents(file_content.path))
        else:
            all_files.append(file_content)

    # progress bar to keep scientist occupied during downloading
    for f in tqdm(all_files, desc='Downloading repo'):

        # maybe these relative subdirs need to be created
        sub_dirs = Path(f.path).parent

        # make sure subfolders exist with respect to root dir
        # (create if necessary)
        new_dirs = Path(root_path).joinpath(sub_dirs)
        if not Path(new_dirs).exists():
            Path(new_dirs).mkdir(parents=True, exist_ok=True)

        # download and write this file
        file_data = base64.b64decode(f.content)  # this is bytecode
        file_out = open(Path(root_path).joinpath(f.path), 'wb')
        file_out.write(file_data)
        file_out.close()

    # try to execute notebook
    try:
        # change directory to execute notebook
        working_dir = Path(root_path).joinpath(contents_path)
        os.chdir(working_dir)

        # at this stage all repo files are downloaded in the tmp dir
        # now we have to run the notebook
        pm.execute_notebook(
            str(Path(working_dir).joinpath(notebook)),
            str(Path(output_path).joinpath(notebook)),
            parameters = papermill_parameters
        )

    except FileNotFoundError as e:
        # check if notebook exists in repo, if not return with False
        if not(Path(root_path).joinpath(notebook).is_file()):
            msg = 'Notebook "{}" could not be found in repo {}'.format(
                notebook,
                repo_url
            )
            print(msg)
        print(e)

    finally:
        # let's clean up the mess
        remove_path = Path(sys_temp).joinpath(split_path[0])
        shutil.rmtree(remove_path)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', action='store', help='Github username')
    parser.add_argument('-p', '--password', action='store', help='Github password')
    parser.add_argument('-r', '--repository', action='store', help='Github repo')
    parser.add_argument('-n', '--notebook', action='store', 
        help='Notebook to run, should be in root folder of Github repo')
    parser.add_argument('-o', '--output', action='store', 
        help='Folder in which the executed Notebook should be put')
    parser.add_argument('-c', '--config', action='store', 
        help='Path to yaml file containing GitMiller script parameters and inlog parameters')


    args = parser.parse_args()

    # intercept repo, if model 

    get_from_github(
        args.repository,
        args.username,
        args.password,
        args.notebook,
        args.output,
        args.config
    )



if __name__ == '__main__':
    main()