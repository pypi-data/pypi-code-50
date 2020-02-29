from typing import *

from fifteenrock.core.core import deploy
from fifteenrock.lib import util, helper
from fifteenrock.template import main as template_main
from pathlib import Path
import pandas as pd
# import nbformat
# import nbconvert
# from nbconvert import PythonExporter

# from notebook.notebookapp import list_running_servers
import re
from urllib.parse import urlencode, urljoin

import logging
import json
from urllib.request import urlopen
from os import path
# import ipykernel
import time

log = logging.getLogger(__name__)


def trial():
    print('Hi Rajiv')


# class StripMagicsProcessor(nbconvert.preprocessors.Preprocessor):
#     """
#     Preprocessor to convert notebooks to Python source while stripping
#     out all magics (i.e IPython specific syntax).
#     """
#
#     _magic_pattern = re.compile('^\s*(?P<magic>%%\w\w+)($|(\s+))')
#
#     def strip_magics(self, source):
#         """
#         Given the source of a cell, filter out all cell and line magics.
#         """
#         filtered = []
#         for line in source.splitlines():
#             match = self._magic_pattern.match(line)
#             if match is None:
#                 filtered.append(line)
#             else:
#                 msg = 'Stripping out IPython magic {magic} in code cell {cell}'
#                 message = msg.format(cell=self._cell_counter, magic=match.group('magic'))
#                 log.warn(message)
#         return '\n'.join(filtered)
#
#     def preprocess_cell(self, cell, resources, index):
#         if cell['cell_type'] == 'code':
#             self._cell_counter += 1
#             cell['source'] = self.strip_magics(cell['source'])
#         return cell, resources
#
#     def __call__(self, nb, resources):
#         self._cell_counter = 0
#         return self.preprocess(nb, resources)


# PREPROCESSORS = [StripMagicsProcessor()]


# OLD
# def notebook_file_name(ikernel):
#     """Return the full path of the jupyter notebook."""
#     # Check that we're running under notebook
#     if not (ikernel and ikernel.config['IPKernelApp']):
#         return
#
#     kernel_id = re.search('kernel-(.*).json',
#                           ipykernel.connect.get_connection_file()).group(1)
#     print('Kernel Id')
#     print(kernel_id)
#     servers = list_running_servers()
#     print('Running Servers')
#     print(servers)
#
#     for srv in servers:
#         query = {'token': srv.get('token', '')}
#         print('Query')
#         print(query)
#         print('Server Url')
#         print(srv['url'])
#         url = urljoin(srv['url'], 'api/sessions') + '?' + urlencode(query)
#         print("Url")
#         print(url)
#         for session in json.load(urlopen(url)):
#             if session['kernel']['id'] == kernel_id:
#                 relative_path = session['notebook']['path']
#                 return path.join(srv['notebook_dir'], relative_path)


def notebook_file_name(ikernel):
    """Return the full path of the jupyter notebook."""
    # Check that we're running under notebook
    if not (ikernel and ikernel.config['IPKernelApp']):
        return

    from notebook.notebookapp import list_running_servers
    import ipykernel

    kernel_id = re.search('kernel-(.*).json',
                          ipykernel.connect.get_connection_file()).group(1)

    servers = list_running_servers()
    for srv in servers:
        query = {'token': srv.get('token', '')}
        url = urljoin(srv['url'], 'api/sessions') + '?' + urlencode(query)
        for session in json.load(urlopen(url)):
            if session['kernel']['id'] == kernel_id:
                relative_path = session['notebook']['path']
                return path.join(srv['notebook_dir'], relative_path)


# def notebook_file_name(ikernel):
#     """Return the full path of the jupyter notebook."""
#     # Check that we're running under notebook
#     if not (ikernel and ikernel.config['IPKernelApp']):
#         return
#
#     kernel_id = re.search('kernel-(.*).json',
#                           ipykernel.connect.get_connection_file()).group(1)
#     print('Kernel')
#     print(kernel_id)
#
#     servers = list_running_servers()
#     print('Servers')
#     print(servers)
#
#     for srv in servers:
#         query = {'token': srv.get('token', '')}
#         print('Query')
#         print(query)
#         url = urljoin(srv['url'], 'api/sessions') + '?' + urlencode(query)
#         print('Url')
#         print(url)
#         for session in json.load(urlopen(url)):
#             if session['kernel']['id'] == kernel_id:
#                 relative_path = session['notebook']['path']
#                 return path.join(srv['notebook_dir'], relative_path)


def notebook_file_name_hub(ikernel, credentials):
    import requests
    import ipykernel
    import re
    from notebook.notebookapp import list_running_servers
    kernel_id = re.search('kernel-(.*).json', ipykernel.connect.get_connection_file()).group(1)
    token = credentials['hub_token']

    servers = list_running_servers()
    for srv in servers:
        base_url = srv['url']
        r = requests.get(
            url=base_url + 'api/sessions',
            headers={'Authorization': 'token {}'.format(token), })

        r.raise_for_status()
        sessions = r.json()
        for session in sessions:
            if session['kernel']['id'] == kernel_id:
                relative_path = session['notebook']['path']
                return path.join(srv['notebook_dir'], relative_path)


# def notebook_file_name_hub(ikernel, credentials):
#     import requests
#     import ipykernel
#     import re
#     from notebook.notebookapp import list_running_servers
#
#     token = credentials['hub_token']
#     print('Token')
#     print(token)
#
#     server = next(list_running_servers())
#     base_url = server['url']
#     r = requests.get(
#         url=base_url + 'api/sessions',
#         headers={'Authorization': 'token {}'.format(token), })
#
#     r.raise_for_status()
#     response = r.json()
#
#     kernel_id = re.search('kernel-(.*).json', ipykernel.connect.get_connection_file()).group(1)
#     relative_path = {r['kernel']['id']: r['notebook']['path'] for r in response}[kernel_id]
#     return relative_path

def deploy_project(project: str, requirements: List[str] = None, url: str = None,
                   dependencies: List = None,
                   credentials: Dict = None, credentials_file: str = None,
                   spec: Dict = None,
                   metadata: Dict = None,
                   framework: str = None,
                   description: str = None) -> pd.DataFrame:
    """
        sample url: https://staging.app.15rock.com/gateway/data/v1/master
    """

    if not is_notebook():
        return None
    # get the url from the json
    credentials_json = helper.get_credentials(credentials, credentials_file)
    if ('compute_url' not in credentials_json) and not url:
        raise ValueError('Either put "compute_url" in your fifteenrock.json file or provide the url')

    _compute_url = url or credentials_json['compute_url']

    if 'faas_token' not in credentials_json:
        raise ValueError('Error in getting the faas token from the credentials json')

    from fifteenrock.core.compute_client import compute as make_compute
    compute = make_compute(url=_compute_url)
    compute.deploy_notebook(project=project,
                            requirements=requirements,
                            dependencies=dependencies,
                            credentials=credentials,
                            credentials_file=credentials_file,
                            spec=spec,
                            metadata=metadata,
                            framework=framework,
                            description=description)

    # deploy_notebook(project,
    #                 requirements,
    #                 _compute_url,
    #                 dependencies,
    #                 credentials,
    #                 credentials_file,
    #                 spec,
    #                 metadata,
    #                 framework,
    #                 description)


def deploy_notebook(project: str, requirements: List[str] = None, url: str = None,
                    dependencies: List = None,
                    credentials: Dict = None, credentials_file: str = None,
                    spec: Dict = None,
                    metadata: Dict = None,
                    framework: str = None,
                    description: str = None,
                    do_notebook_func=None) -> None:
    """
    This function should be only called from within a notebook. In all other scenarios, it is a no-op.
    :param project:
    :param requirements: List of pip libraries required by your code.
    :param url:
    :param dependencies:
    :param credentials:
    :param credentials_file:
    :param spec:
    :param metadata:
    :return:
    """

    do_notebook_func = do_notebook_func or do_notebook
    if is_notebook():
        save_current_notebook()
        _deploy_notebook(credentials, credentials_file, dependencies, description, framework,
                         metadata, project, requirements, spec, url, do_notebook_func)

    else:
        pass


def _deploy_notebook(credentials, credentials_file, dependencies, description, framework, metadata,
                     project, requirements, spec, url, do_notebook_func, base_folder: Path = None):
    try:

        tmp_dir = base_folder or util.tmp_folder()
        module_path = str(tmp_dir / 'fifteenrock_project_main.py')
        credentials = helper.get_credentials(credentials, credentials_file)

        do_notebook_func(credentials, module_path)

        spec = spec or dict()
        metadata = metadata or dict()
        if not requirements:
            requirements = ['ipywidgets', 'fifteenrock']
        else:
            requirements = requirements + ['ipywidgets', 'fifteenrock']

        requirements_file = str(util.make_requirements_file_notebook(tmp_dir, requirements))
        main_file = str(template_main.__file__)
        # main_file = './fifteenrock/template/main.py'
        if not dependencies:
            dependencies = [module_path]
        else:
            dependencies = dependencies + [module_path]

        result = deploy(credentials=credentials, credentials_file=credentials_file,
                        project=project,
                        url=url,
                        main_file=main_file,
                        dependencies=dependencies,
                        requirements_file=requirements_file,
                        spec=spec,
                        metadata=metadata,
                        framework=framework,
                        description=description)
        return result
    except Exception as e:
        raise e
    finally:
        print(tmp_dir)
        # util.remove_dir(tmp_dir)
        pass


def do_notebook(credentials, module_path):
    from IPython import get_ipython
    import ipykernel
    kernel = get_ipython()
    notebook_path = notebook_file_name_hub(kernel, credentials)
    convert_notebook(notebook_path, module_path)


# def deploy_notebook_hub(project: str, function: str, url: str = None, dependencies: List = None,
#                     credentials: Dict = None, credentials_path: str = None) -> None:
#     if is_notebook():
#         save_current_notebook()
#         credentials = helper.get_credentials(credentials, credentials_path)
#         from IPython import get_ipython
#         import ipykernel
#
#         kernel = get_ipython()
#         print('Hi Rajiv')
#
#         notebook_path = notebook_file_name_hub(kernel, credentials)
#         print(notebook_path)
#
#
#
#     else:
#         print('WARNING: deploy_notebook is only executed from a notebook')
#         pass


def save_current_notebook():
    from IPython.display import Javascript

    script = '''
    require(["base/js/namespace"],function(Jupyter) {
        Jupyter.notebook.save_checkpoint();
    });
    '''
    Javascript(script)
    time.sleep(5)
    # print('This notebook has been saved.')


# def convert_notebook(notebook_path, module_path):
#     with open(notebook_path) as fh:
#         nb = nbformat.reads(fh.read(), nbformat.NO_CONVERT)
#
#     exporter = PythonExporter()
#     source, meta = exporter.from_notebook_node(nb)
#
#     with open(module_path, 'w') as fh:
#         fh.writelines(source)


def convert_notebook(notebook_path, module_path, preprocessors=None):
    import nbconvert

    class StripMagicsProcessor(nbconvert.preprocessors.Preprocessor):
        """
        Preprocessor to convert notebooks to Python source while stripping
        out all magics (i.e IPython specific syntax).
        """

        _magic_pattern = re.compile('^\s*(?P<magic>%%\w\w+)($|(\s+))')

        def strip_magics(self, source):
            """
            Given the source of a cell, filter out all cell and line magics.
            """
            filtered = []
            for line in source.splitlines():
                match = self._magic_pattern.match(line)
                if match is None:
                    filtered.append(line)
                else:
                    msg = 'Stripping out IPython magic {magic} in code cell {cell}'
                    message = msg.format(cell=self._cell_counter, magic=match.group('magic'))
                    log.warn(message)
            return '\n'.join(filtered)

        def preprocess_cell(self, cell, resources, index):
            if cell['cell_type'] == 'code':
                self._cell_counter += 1
                cell['source'] = self.strip_magics(cell['source'])
            return cell, resources

        def __call__(self, nb, resources):
            self._cell_counter = 0
            return self.preprocess(nb, resources)

    class TerminalCommandsProcessor(nbconvert.preprocessors.Preprocessor):
        _terminal_pattern = re.compile('^!.*')

        def strip_terminal_commands(self, source):
            """
            Given the source of a cell, filter out all cell and line ter1minal commands.
            """
            filtered = []
            for line in source.splitlines():
                match = self._terminal_pattern.match(line)
                if match is None:
                    filtered.append(line)
                else:
                    msg = 'Commenting out IPython Terminal Commands {command} in code cell {cell}'
                    message = msg.format(cell=self._cell_counter, command=match.group(0))
                    log.warn(message)
                    filtered.append("#" + line)
            return '\n'.join(filtered)

        def preprocess_cell(self, cell, resources, index):
            if cell['cell_type'] == 'code':
                self._cell_counter += 1
                cell['source'] = self.strip_terminal_commands(cell['source'])
            return cell, resources

        def __call__(self, nb, resources):
            self._cell_counter = 0
            return self.preprocess(nb, resources)

    default_preprocessors = [StripMagicsProcessor(), TerminalCommandsProcessor()]
    preprocessors = preprocessors or default_preprocessors
    import nbformat
    from nbconvert import PythonExporter
    with open(notebook_path) as fh:
        nb = nbformat.reads(fh.read(), nbformat.NO_CONVERT)

    exporter = PythonExporter()
    for preprocessor in preprocessors:
        exporter.register_preprocessor(preprocessor)

    source, meta = exporter.from_notebook_node(nb)
    source = source.replace('get_ipython().run_line_magic', '')

    with open(module_path, 'w') as fh:
        fh.writelines(source)


def is_notebook():
    try:
        from IPython import get_ipython
    except ImportError as ex:
        return False

    try:
        kernel = get_ipython()
        shell = kernel.__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True  # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False  # Probably standard Python interpreter


import ipywidgets as widgets
from ipywidgets import Layout, HBox, Label
from IPython.core.display import clear_output, display


def deploy_form():
    # project: str, requirements: List[str] = None, url: str = None,
    #                     dependencies: List = None,
    #                     credentials: Dict = None, credentials_file: str = None,
    #                     spec: Dict = None,
    #                     metadata: Dict = None,
    #                     framework: str = None,
    #                     description: str = None
    default_text_area = """
    build:
        commands:
            - apt-get upgrade -y python-pip
    """
    style = {'description_width': 'initial'}
    default_layout = Layout(width='50%')
    label_layout = Layout(width='20%')

    # default_layout = Layout(
    #     display='flex',
    #     flex_flow='row',
    #     justify_content='space-between',
    # )
    project_name_textbox = widgets.Text(
        placeholder='',
        layout=default_layout,
        style=style
    )

    project_name_hbox = HBox([Label('Project(required)', layout=label_layout), project_name_textbox])
    # requirements_textbox = widgets.Text(
    #     placeholder='e.g. tensorflow, flake8==3.5.0',
    #     # description='Python libraries(Optional)',
    #     layout=default_layout,
    #     style=style
    # )
    # requirements_hbox = HBox([Label('Python libraries(Optional)', layout=label_layout), requirements_textbox])
    spec_textarea = widgets.Textarea(
        placeholder=default_text_area,
        layout=default_layout,
        # style=style
    )
    spec_hbox = HBox([Label('YAML Specification(Optional)', layout=label_layout), spec_textarea])
    # framework_textbox = widgets.Text(
    #     placeholder='default is nuclio. One of ["flask", "nuclio"]',
    #     layout=default_layout,
    #     # style=style
    # )

    # framework_hbox = HBox([Label('Framework(Optional)', layout=label_layout), framework_textbox])

    description_textbox = widgets.Text(
        placeholder='My amazing project',
        layout=default_layout,
        # style=style
    )
    description_hbox = HBox([Label('Description(Optional)', layout=label_layout), description_textbox])
    # endpoint_textbox = widgets.Text(
    #     layout=default_layout,
    #
    # )
    # endpoint_hbox = HBox([Label('Endpoint(Optional)', layout=label_layout), endpoint_textbox])
    #
    # url_textbox = widgets.Text(
    #     value='Enter Url',
    #     description='Url', )

    button = widgets.Button(description='Deploy Notebook')
    status_label = Label('', layout=label_layout)
    button_hbox = HBox([button, status_label])
    output = widgets.Output()

    def on_button_clicked(_):
        # "linking function with output"
        with output:
            # what happens when we press the button
            clear_output()
            status_label.value = "This will take a while.."
            # function_name = function_name_textbox.value
            project_name = project_name_textbox.value
            # ur_value = url_textbox.value
            # requirements_list = [s.strip() for s in requirements_textbox.value.split(",")]
            requirements_list = []
            spec = util.from_yaml(spec_textarea.value)
            # framework = framework_textbox.value
            description = description_textbox.value
            # url = endpoint_textbox.value
            # call function from here
            # logic for calling the method can be added here
            # deploy_notebook(project= project_name, requirements=requirements_list,spec=spec, framework=framework, description=description)
            # result = dict(project=project_name, requirements=requirements_list, spec=spec, framework=framework,
            #               description=description, url=url)
            result = dict(project=project_name, spec=spec, description=description)
            try:
                deploy_notebook(**result)
            except Exception as e:
                status_label.value = ""
                raise e
            finally:
                status_label.value = ""

        # linking button and function together using a button's method

    button.on_click(on_button_clicked)
    # displaying button and its output together
    # deploy_widget = widgets.VBox(
    #     [project_name_hbox, requirements_hbox, spec_hbox, framework_hbox, description_hbox, endpoint_hbox, button_hbox,
    #      output])
    deploy_widget = widgets.VBox(
        [project_name_hbox, spec_hbox, description_hbox, button_hbox, output])
    display(deploy_widget)
