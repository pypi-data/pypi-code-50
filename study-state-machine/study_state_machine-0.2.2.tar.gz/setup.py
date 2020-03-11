import io
import os
import re
from setuptools import setup

DOCUMENTATION_URL = "https://study_state_machine.readthedocs.io/en/stable/"
SOURCE_CODE_URL = "https://github.com/bedapub/study-state-machine"

module_path = os.path.dirname(__file__)

with io.open(os.path.join(module_path, "study_state_machine/__init__.py"), "rt", encoding="utf8") as f:
    version = re.search(r"__version__ = \"(.*?)\"", f.read()).group(1)

with io.open(os.path.join(module_path, "./README.rst"), "rt", encoding="utf8") as f:
    LONG_DESCRIPTION = f.read()


setup(
    name="study_state_machine",
    version=version,
    url=SOURCE_CODE_URL,
    project_urls={
        "Documentation": DOCUMENTATION_URL,
        "Code": SOURCE_CODE_URL,
    },
    author="Rafael S. Müller",
    author_email="rafa.molitoris@gmail.com",
    description="A package to control the state of a study",
    packages=["study_state_machine"],
    long_description=LONG_DESCRIPTION,
    install_requires=[

    ],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
    ],
    extra_require={
        "dev": [
            "unittest"
            "coverage",
        ],
        "docs": [
            "Sphinx",
            "sphinx-rdt-theme"
        ],
    }

)
