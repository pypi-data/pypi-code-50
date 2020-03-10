import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

data = ['beacon',  'bee_hive',  'blinker', ' block', 'boat',
        'diehard', ' glider', ' glider__',
        'gosper_glider_gun',  '__init__.py', 'loaf',
        'pulsar', 'r_pentominoi', 'toad', 'tub']

setuptools.setup(
    name="game-of-life-MUGOH",
    version="0.0.16",
    include_package_data=True,
    package_data={'game_of_life': ['game_of_life/.data/*', 'config.json']},
    author="mugoh",
    author_email="mugoh.ks@gmail.com",
    description="Conway's game of life in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hogum/game-of-life",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=['numpy'],
)
