import os
import sys
from shutil import rmtree
from setuptools import setup, Command, find_packages


here = os.path.abspath(os.path.dirname(__file__))


class UploadCommand(Command):
    """Support setup.py publish."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except FileNotFoundError:
            pass
        self.status("Building Source distribution…")
        os.system("{0} setup.py sdist bdist_wheel".format(sys.executable))
        self.status("Uploading the package to PyPi via Twine…")
        os.system("sudo twine upload dist/*")
        sys.exit()

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "linkkt_e2e_handlers",
    version="0.1.3",
    author = "Kevin Hill",
    author_email = "kah.kevin.hill@gmail.com",
    description = ("Cross service interaction"),
    license = "BSD",
    keywords = "example documentation tutorial",
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=[
        'jamboree', 'mlfinlab', 'sklearn',
        'cytoolz', 'loguru', 
        'maya', 'crayons'
    ],
    cmdclass={"upload": UploadCommand},
)