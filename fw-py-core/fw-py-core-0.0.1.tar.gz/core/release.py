from setuptools import Command
from subprocess import Popen
import sys


class ReleaseCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def build(self):

        """
        Build a wheel distribution.
        """
        code = Popen([sys.executable, "setup.py", "clean", "sdist"]).wait()
        if code:
            raise RuntimeError("Error building wheel")

    def publish(self):
        """
        Publish the distribution to local PyPi.
        """
        process = Popen(["twine", "upload", "-u" , "Rainmakers","-p", "Junkyfunky8990#", "dist/*"])

    def run(self):
        print("Running Build")
        self.build()
        print("Completed Build")
        print("Running release")
        self.publish()
        print("Completed release")
