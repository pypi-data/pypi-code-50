from bottle import request
from bottle_elastic_apm.constants import HEADER_TRACER_PARENT, HTTP_WITH_BODY
from elasticapm.utils import compat, get_url_dict
from elasticapm.utils.disttracing import TraceParent


def get_data_from_request(server_request, capture_body=False,
                          capture_headers=True):
    data = {
        "method": server_request.method,
        "socket": {
            "remote_address": server_request.remote_addr,
            "encrypted": 'https' == server_request.urlparts[0]
        },
        "cookies": dict(**server_request.cookies),
        "url": get_url_dict(server_request.url)
    }
    if capture_headers:
        data["headers"] = dict(**server_request.headers)
        data["headers"].pop("Cookie", None)
    if request.method in HTTP_WITH_BODY:
        if request.content_type == "application/x-www-form-urlencoded":
            body = compat.multidict_to_dict(request.forms)
        elif request.content_type and request.content_type.startswith(
                "multipart/form-data"):
            body = compat.multidict_to_dict(request.forms)
            if request.files:
                body["_files"] = {
                    field: val[0].filename if len(val) == 1 else [f.filename
                                                                  for f in val]
                    for field, val in compat.iterlists(request.files)
                }
        elif request.json:
            body = request.json
        else:
            body = request.body.read().decode('utf-8')

        if body is not None:
            data["body"] = body if capture_body else "[REDACTED]"
    return data


def get_data_from_response(server_response, capture_headers=True):
    data = {"status_code": server_response.status_code}
    if capture_headers and server_response.headers:
        data["headers"] = {
            key: ";".join(server_response.headers.getall(key))
            for key in compat.iterkeys(server_response.headers)
        }
    return data


def trace_parent():
    trace_parent_header = request.headers.get(HEADER_TRACER_PARENT)
    if not trace_parent_header:
        return None
    return TraceParent.from_string(trace_parent_header)
