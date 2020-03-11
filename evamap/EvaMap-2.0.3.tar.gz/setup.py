import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='EvaMap',
                 version='2.0.3',
                 description='A python library that can assess the quality of an RDF mapping',
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url='https://github.com/benjimor/EvaMap',
                 author='benjimor',
                 author_email='benjimor44@gmail.com',
                 license='MIT',
                 packages=setuptools.find_packages(),
                 install_requires=[
                     'rdflib',
                     'pyyaml',
                     'requests'
                 ],
                 classifiers=[
                     "Programming Language :: Python :: 3",
                     "License :: OSI Approved :: MIT License",
                     "Operating System :: OS Independent",
                 ],
                 keywords=["rdf", "mapping", "semantic web", "research"],
                 )
