from pythonforandroid.recipe import PythonRecipe


class SimplePlotterRecipe(PythonRecipe):

    version = 'master'
    url = 'https://gitlab.com/thecker/simple-plotter/-/archive/master/simple-plotter-{version}.tar.gz'    

    depends = ['setuptools', 'setuptools_scm', 'kivy', 'jsonpickle', 'numpy', 'pytest', 'jinja2']
    # depends = ['setuptools', 'setuptools_scm', 'kivy', 'jsonpickle', 'numpy', 'matplotlib', 'pytest', 'jinja2']
    site_packages_name = 'simple_plotter'

    call_hostpython_via_targetpython = False


recipe = SimplePlotterRecipe()
