import setuptools

def long_description():
    with open('README.md') as f:
        return f.read()

setuptools.setup(
        name = 'pyven',
        version = '23',
        description = 'Management of PYTHONPATH for simultaneous dev of multiple projects',
        long_description = long_description(),
        long_description_content_type = 'text/markdown',
        url = 'https://github.com/combatopera/pyven',
        author = 'Andrzej Cichocki',
        packages = setuptools.find_packages(),
        py_modules = ['pkg_resources_lite'],
        install_requires = ['nose', 'pyflakes', 'twine', 'aridity'],
        package_data = {'': ['*.pxd', '*.pyx', '*.pyxbld', '*.arid', '*.aridt']},
        scripts = ['bootstrap', 'foreignsyms'],
        entry_points = {'console_scripts': ['checks=pyven.checks:main_checks', 'tests=pyven.checks:main_tests', 'gclean=pyven.gclean:main_gclean', 'initopt=pyven.initopt:main_initopt', 'release=pyven.release:main_release', 'tasks=pyven.tasks:main_tasks', 'travis_ci=pyven.travis_ci:main_travis_ci']})
