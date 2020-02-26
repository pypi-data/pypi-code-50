#!/usr/bin/python3
import subprocess


class ProjectLocation(object):
    def __init__(self):
        self.current_project_location = repr(subprocess.Popen(
            ["pwd"], stdout=subprocess.PIPE).communicate()[0])
        self.current_project_location = self.current_project_location.split(
            '/')[-2].split('\\')[0]

    def get_project_location(self):
        return self.current_project_location
