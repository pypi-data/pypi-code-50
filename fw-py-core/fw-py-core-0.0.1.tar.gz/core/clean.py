import os
import shutil
from setuptools import Command


class CleanCommand(Command):

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print("Running clean")
        shutil.rmtree("./build", ignore_errors=True)
        shutil.rmtree("./dist", ignore_errors=True)
        print("Completed clean up")
