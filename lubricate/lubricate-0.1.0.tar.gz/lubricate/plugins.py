#!/usr/bin/env python3
import os
import subprocess
import venv


class VirtualEnv:
    def __init__(self, path):
        self.create_virtualenv(path)
        self.install_packages(path)

    def create_virtualenv(self, path):
        """Creats an isolated virtual Python environment"""
        print("Creating virtualenv")
        venv.create(os.path.join(path, "venv"), with_pip=True)

    def install_packages(self, path):
        """Install all required Python packages"""
        print("Installing packages")
        pip_cmd = os.path.join(path, "venv", "bin", "pip")
        subprocess.run([pip_cmd, "install", "--upgrade", "pip", "setuptools"])
        with open(os.path.join(path, "requirements.txt")) as fobj:
            for package in fobj.readlines():
                subprocess.run([pip_cmd, "install", package])
