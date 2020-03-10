from setuptools import setup, find_packages
# import versioneer

# fetch readme for pypi
with open('README.rst', 'r') as file:
    readme = file.read()

# read version from AndroidManifest.xml
# with open('AndroidManifest.xml', 'r') as file:
#     lines = file.readlines()
#     for line in lines:
#         if 'android:versionName' in line:
#             version = line.split("\"")[1]

name = 'simple_plotter4a'
install_requires = [
    'simple-plotter>=0.3',
    'kivy>=1.11',
]

extras_require = {
    'kivy-matplotlib': ['matplotlib>=2'],
    'kivy-garden-graph': ['kivy-garden.graph>=0.4'],
    'all': ['matplotlib>=2', 'kivy-garden.graph>=0.4']
}

license = 'GPL3'
summary = "kivy based / Android optimized front-end for simple_plotter"
git_source = "https://gitlab.com/thecker/simple-plotter4a/"
doc_url = "https://simple-plotter.readthedocs.io/"
home = "https://simple-plotter.readthedocs.io/en/latest/"

setup(
    name=name,
    # version=versioneer.get_version(),
    # cmdclass=versioneer.get_cmdclass(),
    # version=version,
    packages=find_packages(),

    include_package_data=True,

    use_scm_version=True,

    install_requires=install_requires,
    extras_require=extras_require,
    entry_points={
        'gui_scripts': [
            'simple-plotter-kivy-matplotlib = simple_plotter4a.main:start_mpl [kivy-matplotlib]',
            'simple-plotter-kivy-garden-graph = simple_plotter4a.main:start_garden_graph [kivy-garden-graph]'
        ]
    },
    python_requires='>=3',

    # metadata to display on PyPI
    author="Thies Hecker",
    author_email="thies.hecker@gmx.de",
    description=summary,
    long_description=readme,
    long_description_content_type='text/x-rst',
    license=license,
    keywords="kivy Android plot plotting gui front-end",
    url=home,
    project_urls={
        "Documentation": doc_url,
        "Source Code": git_source,
    },
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ]
)
