import sys
import copy
import logging

from azureml.designer.serving.dagengine.Processor import load_graph, handle_request, handle_empty
from azureml.designer.serving.dagengine.Processor import pip_install, enable_rawhttp


def eprint(*args, **kwargs): print(*args, file=sys.stderr, **kwargs)


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.log = print
logger.info = print
logger.warning = eprint
logger.error = eprint


def init():
    logger.info('Using dagengine pip package.')
    pip_install('azureml.contrib.services')
    global graph
    graph = load_graph()
    enable_rawhttp()


def run(request):
    if request.method == 'POST':
        try:
            dag = copy.deepcopy(graph)
        except Exception as ex:
            # TODO: temporary fix
            logger.error(f'Error while deepcopying: {ex}')
            dag = copy.copy(graph)
        return handle_request(dag, request.get_data(), request.args)
    else:
        return handle_empty(request)
