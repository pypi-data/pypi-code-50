import setuptools

with open("./ActivityTasks/README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="activityTasks-udacity-inventrohyder", 
    version="0.1.0a",
    author="Haitham Alhad",
    author_email="haitham.hyder@minerva.kgi.edu",
    description="A Activity and Tasks package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Inventrohyder/CS110/tree/master/Assignments/cs110_assignment_2/package",
    packages=setuptools.find_packages()
)