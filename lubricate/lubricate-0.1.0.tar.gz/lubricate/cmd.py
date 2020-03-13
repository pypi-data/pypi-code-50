#!/usr/bin/env python3
"""
The analysis lubricator.

Usage:
    lubricate [options] new TEMPLATE PROJECT_PATH
    lubricate templates
    lubricate (-h | --help)
    lubricate --version

Options:
    TEMPLATE      The template of the project to create [default: python].
    -h --help     Show this screen.
    -v            Verbose output.
    --version     Show the version.
"""
import os
import re
import shutil
import subprocess
import tempfile
import toml
from docopt import docopt

from . import plugins

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
TEMPLATES_PATH = os.path.join(BASE_PATH, "templates")
TEMPLATES = os.listdir(TEMPLATES_PATH)

TEMPLATE_PARAM_REGEX = r'{{: [a-zA-Z _\-\d]+ :}}+'


def extract_parameters(path):
    """Find all available parameters in a template path"""
    parameters = set()
    for path, dirs, files in os.walk(path, topdown=True):
        dirs[:] = [d for d in dirs if d not in [".git"]]
        for filename in files:
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()
            parameters = parameters.union(re.findall(TEMPLATE_PARAM_REGEX, s))
    return parameters


def set_values(path):
    """Traverses through all files and prompts the user for inputs"""
    parameters = extract_parameters(path)
    values = {}
    for parameter in parameters:
        values[parameter] = input("{}: ".format(parameter[4:-4]))
    for path, dirs, files in os.walk(path, topdown=True):
        dirs[:] = [d for d in dirs if d not in [".git"]]
        for filename in files:
            filepath = os.path.join(path, filename)
            for parameter in parameters:
                with open(filepath) as f:
                    s = f.read()
                if parameter not in s:
                    continue
                s = s.replace(parameter, values[parameter])
                with open(filepath, "w") as f:
                    f.write(s)


def initialise_project(path, template):
    """The main initialisation routine to create a project."""
    print("Bootstrapping a new {} project...".format(template))

    if os.path.exists(path):
        print("The folder named '{}' already exists, exiting." .format(path))
        exit(1)

    os.makedirs(path)

    tmpdir = tempfile.TemporaryDirectory()
    tmppath = os.path.join(tmpdir.name, "project")
    create_folder_structure(tmppath, template)

    try:
        settings = toml.load(os.path.join(tmppath, ".lubricate.toml"))
    except FileNotFoundError:
        settings = {}

    initialise_git(tmppath)
    set_values(tmppath)

    for f in os.listdir(tmppath):
        shutil.move(os.path.join(tmppath, f), path)
    tmpdir.cleanup()

    initialise_plugins(path, settings["plugins"])
    print("A new project was successfully initialised in '{}'.".format(path))


def initialise_plugins(path, plugin_list):
    for plugin in plugin_list:
        try:
            getattr(plugins, plugin)(path)
        except AttributeError:
            print("Plugin {} not found.".format(plugin))


def create_folder_structure(path, template):
    """Creates the folder structure in the given path"""
    template_path = os.path.join(TEMPLATES_PATH, template)
    shutil.copytree(template_path, path)


def _merge_folders(source, destination):
    """Copy all files to the destination and overwrite existing files."""
    for src_dir, dirs, files in os.walk(source):
        dst_dir = src_dir.replace(source, destination, 1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                os.remove(dst_file)
            shutil.copy(src_file, dst_dir)


def initialise_git(path):
    """Initialise a Git repository"""
    base_cmd = ["git", "-C", path]
    subprocess.run(base_cmd + ["init"])
    subprocess.run(base_cmd + ["add", "."])
    subprocess.run(base_cmd + ["commit", "-m", "Initial commit"])



def show_available_templates():
    """Print the available templates"""
    print("Available templates: {}".format(', '.join(TEMPLATES)))

def main():
    args = docopt(__doc__)

    if args['TEMPLATE'] not in TEMPLATES:
        print("'{}' project template is not supported.".format(args['TEMPLATE']))
        show_available_templates()
        exit(1)

    if args["--version"]:
        print(lc.version)

    if args["new"]:
        initialise_project(args["PROJECT_PATH"], template=args['TEMPLATE'])


if __name__ == "__main__":
    main()
