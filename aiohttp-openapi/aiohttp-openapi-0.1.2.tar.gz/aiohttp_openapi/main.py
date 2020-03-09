import pathlib
import re

from aiohttp import web

_YAML_DATA = ''


def setup_openapi(app, yaml_path=None):
    _load_yml(yaml_path)
    _travers_endpoints(app)

    swagger_ui_path = pathlib.Path(__file__).parent / 'dist'
    app.router.add_static('/dist', swagger_ui_path, show_index=True)

    app.router.add_get('/docs', redirect_to_index)
    app.router.add_get('/docs/', redirect_to_index)
    app.router.add_get('/swagger', stream_yaml)


async def redirect_to_index(_):
    return web.HTTPFound('/dist/index.html')


async def stream_yaml(request):
    global _YAML_DATA
    stream = web.StreamResponse()
    await stream.prepare(request)
    await stream.write(_YAML_DATA.encode())
    await stream.write_eof()
    return stream


def _travers_endpoints(app) -> None:
    global _YAML_DATA
    d_tree = {}
    for route in app.router.routes():
        method = route.method.lower()
        if method == 'head':
            continue
        endpoint = route.resource.canonical
        if d_tree.get(endpoint) is None:
            d_tree[endpoint] = {}

        if route.handler.__doc__ and '---' in route.handler.__doc__:
            try:
                docstr = route.handler.__doc__.splitlines()
            except AttributeError:
                return None
            opanapi_docstr = _extract_openapi_docstr(docstr)
            is_valid_docstr: bool = _is_valid_docstr(opanapi_docstr, endpoint, method)
            assert is_valid_docstr, f'docstr does not match handler definition ({method} {endpoint})'
            if is_valid_docstr:
                d_tree[endpoint][method] = _remove_endpoint_and_method(opanapi_docstr)

    # join dict to a single file
    for endpoint in d_tree:
        if len(d_tree[endpoint]) > 0:
            _YAML_DATA += f'    {endpoint}:'
            for method in d_tree[endpoint]:
                _YAML_DATA += f'\n        {method}:'
                docstr = d_tree[endpoint][method]
                _YAML_DATA += docstr


def _load_yml(yaml_path) -> None:
    """
    Load global yaml file if one exist.
    :param yaml_path:
    :return: None
    """
    global _YAML_DATA
    with open(yaml_path, 'r') as yaml_file:
        data = yaml_file.read()
        _YAML_DATA += data
    if 'paths' not in _YAML_DATA:
        _YAML_DATA += 'paths:\n'


def _is_valid_docstr(docstr: str, endpoint: str, method: str) -> bool:
    """
    Check if first two lines of the docstr matches with a handler's endpoint & method.
    :param endpoint:
    :param method:
    :param docstr:
    :return:
    """
    # TODO: do not hard code tab's spaces size
    first_line: str = '\\s{4}' + endpoint + ':\n'  # 4 white spaces ENDPOINT: newline
    second_line: str = '\\s{8}' + method + ':\n'  # 8 white spaces METHOD: newline
    pattern: str = first_line + second_line
    result = re.search(pattern, docstr)
    if result is None:
        print(docstr)
    return result is not None


def _remove_endpoint_and_method(docstr: str) -> str:
    second_new_line = _find_nth(docstr, '\n', 2)
    return docstr[second_new_line:]


def _extract_openapi_docstr(end_point_doc):
    # Find Swagger start point in doc
    endpoint_swagger_start = 0
    for i, doc_line in enumerate(end_point_doc):
        if '---' in doc_line:
            endpoint_swagger_start = i + 1
            break

    out = '\n'.join(end_point_doc[endpoint_swagger_start:-1])
    out += '\n'
    return out


def _find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start
