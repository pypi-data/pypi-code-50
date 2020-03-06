import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ketaway", # Replace with your own username
    version="0.0.4",
    author = 'Mongkolchai Worakhajee',
    author_email = 'ketaway@gmail.com',
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ketaway/ketaway",
	download_url = 'https://github.com/ketaway/ketaway/archive/0.0.4.zip',    # I explain this later on
	keywords = ['ketaway', 'Mongkolchai'],   # Keywords that define your package best
    packages=setuptools.find_packages(),
    classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    ],
    python_requires='>=3',
)