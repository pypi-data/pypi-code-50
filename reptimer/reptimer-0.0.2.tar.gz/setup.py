import setuptools

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name="reptimer",  # name of the project, has to be unique
    version="0.0.2",  # version number follows PEP 440
    author="Guilherme Salome",
    author_email="guilhermesalome@gmail.com",
    description="A timer that repeats and beeps.",  # 1 sentence description of package
    long_description=long_description,  # shown on PyPA package page
    long_description_content_type="text/markdown",  # format for description file
    url="https://github.com/Salompas/timer",  # url of the package repo
    packages=setuptools.find_packages(),  # packages to be distributed
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Development Status :: 1 - Planning",
        "Operating System :: MacOS",
    ],
    entry_points={"console_scripts": ["reptimer=reptimer.commandline:main"]},
    include_package_data=True,
)
