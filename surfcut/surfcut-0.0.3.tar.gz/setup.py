from setuptools import setup, find_packages

from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

requirements = [
    "numpy",
    "scipy",
    "napari>=0.2.12",
    "tifffile",
    "pillow",
    "scikit-image",
]


setup(
    name="surfcut",
    version="0.0.3",
    description="Cutting confocal stacks at various depths relative to surface signal ",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    install_requires=requirements,
    python_requires=">=3.6",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "surfcut = surfcut.run:main",
            "surfcut-gui = surfcut.gui:main",
        ]
    },
    include_package_data=True,
    zip_safe=False,
)
