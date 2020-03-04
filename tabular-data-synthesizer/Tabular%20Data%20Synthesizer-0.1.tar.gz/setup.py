import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='Tabular Data Synthesizer',
    version="0.1",
    author="Bauke Brenninkmeijer",
    author_email="bauke.brenninkmeijer@gmail.com",
    description="A package to evaluate how close a synthetic data set is to real data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Baukebrenninkmeijer/Tabular-data-synthesizer',
    keywords=['SYNTHETIC-DATA', 'GANs', 'SAMPLING', 'FAKE-DATA', 'TEST-DATA'],  # Keywords that define your package best
    packages=setuptools.find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'sdgym',
        'tqdm',
        'psutil',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

# setuptools.setup(
#     name='Tabular Data Synthesizers',  # How you named your package folder (MyLib)
#     packages=['tabular_data_synthesizer'],  # Chose the same as "name"
#     version='0.1',  # Start with a small number and increase it with every change you make
#     license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
#     description='Package to create synthetic data for industry using GANs.',  # Give a short description about your library
#     # long_description=long_description,
#     author='Bauke Brenninkmeijer',
#     author_email='bauke.brenninkmeijer@gmail.com',
#     url='https://github.com/Baukebrenninkmeijer/Tabular-data-synthesizer',  # Provide either the link to your github or to your website
#     keywords=['SYNTHETIC-DATA', 'GANs', 'SAMPLING', 'FAKE-DATA', 'TEST-DATA'],  # Keywords that define your package best
#     install_requires=[  # I get to this in a second
#         'pandas',
#         'neptune',
#         'numpy',
#         'sdgym',
#         'tqdm',
#         'psutil',
#     ],
#     classifiers=[
#         'Development Status :: 3 - Alpha',  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
#         'Intended Audience :: Developers',  # Define that your audience are developers
#         'Topic :: Software Development :: Build Tools',
#         'License :: OSI Approved :: MIT License',
#         'Programming Language :: Python :: 3.6',
#         'Programming Language :: Python :: 3.7',
#         'Programming Language :: Python :: 3.8',
#     ],
# )
